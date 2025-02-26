## `wikitable_scraper.py`
_This Python script scrapes tables from Wikipedia pages, extracts the table headers and data, and optionally saves the extracted data to CSV files. It utilizes the `requests` library for making HTTP requests and `BeautifulSoup` from `bs4` for parsing HTML._

## Features
- Scrapes tables with the class `wikitable` or `wikitable sortable` from any Wikipedia page.
- Prints an overview of the headers and the data rows for each table scraped.
- Allows you to save the extracted data as CSV files.
- Returns the scraped data as a list of dictionaries for further processing.

## Requirements
Before running the script, you need to install the necessary Python libraries. You can install them using `pip`:
```bash
pip install requests beautifulsoup4
```

## How to Use

### 1. Clone or Download the Script
Download or clone the script into your local machine.

### 2. Modify the URL
In the script, modify the `url` variable to the URL of the Wikipedia page from which you want to scrape tables. For example:
```python
url = "https://en.wikipedia.org/wiki/List_of_cities_by_population_density"
```

### 3. Call the `scrape_wikipedia_table` function
The `scrape_wikipedia_table` function accepts the following parameters:
- `url` (str): The URL of the Wikipedia page to scrape.
- `save_csv` (bool): If `True`, the function will save the extracted data as CSV files. By default, it is set to `False`.

To scrape a Wikipedia page and save the tables to CSV files:
```python
wiki_data = scrape_wikipedia_table(url, save_csv=True)
```

If you don’t want to save the data to CSV, you can set `save_csv` to `False`:
```python
wiki_data = scrape_wikipedia_table(url, save_csv=False)
```

## Output
The script will print an overview of each table, including the headers and the number of data rows extracted. It will also display the data row dictionaries in the console.

If `save_csv=True`, the script will save each table as a CSV file. Each table will be saved in a separate CSV file named `table_1.csv`, `table_2.csv`, etc.

The `wiki_data` variable will hold the scraped data as a list of dictionaries. Each dictionary corresponds to a row in the table with keys as the column headers.

## <samp>Example Output</samp>
If the script successfully scrapes the data, you will see something like this in the console:

```
Scraping Table 1:
This table contains the following columns:
City, Population, Area, Density, Country, Year, km2, mi2, /km2, /mi2

Extracting the data rows...

Successfully extracted 95 data rows.
{'City': 'Croix-Daurade', 'Population': '148,163', 'Area': '53.16', 'Density': '2,785', 'Country': 'France', 'Year': '2017', 'km2': '53.16', 'mi2': '20.5', '/km2': '2,785', '/mi2': '7,222'}

Table 1 saved as table_1.csv.
```

If no tables are found on the page:

```
No tables found on this page.
```

## Author
[DUYGU DAĞDELEN]
