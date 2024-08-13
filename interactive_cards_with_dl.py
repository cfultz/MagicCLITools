import csv
import os
import requests

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

# Function to download the full card image
def download_full_card_image(set_code, collector_number, card_name, foil):
    url = f"https://api.scryfall.com/cards/{set_code}/{collector_number}"
    response = requests.get(url)
    
    if response.status_code == 200:
        card_data = response.json()
        
        # Determine the image URL (normal)
        image_url = card_data['image_uris']['normal'] if 'image_uris' in card_data else None
        if not image_url and 'card_faces' in card_data:  # Check for double-sided cards
            image_url = card_data['card_faces'][0]['image_uris']['normal']
        
        if image_url:
            # Create the full_card directory if it doesn't exist
            directory = 'full_card'
            if not os.path.exists(directory):
                os.makedirs(directory)

            # Create a filename for the image
            foil_text = "_foil" if foil else ""
            file_name = f"{card_name.replace('/', '-').replace(':', '').replace(' ', '_')}_{set_code}_{collector_number}{foil_text}.jpg"
            file_path = os.path.join(directory, file_name)

            # Download and save the image
            image_response = requests.get(image_url)
            with open(file_path, 'wb') as file:
                file.write(image_response.content)
            
            print(f"Downloaded full card image for {card_name} (Set: {set_code}, Collector Number: {collector_number}, Foil: {foil})")
        else:
            print(f"No full card image found for {card_name} (Set: {set_code}, Collector Number: {collector_number})")
    else:
        print(f"Failed to fetch data for {card_name} (Set: {set_code}, Collector Number: {collector_number}) from Scryfall.")

# Function to sort the CSV file by Set Code and Collector Number
def sort_csv_file(csv_path):
    with open(csv_path, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Read the header
        sorted_rows = sorted(reader, key=lambda row: (row[1], int(row[2])))  # Sort by Set Code (row[1]) and Collector Number (row[2]))

    # Write the sorted data back to the CSV
    with open(csv_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Write the header back
        writer.writerows(sorted_rows)  # Write the sorted rows

    print(f"CSV file sorted by Set Code and Collector Number.")

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

        # Download the full card image
        download_full_card_image(set_code, collector_number, card_name, foil)

        # Sort the CSV file after each entry
        sort_csv_file(csv_path)

if __name__ == "__main__":
    csv_path = input("Enter the path to the CSV file: ").strip()
    interactive_card_entry(csv_path)
