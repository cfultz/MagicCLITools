import requests
from bs4 import BeautifulSoup
import csv
import sys

def scrape_scryfall_checklist(set_code):
  """
  Scrapes a Scryfall checklist page and saves the card names and numbers 
  to a CSV file in alphabetical order, using the provided set code.

  Args:
    set_code: The three-letter set code (e.g., 'afr').
  """

  url = f'https://scryfall.com/sets/{set_code}?as=checklist'
  filename = f'{set_code}_checklist.csv'  # Changed file name format

  response = requests.get(url)
  response.raise_for_status()

  soup = BeautifulSoup(response.content, 'html.parser')
  card_rows = soup.find_all('tr', {'data-component': "card-tooltip"})

  card_data = []
  for row in card_rows:
    # Initialize variables with default values
    count = ''  # You'll need to add logic for the checkbox later
    name = ''
    edition = ''
    condition = 'NM'  # Set condition to 'NM' for all cards
    language = 'en'  # Set language to 'en' for all cards
    foil = 'No'  # Default to 'No' unless foil information is found
    collector_number = ''
    purchase_price = ''  # You'll need to add logic for purchase price later

    # Extract collector number
    number_link = row.find('td', class_='right').find('a')
    if number_link:
      collector_number = number_link.text.strip()

    # Extract name
    name_link = row.find('td', class_='ellipsis').find('a')
    if name_link:
      name = name_link.text.strip()

    # Extract edition (set name)
    set_link = row.find('td').find('a')
    if set_link:
      edition = set_link.text.strip()

    # Check for foil (you'll need to adjust this based on Scryfall's HTML)
    # if row.find('td', class_='foil-card'):  # Example
    #   foil = 'Yes'

    card_data.append([count, name, edition, condition, language, foil, collector_number, purchase_price])

  # Sort card data alphabetically by name
  card_data.sort(key=lambda x: x[1])

  with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Count', 'Name', 'Edition', 'Condition', 'Language', 'Foil', 'Collector Number', 'Purchase Price'])
    writer.writerows(card_data)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    set_code = sys.argv[1]
    scrape_scryfall_checklist(set_code)
  else:
    print("Error: Please provide a set code (e.g., python main.py afr)")