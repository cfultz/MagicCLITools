import requests

def refactor_commander_name(name):
    # Replace spaces, commas, and apostrophes with dashes, and convert to lowercase
    name = name.replace(" ", "-").replace(",", "").replace("'", "")
    return name.lower()

def fetch_edhrec_data(commander_name):
    url = f"https://json.edhrec.com/pages/commanders/{commander_name}.json"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {commander_name}")
        return None

def fetch_card_name_from_scryfall(uuid):
    scryfall_url = f"https://api.scryfall.com/cards/{uuid}"
    response = requests.get(scryfall_url)

    if response.status_code == 200:
        data = response.json()
        return data['name']
    else:
        print(f"Failed to fetch card name from Scryfall for UUID: {uuid}")
        return None

def extract_uuids_and_quantities_from_archidekt(edhrec_data):
    card_info = []

    if 'archidekt' in edhrec_data:
        for idx, deck_section in enumerate(edhrec_data['archidekt']):
            if isinstance(deck_section, dict) and 'u' in deck_section and 'q' in deck_section:
                uuid = deck_section['u']
                quantity = deck_section['q']
                card_info.append((uuid, quantity))
    else:
        print("No Archidekt section found in the EDHREC data.")

    return card_info

def fetch_card_names_from_uuids(card_info):
    card_entries = []
    for uuid, quantity in card_info:
        card_name = fetch_card_name_from_scryfall(uuid)
        if card_name:
            card_entries.append(f"{quantity}x {card_name}")
    return card_entries

def create_moxfield_deck_file(commander_name, card_entries):
    filename = f"{commander_name}_edh.txt"
    with open(filename, 'w') as file:
        for entry in card_entries:
            file.write(f"{entry}\n")
    print(f"Deck list saved to {filename}")

def main():
    commander_name = input("Enter the commander card name: ")
    refactored_name = refactor_commander_name(commander_name)
    
    print(f"Fetching EDHREC data for {commander_name}...")
    edhrec_data = fetch_edhrec_data(refactored_name)

    if edhrec_data:
        print(f"Extracting UUIDs and quantities from Archidekt section...")
        card_info = extract_uuids_and_quantities_from_archidekt(edhrec_data)
        
        if card_info:
            print(f"Fetching card names from Scryfall...")
            card_entries = fetch_card_names_from_uuids(card_info)
            if card_entries:
                create_moxfield_deck_file(refactored_name, card_entries)
            else:
                print("No card names found for the given UUIDs.")
        else:
            print("No UUIDs found in the Archidekt decks.")

if __name__ == "__main__":
    main()
