import csv
import os
import argparse

# Function to append a card entry to the CSV file
def add_card_to_csv(csv_path, card_name, set_code, collector_number, quantity, foil):
    file_exists = os.path.isfile(csv_path)
    
    with open(csv_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write header if the file doesn't exist
        if not file_exists:
            writer.writerow(['Card Name', 'Set Code', 'Collector Number', 'Quantity', 'Foil'])
        
        # Append the card data
        writer.writerow([card_name, set_code, collector_number, quantity, foil])
    
    print(f"Added {quantity}x {card_name} from set {set_code} with collector number {collector_number} (Foil: {foil}) to {csv_path}.")

# Function to parse and add multiple cards
def add_multiple_cards(csv_path, card_entries):
    for entry in card_entries:
        card_name, set_code, collector_number, quantity, foil = entry
        add_card_to_csv(csv_path, card_name, set_code, collector_number, quantity, foil)

# Main function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description="Add one or more Magic: The Gathering cards to a CSV file.")
    
    parser.add_argument('csv_path', 
                        help="The path to the CSV file where the card data will be stored. If the file does not exist, it will be created.")
    
    # Allow multiple --card entries
    parser.add_argument('--card', 
                        action='append', 
                        nargs=5, 
                        metavar=('Card_Name', 'Set_Code', 'Collector_Number', 'Quantity', 'Foil'),
                        help=("Add a card to the CSV file. "
                              "Each card entry should be specified in the following format: "
                              "Card_Name Set_Code Collector_Number Quantity Foil. "
                              "Foil should be 'True' or 'False' indicating if the card is foil or not. "
                              "This option can be used multiple times to add multiple cards in one command."))

    args = parser.parse_args()

    if args.card:
        card_entries = []
        for card in args.card:
            card_name, set_code, collector_number, quantity, foil = card
            quantity = int(quantity)
            foil = foil.lower() == 'true'  # Convert the foil input to a boolean
            card_entries.append((card_name, set_code, collector_number, quantity, foil))
        
        add_multiple_cards(args.csv_path, card_entries)
    else:
        print("No cards provided. Use the --card option to add cards.")

if __name__ == "__main__":
    main()
