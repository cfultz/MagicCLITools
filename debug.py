import requests
import json

def refactor_commander_name(name):
    # Replace spaces, commas, and apostrophes with dashes
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

def test_archidekt_section(edhrec_data):
    if 'archidekt' in edhrec_data:
        print("Archidekt Section Found:")
        print(json.dumps(edhrec_data['archidekt'], indent=4))  # Pretty-print the Archidekt section

        # Since archidekt is a list, we'll iterate directly over the elements
        for idx, deck_section in enumerate(edhrec_data['archidekt']):
            print(f"\nProcessing Archidekt section {idx}...")
            if isinstance(deck_section, dict) and 'u' in deck_section:
                uuid = deck_section['u']
                print(f"Found UUID: {uuid}")
    else:
        print("No Archidekt section found in the EDHREC data.")

def main():
    commander_name = input("Enter the commander card name: ")
    refactored_name = refactor_commander_name(commander_name)
    
    print(f"Fetching EDHREC data for {commander_name}...")
    edhrec_data = fetch_edhrec_data(refactored_name)

    if edhrec_data:
        print(f"Testing Archidekt section...")
        test_archidekt_section(edhrec_data)

if __name__ == "__main__":
    main()
