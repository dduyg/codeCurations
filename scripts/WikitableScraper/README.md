## `wikiTable_scraper.py`
_This Python script scrapes tables from Wikipedia pages, extracts the table headers and data, and optionally saves the extracted data as CSV files. It utilizes the `requests` library for making HTTP requests and `BeautifulSoup` from bs4 for parsing HTML._

### Features
✅ Scrapes tables with the class `wikitable` or `wikitable sortable` from any Wikipedia page.

✅ Prints an overview of the headers and the data rows for each table scraped.

✅ Returns the scraped data as a list of dictionaries for further processing.

✅ Optionally saves the extracted data as CSV files.

## Requirements
Before running the script, install the required Python libraries using `pip`:
```bash
pip install requests beautifulsoup4
```

## How to Use
### 1️⃣ Clone or Download the Script
Download or clone the script onto your local machine.

### 2️⃣ Modify the URL
In the script, set the `url` variable to the Wikipedia page you want to scrape. Example:
```python
url = "https://en.wikipedia.org/wiki/List_of_cities_by_population_density"
```

### 3️⃣ Call the `scrape_wikipedia_table` Function
The function supports the following parameters:
- `url` (**str**): The Wikipedia page URL to scrape.
- `save_csv` (**bool**, default=`False`): If `True`, saves the data as CSV files.
- `preview_rows` (**int**, default=`5`): Number of rows to preview in the console.

To scrape a Wikipedia page and preview the first 5 rows per table:
```python
wiki_data = scrape_wikipedia_table(url)
```

To scrape and save each table as a CSV file:
```python
wiki_data = scrape_wikipedia_table(url, save_csv=True)
```


## Output
The script will print an **overview** of each table, including the headers and the number of data rows extracted. It will also display a preview of the first few rows in the console.

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

Preview of the first 5 rows:
{'City': 'Croix', 'Population': '21,117', 'Area': '1.44', 'Density': '14,670', 'Country': 'France', 'Year': '2017'}
{'City': 'Paris', 'Population': '2,165,423', 'Area': '105.4', 'Density': '20,609', 'Country': 'France', 'Year': '2020'}
...

Table 1 saved as table_1.csv.
```

If **no tables** are found:
```
No tables found on this page.
```
