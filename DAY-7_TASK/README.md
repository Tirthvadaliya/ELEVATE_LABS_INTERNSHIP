# Image Batch Resizer and Converter

This project provides a Python script ([code.py](code.py)) to batch resize and convert images from an input folder to an output folder. It uses the [Pillow](https://python-pillow.org/) library for image processing.

## Features

- Batch resize images to a specified size.
- Convert images to a specified format (e.g., JPEG, PNG).
- Supports common image formats: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`.
- Automatically creates the output directory if it does not exist.
- Skips non-image files.
- Prints status messages for each processed file.

## Requirements

- Python 3.x
- [Pillow](https://pypi.org/project/Pillow/)

## Installation

1. **Clone or download this repository.**
2. **Install Pillow:**
   ```sh
   pip install Pillow
   ```

## Usage

1. Place the images you want to process in the `input_images/` folder.
2. Run the script:

   ```sh
   python code.py
   ```

   By default, this will:
   - Read images from `input_images/`
   - Resize them to 500x500 pixels
   - Convert and save them as JPEGs in `output_images/`

3. The processed images will be saved in the `output_images/` folder.

## Customization

You can change the resize dimensions and output format by modifying the script or calling the `resize_images` function with different arguments.

### Example

```python
from code import resize_images

resize_images(
    input_folder="input_images",
    output_folder="output_images",
    size=(800, 800),           # Resize to 800x800 pixels
    output_format="PNG"        # Save as PNG
)
```

## Script Details

- **Function:** `resize_images(input_folder, output_folder, size=(800, 800), output_format="JPEG")`
  - `input_folder`: Path to the folder containing input images.
  - `output_folder`: Path to save resized images.
  - `size`: Tuple specifying the new size `(width, height)`.
  - `output_format`: Format to save images (`"JPEG"`, `"PNG"`, etc.).

## Example Output

```
✅ Saved: output_images/21.jpeg
✅ Saved: output_images/Ganesha-f000067c-dc26-45ca-baf6-f00c2a6883ab.jpeg
✅ Saved: output_images/IMG-20230519-WA0011.jpeg
✅ Saved: output_images/Lord Krishna Aesthetic Laptop Wallpaper.jpeg
```

## Error Handling

If an image cannot be processed, the script will print an error message and continue with the next file.

