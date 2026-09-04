"""
Squadron Activity Report Generator

This script demonstrates how to use the report_functions module
to generate a comprehensive squadron activity report.

Students will build this step-by-step in the assignment.
"""

import report_functions as rf


def generate_squadron_report(squadron_code, output_file):
    """
    Generates a comprehensive activity report for a specific squadron.

    Args:
        squadron_code (str): Squadron identifier (e.g., 'VFA-41')
        output_file (str): Path to save the report
    """
    # TODO: PART 1 - Load the data files
    pilots = rf.read_csv_file('../data/pilots.csv')
    aircraft = rf.read_csv_file('../data/aircraft.csv')
    flight_logs = rf.read_csv_file('../data/flight_logs.csv')

    # TODO: PART 2 - Filter data for the specified squadron
    squadron_pilots = rf.filter_by_field(
        pilots,
        'squadron',
        squadron_code
    )

    squadron_aircraft = rf.filter_by_field(
        aircraft,
        'squadron',
        squadron_code
    )

    # TODO: PART 3 - Get flights for squadron pilots
    squadron_flights = []

    for pilot in squadron_pilots:
        pilot_flights = rf.filter_by_field(
            flight_logs,
            'pilot_id',
            pilot['pilot_id']
        )

        squadron_flights.extend(pilot_flights)

    # TODO: PART 4 - Calculate statistics
    completed_flights = rf.filter_by_field(
        squadron_flights,
        'status',
        'Completed'
    )

    cancelled_flights = rf.filter_by_field(
        squadron_flights,
        'status',
        'Cancelled'
    )

    logged_missions = rf.count_records(squadron_flights)
    total_missions = rf.count_records(completed_flights)
    cancelled_missions = rf.count_records(cancelled_flights)

    total_hours = rf.calculate_total(
        completed_flights,
        'duration_hours'
    )

    average_duration = rf.calculate_average(
        completed_flights,
        'duration_hours'
    )

    mission_types = rf.get_unique_values(
        squadron_flights,
        'mission_type'
    )

    mission_breakdown = {}

    for mission_type in mission_types:
        matching_flights = rf.filter_by_field(
            completed_flights,
            'mission_type',
            mission_type
        )

        mission_breakdown[mission_type] = rf.count_records(
            matching_flights
        )
        mission_types = rf.get_unique_values(
        squadron_flights,
        'mission_type'
    )

    active_aircraft = rf.filter_by_field(
        squadron_aircraft,
        'status',
        'Active'
    )

    maintenance_aircraft = rf.filter_by_field(
        squadron_aircraft,
        'status',
        'Maintenance'
    )

    active_aircraft_count = rf.count_records(active_aircraft)
    maintenance_aircraft_count = rf.count_records(
        maintenance_aircraft
    )

    # TODO: PART 5 - Build the report content
    report_lines = [
        rf.format_header(
            f"{squadron_code} SQUADRON ACTIVITY REPORT"
        ),
        "",
        "Flight hours and mission breakdown use completed missions.",
        "",
        "PERSONNEL ROSTER",
        "-" * 60
    ]

    for pilot in squadron_pilots:
        pilot_line = (
            f"{pilot['pilot_id']} | "
            f"{pilot['rank']} "
            f"{pilot['first_name']} {pilot['last_name']} "
            f"({pilot['callsign']})"
        )

        report_lines.append(pilot_line)

    report_lines.extend([
        "",
        "AIRCRAFT INVENTORY",
        "-" * 60
    ])

    for plane in squadron_aircraft:
        aircraft_line = (
            f"{plane['tail_number']} | "
            f"{plane['model']} | "
            f"{plane['status']}"
        )

        report_lines.append(aircraft_line)

    report_lines.extend([
        "",
        "FLIGHT OPERATIONS SUMMARY",
        "-" * 60,
        f"Logged flight records: {logged_missions}",
        f"Completed missions flown: {total_missions}",
        f"Cancelled missions: {cancelled_missions}",
        f"Flight hours (completed): {total_hours:.1f}",
        f"Average duration (completed): "
        f"{average_duration:.2f} hours"
    ])

    report_lines.extend([
        "",
        "COMPLETED MISSIONS BY TYPE",
        "-" * 60
    ])

    for mission_type in mission_breakdown:
        mission_count = mission_breakdown[mission_type]

        report_lines.append(
            f"{mission_type}: {mission_count}"
        )

    report_lines.extend([
        "",
        "OPERATIONAL STATUS",
        "-" * 60,
        "Aircraft status as recorded in the supplied inventory:",
        f"Active aircraft: {active_aircraft_count}",
        f"Aircraft in maintenance: {maintenance_aircraft_count}"
    ])

    report_content = "\n".join(report_lines) + "\n"
    print(report_content)

    # TODO: PART 6 - Write the report to file
    rf.write_report_to_file(
        output_file,
        report_content
    )

# Main execution
if __name__ == '__main__':
    # TODO: Students will customize this to generate reports for different squadrons
    print("Generating squadron activity reports...")
    squadron_codes = [
        'VFA-41',
        'VFA-25',
        'VFA-154',
        'VFA-113',
        'VFA-14',
        'VFA-192',
        'VFA-2'
    ]

    for squadron_code in squadron_codes:
        output_file = (
            f"../reports/{squadron_code.lower()}-report.txt"
        )

        generate_squadron_report(
            squadron_code,
            output_file
        )
    print("Report generation complete.")
