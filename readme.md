# CSV to SQLite Demo

This repository contains a Python-based demonstration of transforming legacy CSV file data into a relational database format (SQLite). The demo illustrates a simple process of reading data from a CSV file, inserting that data into an SQLite database, and performing basic validation.

## 🚀 Overview

The purpose of this script is to demonstrate how a legacy CSV file can be processed, transformed, and inserted into an SQLite database. While there are many tools and libraries available for similar tasks, this demo focuses on custom code to illustrate how you can achieve the same goal without relying on heavy libraries.

### 🗂️ Files
- `CSVtoSQLite.py`: The main Python script responsible for reading the CSV file, transforming the data, and inserting it into an SQLite database.
- `legacy_data.txt`: A sample input CSV file with legacy data that will be transformed into the database.
- `expected_output.txt`: A sample output file that demonstrates the expected format of the database contents after transformation. This file can be used for comparison to verify successful data insertion.
- `requirements.txt`: Lists the required Python dependencies for the project (currently only `requests`).

## 🔧 How It Works

1. **Read the Legacy File**: The script starts by reading a CSV file that contains legacy data.
2. **Parse the Data**: It then parses the CSV file, extracting the data in a structured format.
3. **Insert Data into SQLite**: The script then inserts the parsed data into an SQLite database. Each data row is saved with a category and an associated amount.
4. **Validation**: After inserting the data, the script prints out the contents of the SQLite database to validate that the data was properly inserted.

### 🎯 Features Demonstrated
- **CSV Parsing**: Reads a CSV file and structures the data for insertion.
- **SQLite Database Interaction**: Creates a new SQLite database or uses an existing one, inserting the parsed data.
- **Validation**: Displays the contents of the SQLite database to confirm successful insertion.

## 📝 Why Custom Code?

While Python offers robust libraries like `pandas` to make tasks like transforming CSV data easier, we opted to use a more **custom approach** to demonstrate flexibility and understanding of the underlying process. Here are the reasons:

1. **Fine-grained Control**: By writing custom code, we can fine-tune the process for legacy systems, ensuring we handle each step as needed without relying on the abstraction provided by larger libraries like `pandas`.
2. **Long-Term Scalability**: Using custom code allows us to better handle future system complexities, particularly in legacy systems that may need highly tailored solutions. Pandas, while powerful, has limitations when it comes to scalability and may introduce unnecessary overhead.
3. **Transparency**: Custom solutions make it easier to explain each transformation step, making the process more transparent for stakeholders who may be unfamiliar with high-level libraries.
4. **Simplicity**: For smaller scripts like this one, custom code is often more straightforward and lightweight than using an external library that adds complexity and dependencies.

## 🗄️ Why SQLite?

For the purposes of this demo, **SQLite** was chosen due to the following reasons:

1. **Simplicity**: SQLite is a **serverless** database, meaning it doesn't require a separate server or complex setup. It's ideal for small to medium-sized demos and provides a straightforward way to work with relational data without the overhead of setting up a server.
2. **Portability**: SQLite databases are stored in a single file, making it easy to move or back up the database. This is particularly useful for small-scale projects and demos.
3. **No Need for Setup**: Unlike **MongoDB** or **PostgreSQL**, which require installation and setup of a database server, SQLite is embedded directly into the Python script, meaning it’s easier to run and manage for a demo or small project.
4. **Focus on Transformation**: The goal of this demo is to showcase the transformation process. Using SQLite allows us to focus on the core functionality of transforming and inserting data, without complicating the example with server-side management or cloud infrastructure.

### ❓ Why Not MongoDB or PostgreSQL?
While **MongoDB** and **PostgreSQL** are powerful databases used in production environments, they introduce more complexity in terms of setup, management, and performance optimization. This demo is focused on the transformation from legacy CSV data to a database, and using SQLite allows us to keep the process simple and focused.

- **MongoDB**: It would be suitable for a NoSQL database, but it's more commonly used for unstructured data, which doesn't fit this use case of structured tabular data.
- **PostgreSQL**: While ideal for larger applications that require relational integrity and complex querying, PostgreSQL would introduce unnecessary overhead for this simple transformation demo.

## 📦 Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/CSVtoSQLite_Demo.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the script:
    ```bash
    python CSVtoSQLite.py
    ```

## ⚠️ Limitations
- This is a simplified demo meant to showcase the basic transformation of legacy CSV data into an SQLite database. For full-scale solutions, more advanced features (e.g., error handling, data validation, multi-file support) would need to be incorporated.

## 🔍 Expected Output

After running the script, the SQLite database is populated with the contents of the CSV file. You can validate the output by comparing the database contents with the `expected_output.txt` file, which contains the expected format and values of the database.

```text
Raw Input File Data:
category,amount
Sales,5320.00
Refunds,140.50
Sales,2785.00
Refunds,55.25

Data inserted into SQLite database.

Validation: Database Contents
(1, 'Sales', 5320.0)
(2, 'Refunds', 140.5)
(3, 'Sales', 2785.0)
(4, 'Refunds', 55.25)

License:
MIT License — See LICENSE file for details.
