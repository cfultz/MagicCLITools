import requests
import pandas as pd
import os
import time

# Function to fetch card details from Scryfall using the set code and collector number
def fetch_card_images_by_set_and_number(set_code, collector_number):
    url = f"https://api.scryfall.com/cards/{set_code}/{collector_number}"
    response = requests.get(url)
    
    if response.status_code == 200:
        card_data = response.json()
        images = []
        
        # Handle single-sided or multi-sided cards
        if 'image_uris' in card_data:
            images.append((card_data['image_uris']['art_crop'], card_data['name']))
        if 'card_faces' in card_data:
            for face in card_data['card_faces']:
                if 'image_uris' in face:
                    images.append((face['image_uris']['art_crop'], face['name']))
        return images
    else:
        print(f"Error fetching card with set code {set_code} and collector number {collector_number}: {response.status_code}")
        return None

# Function to download and save an image
def download_image(image_url, save_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
    else:
        print(f"Failed to download image from {image_url}")

# Function to process the CSV and download images
def download_images_from_csv(csv_path, output_folder):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Read the CSV file
    df = pd.read_csv(csv_path)
    
    # Assuming the CSV has columns 'Card Name', 'Set Code', and 'Collector Number'
    for index, row in df.iterrows():
        card_name = row['Card Name']
        set_code = row['Set Code']
        collector_number = row['Collector Number']
        
        # Naming convention: set_code_card_name_face_name.jpg
        image_base_name = f"{set_code}_{card_name.replace('/', '-').replace(':', '').replace(' ', '-').replace(',', '-')}"
        
        print(f"Processing {card_name} from set {set_code} with collector number {collector_number}...")
        
        images = fetch_card_images_by_set_and_number(set_code, collector_number)
        if images:
            for image_url, face_name in images:
                # Sanitize file name by removing invalid characters
                image_file_name = f"{image_base_name}_art_crop.jpg"
                save_path = os.path.join(output_folder, image_file_name)
                
                # Skip downloading if the image already exists
                if os.path.exists(save_path):
                    print(f"Image already exists for {card_name} ({face_name}), skipping download.")
                    continue
                
                download_image(image_url, save_path)
                time.sleep(0.1)  # Sleep to avoid hitting API rate limits
        else:
            print(f"No images found for {card_name} from set {set_code} with collector number {collector_number}")

# Main execution
if __name__ == "__main__":
    # Define the path to the input CSV and output folder
    csv_path = 'cards.csv'  # Replace with your CSV file path
    output_folder = 'artcrop_images'
    
    # Start the download process
    download_images_from_csv(csv_path, output_folder)
    print("Download completed.")
