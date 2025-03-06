from PIL import Image
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

def extract_colors(image_path, num_colors=5):
    # Ouvrir l'image et la convertir en mode RGB
    image = Image.open(image_path).convert('RGB')
    # Redimensionner pour accélérer le traitement
    image = image.resize((100, 100))
    # Récupérer tous les pixels de l'image
    pixels = list(image.getdata())
    # Compter la fréquence de chaque couleur
    counter = Counter(pixels)
    # Trouver les `num_colors` couleurs les plus fréquentes
    most_common = counter.most_common(num_colors)
    # Extraire uniquement les valeurs RGB
    colors = [color for color, count in most_common]
    return colors

def calculate_mid_tones(colors):
    # Calculer la teinte moyenne en ajoutant (128, 128, 128) à chaque couleur et en divisant par 2
    gray = np.array([128, 128, 128])
    mid_tones = [(np.array(color) + gray) // 2 for color in colors]
    mid_tones = [tuple(map(int, mid_tone)) for mid_tone in mid_tones]

    # Fonction pour calculer la luminosité d'une couleur
    def brightness(color):
        r, g, b = color
        return 0.299 * r + 0.587 * g + 0.114 * b

    # Trier les couleurs du plus foncé au plus clair
    mid_tones = sorted(mid_tones, key=brightness)
    mid_tones[4], mid_tones[3] = mid_tones[3], mid_tones[4]
    return mid_tones


# Exemple d'utilisation
image_path = "../hyprland/wallpaper.png"
colors =  extract_colors(image_path, num_colors=5)
mid_tones = calculate_mid_tones(colors)
print("Palette de couleurs extraite :", mid_tones)


with open("default.css", "r") as f:
    file = f.read()

for i, variation in enumerate(["VERY_DARK", "DARK", "DEFAULT", "VERY_LIGHT", "LIGHT"]):
    file = file.replace(variation, f"rgb{mid_tones[i]}")

with open("style.css", "w") as f:
    f.write(file)
