# Inventory

`cli_cards.py` Help Section

```
Add one or more Magic: The Gathering cards to a CSV file.

positional arguments:
  csv_path              The path to the CSV file where the card data will be stored. If the file does not exist, it will be created.

options:
  -h, --help            show this help message and exit
  --card Card_Name Set_Code Collector_Number Quantity Foil
                        Add a card to the CSV file. Each card entry should be specified in the following format: Card_Name Set_Code Collector_Number Quantity Foil. Foil should be 'True' or 'False' indicating if the card is foil or not.
                        This option can be used multiple times to add multiple cards in one command.
```

`interactive_cards.py` Input Example
```
Enter the path to the CSV file: cards.csv
Enter the card name (or type 'exit' to quit): Evercoat Ursine
Enter the set code: blc
Enter the collector number: 64
Enter the quantity: 1
Is this card a foil? (yes/no): no
Added 1x Evercoat Ursine from set blc with collector number 64 (Foil: False) to cards.csv.
CSV file sorted by Set Code and Collector Number.
Enter the card name (or type 'exit' to quit):
```