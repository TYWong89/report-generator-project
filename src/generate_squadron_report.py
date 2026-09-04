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
    # temp test check for pt2

    print()
    print(f"Squadron: {squadron_code}")

    print(
        f"Assigned pilots: "
        f"{rf.count_records(squadron_pilots)}"
    )

    print(
        f"Assigned aircraft: "
        f"{rf.count_records(squadron_aircraft)}"
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
    # Temporary checks for Part 3
    print()

    print(
        f"Flight records for {squadron_code}: "
        f"{rf.count_records(squadron_flights)}"
    )

    print(
        "Pilot IDs in those records:",
        rf.get_unique_values(squadron_flights, 'pilot_id')
    )

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
     # Count the mission records
    logged_missions = rf.count_records(squadron_flights)
    total_missions = rf.count_records(completed_flights)
    cancelled_missions = rf.count_records(cancelled_flights)

    # Calculate hours using completed flights
    total_hours = rf.calculate_total(
        completed_flights,
        'duration_hours'
    )

    average_duration = rf.calculate_average(
        completed_flights,
        'duration_hours'
    )
     # Find the mission types present in the squadron's logs
    mission_types = rf.get_unique_values(
        squadron_flights,
        'mission_type'
    )

    # Count completed missions for each type
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
        # Separate aircraft by their recorded status
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
    # Temporary checks for Part 4
    print()
    print("PART 4 CHECKS")

    print(f"Logged missions: {logged_missions}")
    print(f"Completed missions: {total_missions}")
    print(f"Cancelled missions: {cancelled_missions}")

    print(f"Total flight hours: {total_hours:.1f}")
    print(f"Average mission duration: {average_duration:.2f}")

    print("Completed missions by type:")

    for mission_type in mission_breakdown:
        print(
            f"  {mission_type}: "
            f"{mission_breakdown[mission_type]}"
        )

    print(f"Active aircraft: {active_aircraft_count}")
    print(f"Aircraft in maintenance: {maintenance_aircraft_count}")


    # TODO: PART 5 - Build the report content
    pass

    # TODO: PART 6 - Write the report to file
    pass


# Main execution
if __name__ == '__main__':
    # TODO: Students will customize this to generate reports for different squadrons
    print("Generating squadron activity reports...")

    # Example: Generate report for VFA-41 (Black Aces)
    generate_squadron_report('VFA-41', '../reports/vfa-41-report.txt')
    print("Report generation complete.")
