import csv
import requests
import json

# Function to parse the legacy CSV file
def parse_legacy_file(file_path):
    """
    Parses the legacy CSV file and returns the data as a list of dictionaries.
    
    Args:
        file_path (str): The path to the CSV file.
        
    Returns:
        list: A list of dictionaries representing the rows in the CSV file.
    """
    data = []  # Initialize an empty list to store the parsed data
    
    # Open the CSV file and read it
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)  # Use csv.DictReader to read the CSV as dictionaries
        for row in reader:
            data.append(row)  # Append each row (as a dictionary) to the data list
    
    return data  # Return the list of dictionaries (data)

# Main function to execute the file processing
def main():
    """
    Main function to read the legacy file, transform the data, and send it to an API.
    
    Steps:
    1. Read raw input file.
    2. Parse the file into structured data.
    3. Transform the data into API-friendly format.
    4. Send the data to a public API and print the response.
    """
    # Step 1: Read legacy file
    print("Raw Input File Data:")
    with open(INPUT_FILE, 'r') as f:
        raw_data = f.read()  # Read the entire contents of the legacy file
    print(raw_data)  # Print the raw data as it appears in the file

    # Step 2: Parse legacy file and transform data
    legacy_data = parse_legacy_file(INPUT_FILE)  # Parse the legacy file into structured data
    print("\nFormatted API Request Data:")

    # Transform the data into a format suitable for the API (list of dictionaries)
    transformed_data = [
        {
            "category": row["category"],  # The 'category' field from the CSV
            "amount": float(row["amount"])  # The 'amount' field from the CSV, converted to float
        }
        for row in legacy_data
    ]
    
    # Print the transformed data
    print(json.dumps(transformed_data, indent=4))  # Print the formatted data for the API

    # Step 3: Send the data to the API
    API_URL = "https://httpbin.org/post"  # The API endpoint to send data to
    
    # Make the POST request with the transformed data
    response = requests.post(API_URL, json=transformed_data)  # Send data as JSON
    
    # Check if the request was successful and print the response
    if response.status_code == 200:
        print("\nData successfully sent to API.")
    else:
        print(f"\nError sending data: {response.status_code}")
    
    # Print the full response from the API for review
    print("\nAPI Response:")
    print(response.json())  # Print the API response as JSON

# Run the script if it's executed as a standalone program
if __name__ == '__main__':
    INPUT_FILE = 'legacy_data.txt'  # Path to the input file (can be customized)
    main()  # Call the main function to execute the script
