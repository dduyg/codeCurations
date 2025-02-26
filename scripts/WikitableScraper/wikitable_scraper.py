import requests
from bs4 import BeautifulSoup
import csv

def scrape_wikipedia_table(url, save_csv=False, preview_rows=5):
    """
    Scrapes tables from a Wikipedia page, returns the headers and data as a list of dictionaries,
    and optionally saves the data as CSV files.

    Args:
        url (str): The URL of the Wikipedia page to scrape.
        save_csv (bool): If True, the function will save the extracted data as CSV files.
        preview_rows (int): Number of rows to preview in the output to give a quick overview.

    Returns:
        list: A list of dictionaries containing the table data. Each dictionary represents a row of data.
    """
    
    # Send HTTP request to the Wikipedia page and get the response
    response = requests.get(url)
    
    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all tables with the class 'wikitable' or 'wikitable sortable'
    tables = soup.find_all('table', {'class': 'wikitable'})

    # Check if any tables are found
    if not tables:
        print("No tables found on this page.")
        return []

    # Initialize a list to store all scraped data
    wiki_data = []

    # Process each table found on the page
    for table_index, table in enumerate(tables):
        # Extract headers (th) for the current table
        headers = [th.get_text(strip=True) for th in table.find_all('th')]

        # Display the header and other overview info
        print(f"\nScraping Table {table_index + 1}:")
        print("This table contains the following columns:\n")
        print(", ".join(headers))
        print("\nExtracting the data rows...\n")

        # Initialize a list to store the row data
        all_rows_data = []

        # Extract rows (tr) and their corresponding data (td)
        for row in table.find_all('tr')[1:]:  # Skip the header row
            columns = row.find_all('td')
            
            # Extract text from each column (td) in the row
            row_data = [column.get_text(strip=True) for column in columns]
            
            # Only add non-empty rows to the data list
            if row_data:
                all_rows_data.append(dict(zip(headers, row_data)))
        
        # Output a preview of the data (first few rows)
        total_rows = len(all_rows_data)
        if total_rows > 0:
            print(f"Successfully extracted {total_rows} data rows.\n")
            print("Preview of the first few rows:")
            for row in all_rows_data[:preview_rows]:
                print(row)
        else:
            print("No data rows found in the table.")

        # Add the current table data to the overall data list
        wiki_data.append(all_rows_data)

        # Save the data to CSV if save_csv is True
        if save_csv:
            # Define the CSV filename
            filename = f"table_{table_index + 1}.csv"

            # Write the extracted data to a CSV file
            with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=headers)
                writer.writeheader()
                writer.writerows(all_rows_data)
            print(f"Table {table_index + 1} saved as {filename}.")

    # Return the data as a list of dictionaries
    return wiki_data


# ===================================================================================
# Example usage: Scraping from the Wikipedia page for population density
# ===================================================================================

# URL of the Wikipedia page you want to scrape
url = "https://en.wikipedia.org/wiki/List_of_cities_by_population_density"

# Call the function to scrape the table data from the specified URL and save the data as CSV
wiki_data = scrape_wikipedia_table(url, save_csv=True, preview_rows=5)

# The variable 'wiki_data' now contains the extracted data, which can be further processed or saved
