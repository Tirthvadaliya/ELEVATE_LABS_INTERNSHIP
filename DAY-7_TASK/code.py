import os
from PIL import Image

def resize_images(input_folder, output_folder, size=(800, 800), output_format="JPEG"):
    """
    Resize and convert images in batch.
    
    Parameters:
        input_folder (str): Path to the folder with input images.
        output_folder (str): Path to save resized images.
        size (tuple): New size for images (width, height).
        output_format (str): Format to save images ("JPEG", "PNG", etc.)
    """
    
    # Create output folder if not exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the folder
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        # Skip if not an image
        if not (filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))):
            continue

        try:
            # Open image
            with Image.open(file_path) as img:
                # Resize
                img_resized = img.resize(size)

                # Create new file name
                base_name, _ = os.path.splitext(filename)
                new_filename = f"{base_name}.{output_format.lower()}"
                save_path = os.path.join(output_folder, new_filename)

                # Save image
                img_resized.save(save_path, output_format)

                print(f"✅ Saved: {save_path}")
        
        except Exception as e:
            print(f"❌ Could not process {filename}: {e}")

# Example usage
if __name__ == "__main__":
    input_folder = "input_images"   # Folder with original images
    output_folder = "output_images" # Folder for resized images
    resize_images(input_folder, output_folder, size=(500, 500), output_format="JPEG")
