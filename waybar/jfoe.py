from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def rgb_to_luminosity(rgb):
    """Convert RGB color to luminosity using the perceived brightness formula."""
    return 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]

def generate_palette(image_path, num_colors=10):
    # Load the image
    image = Image.open(image_path)
    
    # Resize image for faster processing
    image = image.resize((image.width // 10, image.height // 10))
    
    # Convert image to RGB and get colors
    pixels = np.array(image.convert('RGB'))
    pixels = pixels.reshape(-1, 3)
    
    # Count the frequency of each color
    color_counts = Counter(map(tuple, pixels))
    
    # Get the most common colors
    most_common_colors = color_counts.most_common(num_colors * 5)  # Get more colors to sample from
    
    # Extract colors and their frequencies
    colors = [color for color, count in most_common_colors]
    
    # Sort colors by luminosity
    colors_sorted = sorted(colors, key=rgb_to_luminosity)
    
    # Select mid-tones (e.g., colors around the middle luminosity range)
    mid_tone_colors = []
    min_lum = rgb_to_luminosity(colors_sorted[0])
    max_lum = rgb_to_luminosity(colors_sorted[-1])
    
    mid_tone_range = (min_lum + max_lum) / 2
    for color in colors_sorted:
        if abs(rgb_to_luminosity(color) - mid_tone_range) < (max_lum - min_lum) / 8:
            mid_tone_colors.append(color)

    # Create a palette to display the sorted mid-tone colors
    unique_mid_tone_colors = list(set(mid_tone_colors))[:num_colors]  # Ensure we have enough colors
    palette = np.zeros((100, 100 * len(unique_mid_tone_colors), 3), dtype=np.uint8)
    
    for i, color in enumerate(unique_mid_tone_colors):
        palette[:, i*100:(i+1)*100] = color

    # Show the palette
    plt.imshow(palette)
    plt.axis('off')  # Turn off axis
    plt.title('Mid-tone Color Palette')
    plt.show()

# Example usage
image_path = '../hyprland/wallpaper.png'  # Replace with your image path
generate_palette(image_path)
