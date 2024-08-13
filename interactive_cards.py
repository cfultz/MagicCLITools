import csv
import os

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

# Function to get user input and add multiple cards interactively
def interactive_card_entry(csv_path):
    while True:
        # Get the card details from the user
        card_name = input("Enter the card name (or type 'exit' to quit): ").strip()
        if card_name.lower() == 'exit':
            print("Exiting the program.")
            break

        set_code = input("Enter the set code: ").strip()
        collector_number = input("Enter the collector number: ").strip()
        quantity = int(input("Enter the quantity: ").strip())
        foil = input("Is this card a foil? (yes/no): ").strip().lower() == 'yes'
        
        # Add the card to the CSV file
        add_card_to_csv(csv_path, card_name, set_code, collector_number, quantity, foil)

if __name__ == "__main__":
    csv_path = input("Enter the path to the CSV file: ").strip()
    interactive_card_entry(csv_path)
