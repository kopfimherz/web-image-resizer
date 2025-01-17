from PIL import Image
import os

input_dir = "_input"  # Ordner mit Originalbildern
output_dir = "_output"  # Ordner für konvertierte Bilder

sizes = {"x1": 800, "x3": 1024}  # Zielbreiten
formats = ["jpeg", "webp"]  # Zielbildformate

os.makedirs(output_dir, exist_ok=True)  # Erstelle den Ausgabeordner, falls nötig

for filename in os.listdir(input_dir):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):  # Unterstützte Formate
        input_path = os.path.join(input_dir, filename)

        with Image.open(input_path) as img:
            for size_label, width in sizes.items():
                aspect_ratio = img.height / img.width
                new_height = int(width * aspect_ratio)
                resized_img = img.resize((width, new_height), Image.Resampling.LANCZOS)

                for fmt in formats:
                    base_name, _ = os.path.splitext(filename)
                    output_filename = f"{base_name}_{size_label}.{fmt}"
                    output_path = os.path.join(output_dir, output_filename)

                    resized_img.save(output_path, format=fmt.upper(), quality=95)
                    print(f"Gespeichert: {output_path}")