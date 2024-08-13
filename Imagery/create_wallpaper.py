import os
import random
from PIL import Image

# Function to load, resize, and crop JPG images from a directory
def load_resize_and_crop_images(directory, target_size):
    images = []
    for filename in os.listdir(directory):
        if filename.lower().endswith((".jpg", ".jpeg")):
            try:
                img = Image.open(os.path.join(directory, filename))
                
                # Calculate the aspect ratios for scaling
                img_aspect = img.width / img.height
                target_aspect = target_size[0] / target_size[1]
                
                if img_aspect > target_aspect:
                    # Image is wider than the target: scale height and crop width
                    img = img.resize((int(img_aspect * target_size[1]), target_size[1]), Image.Resampling.LANCZOS)
                    left = (img.width - target_size[0]) / 2
                    img = img.crop((left, 0, left + target_size[0], target_size[1]))
                else:
                    # Image is taller than the target: scale width and crop height
                    img = img.resize((target_size[0], int(target_size[0] / img_aspect)), Image.Resampling.LANCZOS)
                    top = (img.height - target_size[1]) / 2
                    img = img.crop((0, top, target_size[0], top + target_size[1]))
                
                images.append(img)
            except IOError:
                print(f"Warning: Unable to open image {filename}. It may be corrupted or not a valid image file.")
    return images

# Function to create a wallpaper from images
def create_wallpaper(images, screen_size, output_file):
    wallpaper = Image.new('RGB', screen_size)
    
    random.shuffle(images)  # Randomize the order of images
    
    x_offset = 0
    y_offset = 0
    
    for img in images:
        img_width, img_height = img.size
        
        if x_offset + img_width > screen_size[0]:  # Move to next row if needed
            x_offset = 0
            y_offset += img_height
        
        if y_offset + img_height > screen_size[1]:  # Stop if out of vertical space
            break
        
        wallpaper.paste(img, (x_offset, y_offset))
        x_offset += img_width
    
    wallpaper.save(output_file, format='JPEG')
    print(f"Wallpaper saved as {output_file}")

# Function to prompt user for screen size
def get_screen_size():
    sizes = {
        "1": (1920, 1080),
        "2": (2560, 1440),
        "3": (3840, 2160),
        "4": (1280, 720),
        "5": (1600, 900)
    }
    
    print("Choose a screen size:")
    print("1: 1920x1080 (Full HD)")
    print("2: 2560x1440 (2K)")
    print("3: 3840x2160 (4K)")
    print("4: 1280x720 (HD)")
    print("5: 1600x900 (HD+)")
    
    choice = input("Enter the number corresponding to your choice: ")
    
    return sizes.get(choice, (1920, 1080))  # Default to 1920x1080 if invalid choice

def main():
    directory = input("Enter the directory containing JPG files: ")
    screen_size = get_screen_size()
    
    # Determine the target size for each image based on the screen size
    # Here, we assume a grid of 5 images across and as many rows as needed
    target_size = (screen_size[0] // 5, screen_size[1] // 5)
    
    output_file = input("Enter the name of the output wallpaper file (e.g., wallpaper.jpg): ")
    
    # Ensure the output file has a .jpg extension
    if not output_file.lower().endswith('.jpg'):
        output_file += '.jpg'
    
    images = load_resize_and_crop_images(directory, target_size)
    
    if not images:
        print("No JPG files found in the directory.")
        return
    
    create_wallpaper(images, screen_size, output_file)

if __name__ == "__main__":
    main()
