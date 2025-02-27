import requests
from bs4 import BeautifulSoup
import csv

def scrape_wikipedia_table(url, save_csv=False, preview_rows=5):
    """
    Scrapes tables from a Wikipedia page, correctly handling multi-level column headers,
    returning as a list of dictionaries, and optionally saves the data as CSV files.

    Args:
        url (str): The URL of the Wikipedia page to scrape.
        save_csv (bool): If True, the function will save the extracted data as CSV files. Default is False.
        preview_rows (int): Number of rows to preview in the output. Default is 5.

    Returns:
        list: A list of dictionaries containing the extracted table data.
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
        # Extract headers
        headers = []
        header_rows = table.find_all('tr')

        # Process the first row of headers
        for th in header_rows[0].find_all('th'):
            col_span = int(th.get('colspan', 1))
            text = th.get_text(strip=True)

            if col_span > 1:
                headers.extend([f"{text} ({i + 1})" for i in range(col_span)])
            else:
                headers.append(text)

        # If there's a second row of headers, process it
        if len(header_rows) > 1:
            sub_headers = [th.get_text(strip=True) for th in header_rows[1].find_all('th')]
            grouped_headers = []
            i = 0

            for header in headers:
                if "(" in header:  # If it's a merged column header
                    grouped_headers.append(f"{header.split(' ')[0]} {sub_headers[i]}")
                    i += 1
                else:
                    grouped_headers.append(header)
            headers = grouped_headers

        # Extract table rows
        all_rows_data = []
        for row in table.find_all('tr')[2:]:  # Skip header rows
            columns = row.find_all('td')
            row_data = [col.get_text(strip=True) for col in columns]

            if row_data:
                all_rows_data.append(dict(zip(headers, row_data)))

        # Print overview
        print(f"\nScraping Table {table_index + 1}:")
        print("This table contains the following columns:\n")
        print(", ".join(headers))
        print("\nExtracting the data rows...\n")
        print(f"Successfully extracted {len(all_rows_data)} data rows.")

        # Show preview of first few rows
        print("\nPreview of the first few rows:")
        for row in all_rows_data[:preview_rows]:
            print(row)

        # Add the current table data to the overall data list
        wiki_data.append(all_rows_data)

        # Save to CSV if requested
        if save_csv:
            # Define the CSV filename
            filename = f"table_{table_index + 1}.csv"

            # Write the extracted data to a CSV file
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writeheader()
                writer.writerows(all_rows_data)
            print(f"\nTable {table_index + 1} saved as {filename}.")

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
