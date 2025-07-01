import csv
import sqlite3

# Function to parse the CSV file and return data
def parse_csv_file(file_path):
    """Parse the CSV file and return a list of dictionaries (rows)."""
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)  # Uses DictReader to directly return data as a dictionary
        for row in reader:
            data.append(row)
    return data

# Function to insert the parsed data into an SQLite database
def insert_to_sqlite(data, db_name):
    """Insert parsed data into an SQLite database."""
    conn = sqlite3.connect(db_name)  # Connect to the SQLite database (creates if doesn't exist)
    cursor = conn.cursor()

    # Step 1: Drop the table if it exists to ensure we start fresh every time
    cursor.execute("DROP TABLE IF EXISTS legacy_data")

    # Step 2: Recreate the table in SQLite (this step ensures proper initialization)
    cursor.execute("""
        CREATE TABLE legacy_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            amount REAL
        )
    """)

    # Step 3: Insert new data into SQLite table
    for record in data:
        cursor.execute("""
            INSERT INTO legacy_data (category, amount)
            VALUES (?, ?)
        """, (record['category'], float(record['amount'])))

    conn.commit()  # Commit changes to the database
    cursor.close()  # Close the cursor
    conn.close()  # Close the database connection
    print("Data inserted into SQLite database.")

# Function to validate and output the data from SQLite
def validate_data_in_db(db_name):
    """Query and print all data from the SQLite database to validate insertion."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Query the data from the legacy_data table
    cursor.execute("SELECT * FROM legacy_data")

    # Fetch all rows
    rows = cursor.fetchall()

    # Print the rows for validation
    print("\nValidation: Database Contents")
    for row in rows:
        print(row)

    cursor.close()
    conn.close()

# Main function to run the entire process
def main():
    """Main function to run the entire process."""
    file_path = 'legacy_data.txt'  # Path to the legacy input file

    # Step 1: Read the raw legacy file data
    print("Raw Input File Data:")
    with open(file_path, 'r') as f:
        raw_data = f.read()  # Read the entire contents of the file
    print(raw_data)  # Print the raw data as it appears in the file

    # Step 2: Parse the legacy CSV data
    legacy_data = parse_csv_file(file_path)

    # Step 3: Insert the parsed data into SQLite database
    insert_to_sqlite(legacy_data, 'legacy_data.db')  # Save to SQLite file

    # Step 4: Validate and print the contents of the database
    validate_data_in_db('legacy_data.db')  # Validate data in SQLite

if __name__ == '__main__':
    main()  # Run the script
