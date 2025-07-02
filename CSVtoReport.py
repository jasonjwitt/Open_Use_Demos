import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def parse_legacy_file(file_path):
    data = []
    with open(file_path, 'r') as f:
        reader = pd.read_csv(f)
        data.append(reader)
    return data

def generate_visualization(aggregated_data):
    """Generate a bar chart and save it to a file."""
    # Create a bar plot
    plt.figure(figsize=(10,6))
    sns.barplot(x='date', y='amount', hue='category', data=aggregated_data)
    plt.title('Sales and Refunds Over Time')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    
    # Save the plot to a file (instead of showing it)
    plot_filename = 'sales_refunds_plot.png'
    plt.savefig(plot_filename)
    print(f'Visualization saved as {plot_filename}.')
    plt.close()  # Close the plot to avoid display

def generate_report(aggregated_data):
    """Generate the text report."""
    report_filename = 'report.txt'
    with open(report_filename, 'w') as report_file:
        report_file.write(f"Aggregated Data:\n")
        aggregated_data.to_string(report_file)
    
    print(f'Report saved as {report_filename}.')

def main():
    input_file = 'legacy_data.csv'  # Path to the input CSV file

    # Step 1: Read legacy file
    print("Raw Input File Data:")
    with open(input_file, 'r') as f:
        raw_data = f.read()  # Read raw file contents
    print(raw_data)  # Print raw data as it appears in the file

    # Step 2: Parse legacy file and transform data
    legacy_data = pd.read_csv(input_file)  # Read CSV into DataFrame
    print("\nData loaded into DataFrame.")

    # Step 3: Aggregating data
    aggregated_data = legacy_data.groupby(['date', 'category']).agg({'amount': 'sum'}).reset_index()
    print("\nAggregated Data:")
    print(aggregated_data)

    # Step 4: Generate visualization and save to file
    generate_visualization(aggregated_data)

    # Step 5: Generate text report
    generate_report(aggregated_data)

if __name__ == "__main__":
    main()
