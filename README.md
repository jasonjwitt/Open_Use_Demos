
# CSV to API Transformation Demo

This repository contains a Python script that demonstrates transforming a legacy CSV file into a format suitable for a modern API. The transformation process involves reading raw CSV data, validating the input, and formatting it into a JSON structure before sending it to a public API endpoint.

## Features Demonstrated in This Demo:
- Basic configuration loader
- Basic parsing of CSV files (delimiter-separated)
- Header/trailer validation
- Data transformation into a structured format
- Sending data to an API using a POST request
- Text-based reporting of the transformation process

## Why a Custom Solution Instead of Pandas?

When modernizing legacy systems, flexibility is key. While Python offers high-level libraries like **Pandas** that could simplify transforming CSV files into APIs, a custom solution was chosen in this case for the following reasons:

1. **Addressing Legacy-Specific Needs**:  
   Legacy systems often work with **unstructured or non-standard data**. Custom code ensures precise handling of files with complex structures (e.g., fixed-width or inconsistent delimiters), which might be more challenging to parse using a higher-level library like Pandas.

2. **Fine-Tuned Control Over Transformation**:  
   A custom solution gives us complete control over how data is processed, including **field validation**, **header/trailer checks**, and **data sanitization**. Pandas is excellent for structured data, but doesn't provide the same flexibility for legacy-specific issues.

3. **Lightweight and Performance-Focused**:  
   For **smaller datasets** or **specific legacy formats**, a **custom solution** is more efficient. While Pandas is powerful, it can introduce unnecessary overhead for smaller tasks. A simple script ensures fast, **memory-efficient processing** for tasks like this, where only a specific transformation is needed.

4. **Maintainability and Long-Term Control**:  
   A custom solution offers greater maintainability because the logic is **directly understood** and easy to modify when the business or system requirements evolve. Using external libraries like Pandas could introduce risks with **future updates** that break backward compatibility, making it harder to maintain in the long term.

## How It Works:
The script takes a **CSV file** as input and reads the data line by line. It performs basic validation and transformation on the data, ensuring that each record is correctly structured and that the appropriate fields are present.

### Script Flow:
1. **Input File**: The script takes in a CSV file with a header and trailer structure, and performs necessary transformations.
2. **Normalize (CSV to JSON)**: The data is parsed and transformed into a JSON structure that is suitable for API consumption.
3. **Validate Header & Trailer**: The header and trailer of the file are validated to ensure proper format.
4. **Summarize Data**: The script calculates values (e.g., sums) for each category of data.
5. **Generate Report**: A text-based report is generated, summarizing the key transformations and outputs.
6. **API Request**: The transformed data is sent to an API endpoint using a POST request.

## Files
| File                        | Purpose                                        |
| --------------------------  | ---------------------------------------------  |
| `CSVtoAPI.py`               | Main demo script for CSV to API transformation |
| `legacy_data.txt`           | Sample input CSV file for testing              |
| `README.md`                 | Documentation for using the demo               |
| expected_output.txt         | Expected output when run with given input file |

## How to Use:
To run the script, use the following command:

```bash
python CSVtoAPI.py
```

Ensure that the **input file** (e.g., `legacy_data.txt`) is in the same directory as the script or specify its full path.

## Example Output:
```bash
Raw Input File Data:
category,amount
Sales,5320.00
Refunds,140.50
Sales,2785.00
Refunds,55.25

Formatted API Request Data:
[
    {
        "category": "Sales",
        "amount": 5320.0
    },
    {
        "category": "Refunds",
        "amount": 140.5
    },
    {
        "category": "Sales",
        "amount": 2785.0
    },
    {
        "category": "Refunds",
        "amount": 55.25
    }
]
Data successfully sent to API.

API Response:
{'args': {}, 'data': '[{"category": "Sales", "amount": 5320.0}, {"category": "Refunds", "amount": 140.5}, {"category": "Sales", "amount": 2785.0}, {"category": "Refunds", "amount": 55.25}]', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '166', 'Content-Type': 'application/json', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.32.4', 'X-Amzn-Trace-Id': 'Root=1-685fe81e-50d8352b78220a8d3b968010'}, 'json': [{'amount': 5320.0, 'category': ...
```

## Why This Version is Limited:
This demo showcases the basic transformation functionality, but certain features are omitted for simplicity, such as:
- Full error handling
- Configuration management for multiple input formats
- Enhanced file parsing logic for more complex file types
- API authentication or security

For full functionality, dynamic configuration support, and advanced error handling, please reach out via my [Upwork profile](https://www.upwork.com/freelancers/~01c786da236de4a7ee?mp_source=share).

## License:
MIT License — See LICENSE file for details.
