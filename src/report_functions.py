"""
Report Generation Functions for Flight Operations

This module contains functions for reading, processing, and reporting on
military flight operations data. Students will implement these functions
to practice file I/O, data manipulation, and report generation.
"""

import csv
from pathlib import Path

def read_csv_file(filepath):
    """
    Reads a CSV file and returns the data as a list of dictionaries.
    """
    # TODO: Your code here
    # Hint: Use csv.DictReader to read CSV files into dictionaries
    # Hint: Remember to use 'with open()' for proper file handling
    with open(filepath, mode="r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def count_records(data_list):
    """Counts the number of records in a dataset."""
    # TODO: Your code here
    # Hint: Use the len() function
    return len(data_list)


def get_unique_values(data_list, field_name):
    """Gets all unique values for a specific field in the dataset."""
    # TODO: Your code here
    # Hint: Use a set to collect unique values
    # Hint: Convert the set to a list and sort it before returning
    unique_values = set()

    for record in data_list:
        value = record[field_name]
        unique_values.add(value)

    sorted_values = sorted(unique_values)

    return sorted_values


def filter_by_field(data_list, field_name, field_value):
    """Filters records where a specific field matches a given value."""
    # TODO: Your code here
    # Hint: Use a list comprehension to filter or a loop!
    # see here for more info: https://docs.python.org/3.13/tutorial/datastructures.html#list-comprehensions
    return [
        record for record in data_list
        if record[field_name] == field_value
    ]


def calculate_total(data_list, field_name):
    """Calculates the sum of a numeric field across all records."""
    # TODO: Your code here
    # Hint: Initialize a total variable to 0
    # Hint: Loop through each record and add float(record[field_name]) to total
    # Hint: Remember to convert string values to float!
    return sum(float(record[field_name]) for record in data_list)


def calculate_average(data_list, field_name):
    """Calculates the average value of a numeric field."""
    # TODO: Your code here
    # Hint: Use calculate_total() and count_records() functions
    # Hint: Average = total / count
    if not data_list:
        return 0.0

    return calculate_total(data_list, field_name) / count_records(data_list)


def find_record_by_id(data_list, id_field, id_value):
    """Finds a specific record by its ID field."""
    # TODO: Your code here
    # Hint: Loop through data_list
    # Hint: Return the record when record[id_field] == id_value
    for record in data_list:
        if record[id_field] == id_value:
            return record

    return None


def join_data(primary_list, secondary_list, primary_key, foreign_key):
    """
    Joins two datasets together based on matching key fields.
    Similar to a SQL JOIN.
    """
    # TODO: Your code here
    # Hint: Create a dictionary mapping secondary_list IDs to records
    # Hint: For each record in primary_list, look up the matching secondary record
    # Hint: Use dict.update() to merge dictionaries
    secondary_by_key = {}

    for secondary_record in secondary_list:
        key_value = secondary_record[foreign_key]
        secondary_by_key[key_value] = secondary_record

    joined_records = []

    for primary_record in primary_list:
        key_value = primary_record[primary_key]

        joined_record = primary_record.copy()

        if key_value in secondary_by_key:
            matching_record = secondary_by_key[key_value]

            joined_record.update(matching_record)

        joined_records.append(joined_record)

    return joined_records


def write_report_to_file(filepath, content):
    """Writes a text report to a file."""
    # TODO: Your code here
    # Hint: Use 'with open(filepath, 'w')' to open file for writing
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)

    with open(filepath, mode="w", encoding="utf-8") as file:
        file.write(content)


def format_header(title):
    """Creates a formatted header for reports."""
    # TODO: Your code here
    # Hint: Use "=" * 60 to create a line of equals signs
    # Hint: Use .center(60) to center the title
    line = "=" * 60
    return f"{line}\n{title.center(60)}\n{line}"


# Testing functions
if __name__ == '__main__':
    from pathlib import Path
    print("Testing report functions...")
    print("Implement functions above, then uncomment test code below")

    # # Test read_csv_file
    pilots = read_csv_file('../data/pilots.csv')
    aircraft = read_csv_file('../data/aircraft.csv')
    flights = read_csv_file('../data/flight_logs.csv')
    print(f"Loaded {len(pilots)} pilots")
    print(f"Loaded {len(aircraft)} aircraft")
    print(f"loaded {len(flights)} flights")
    print()
    # # Test count_records
    pilot_count = count_records(pilots)
    print(f"Pilot count: {pilot_count}")
    # Test get_unique_values
    mission_types = get_unique_values(flights, 'mission_type')
    print(f"Mission types: {mission_types}")
    print()