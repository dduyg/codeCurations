## `wikiTable_scraper.py`
*This Python script scrapes tables from Wikipedia pages, extracts the table headers and data, provides an overview of the extracted information, and optionally saves the data as CSV files. It utilizes the `requests` library for making HTTP requests and `BeautifulSoup` from `bs4` for parsing HTML.*

## Features

✅ Scrapes tables with the class `wikitable` or `wikitable sortable` from any Wikipedia page.

✅ Prints an **overview** of each table, including column headers and a preview of the first few rows.

✅ Returns the **full scraped data** as a list of dictionaries for further processing.

✅ **Optionally saves** the extracted data as CSV files.

## Requirements

Before running the script, install the required Python libraries using `pip`:

```bash
pip install requests beautifulsoup4
```

## How to Use

### 1️⃣ **Clone or Download the Script**

Download or clone the script onto your local machine.

### 2️⃣ **Modify the URL**

In the script, set the `url` variable to the Wikipedia page you want to scrape.

Example:

```python
url = "https://en.wikipedia.org/wiki/List_of_cities_by_population_density"
```

### 3️⃣ **Call the `scrape_wikipedia_table` Function**

The function supports the following parameters:

- `url` (**str**): The Wikipedia page URL to scrape.
- `save_csv` (**bool**, default=`False`): If `True`, saves the data as CSV files.
- `preview_rows` (**int**, default=`5`): Number of rows to preview in the console.

### **Basic Usage:**

To scrape a Wikipedia page and preview the first 5 rows per table:

```python
wiki_data = scrape_wikipedia_table(url)
```

### **Save Data as CSV:**

To scrape and save each table as a CSV file:

```python
wiki_data = scrape_wikipedia_table(url, save_csv=True)
```

### **Customize the Preview Size:**

To show only the first 3 rows instead of 5:

```python
wiki_data = scrape_wikipedia_table(url, preview_rows=3)
```

## Output

### **Console Overview:**

The script prints an **overview** of each table, including headers and a **preview** of the first few rows.

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

### **CSV File Output (if enabled)**

If `save_csv=True`, each table is saved as a CSV file (`table_1.csv`, `table_2.csv`, etc.), structured with the column headers.

## **Returned Data Format**

The function returns **all scraped data** as a list of dictionaries, even if only a preview is printed.

Example:

```python
[
    {"City": "Paris", "Population": "2,165,423", "Area": "105.4", "Density": "20,609", "Country": "France", "Year": "2020"},
    {"City": "Manila", "Population": "1,846,600", "Area": "42.88", "Density": "43,079", "Country": "Philippines", "Year": "2020"},
    ...
]
```
