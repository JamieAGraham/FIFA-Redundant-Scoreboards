import pandas as pd
import json

def process_country_codes(input_path, json_output_path, csv_output_path):
    # Read the file and preprocess the lines
    with open(input_path, 'r') as file:
        raw_data = [line.strip() for line in file.readlines() if line.strip()]
    
    # Initialize variables for parsing
    current_region = None
    current_section = None
    parsed_data = []
    old_sections = ["Old FIFA/IOC Codes", "Old Names of Countries/Independent States"]

    # Parse the text data
    for line in raw_data:
        # Detect regions or special sections
        if line in ["Africa", "Asia", "Europe", "North America", "Oceania", "South America"]:
            current_region = line
            current_section = None
        elif line in old_sections:
            current_section = line
            current_region = None
        elif "\t" in line:
            # Parse the country data
            parts = [p.strip() for p in line.split("\t") if p.strip()]
            if len(parts) == 3:
                country, fifa, ioc = parts
                parsed_data.append({
                    'Country': country,
                    'FIFA': fifa,
                    'IOC': ioc,
                    'Region': current_region,
                    'Section': current_section
                })

    # Create a DataFrame from the parsed data
    df = pd.DataFrame(parsed_data)

    # Create the final dictionary
    final_result = (
        df.groupby('Country')
        .apply(lambda group: {
            'FIFA': group.iloc[0]['FIFA'],
            'IOC': group.iloc[0]['IOC'],
            'Region': group.iloc[0]['Region'],
            'Active': group.iloc[0]['Section'] is None
        })
        .to_dict()
    )

    # Save the dictionary as a JSON file
    with open(json_output_path, 'w') as json_file:
        json.dump(final_result, json_file, indent=4)

    # Save the DataFrame as a CSV file
    df_csv = pd.DataFrame.from_dict(final_result, orient='index').reset_index()
    df_csv.rename(columns={'index': 'Country'}, inplace=True)
    df_csv.to_csv(csv_output_path, index=False)

# Define file paths
input_file_path = 'TLAs.txt'  # Input text file path
json_output_file_path = 'country_codes_confirm.json'  # JSON output file path
csv_output_file_path = 'country_codes_confirm.csv'  # CSV output file path

# Process the file and generate outputs
process_country_codes(input_file_path, json_output_file_path, csv_output_file_path)
