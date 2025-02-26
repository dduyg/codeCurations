import requests
from bs4 import BeautifulSoup

def scrape_wikipedia_table(url):
    """
    Scrapes tables from a Wikipedia page and prints the headers and data.

    Args:
        url (str): The URL of the Wikipedia page to scrape.

    Returns:
        None
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
        return

    # Process each table found on the page
    for table_index, table in enumerate(tables):
        # Extract headers (th) for the current table
        headers = [th.get_text(strip=True) for th in table.find_all('th')]

        # Display the header
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
        
        # Output the data in a readable format
        if all_rows_data:
            print(f"Successfully extracted {len(all_rows_data)} data rows.\n")
            for row in all_rows_data:
                print(row)
        else:
            print("No data rows found in the table.")

# Example usage: Scraping from the Wikipedia page for population density
url = "https://en.wikipedia.org/wiki/List_of_cities_by_population_density"
scrape_wikipedia_table(url)
