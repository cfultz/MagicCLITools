# Scryfall Checklist Scraper

This Python script scrapes card data from a Scryfall checklist page and saves it to a CSV file. The output is formatted for easy import into a spreadsheet application.

## Requirements

- Python 3.6 or higher
- `requests` library
- `beautifulsoup4` library

## Installation

1. Make sure you have Python installed.
2. Install the required libraries using `pip`:

```bash
pip install requests beautifulsoup4
```

## Usage

Save the script as a Python file (e.g., scryfall_scraper.py).

Run the script from your terminal, providing the three-letter Scryfall set code as a command-line argument:

```bash
python scryfall_scraper.py afr 
```

Use code with caution.

Replace afr with the desired set code (e.g., neo for Kamigawa: Neon Dynasty).

This will create a CSV file named {set_code}_checklist.csv (e.g., afr_checklist.csv) in the same directory as the script.
CSV File Format

The CSV file will contain the following columns:

* Count: (Empty for user input)
* Name: Card name
* Edition: Set name
* Condition: NM (Near Mint)
* Language: en (English)
* Foil: No (Unless detected as foil)
* Collector Number: Card's collector number in the set
* Purchase Price: (Empty for user input)

```bash
python scryfall_scraper.py neo
```

Use code with caution.

This will create a file named neo_checklist.csv with the card data from the Kamigawa: Neon Dynasty set.
Note

The script relies on the HTML structure of the Scryfall checklist page. If Scryfall changes its website structure, the script might need to be updated.
