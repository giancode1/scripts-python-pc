import os
import colorama
from colorama import Fore, Style
from PIL import Image


def compress_image(filename, quality):
    # Abrir la imagen
    img = Image.open(filename)

    # Obtener el nombre y la extensión del archivo
    name, ext = os.path.splitext(filename)

    # Crear la carpeta "compressed" si no existe
    if not os.path.exists("compressed"):
        os.makedirs("compressed")

    # Comprimir la imagen y guardarla en la carpeta "compressed"
    compressed_filename = f"compressed/{name}{ext}"
    img.save(compressed_filename, optimize=True, quality=quality)

    # Mostrar el tamaño antes y después de la compresión
    original_size = os.path.getsize(filename)
    compressed_size = os.path.getsize(compressed_filename)
    print(f"Tamaño original: {original_size} bytes")
    print(f"Tamaño comprimido: {compressed_size} bytes")


def compress_all_images(quality):
    colorama.init()
    error_count = 0
    success_count = 0
    for filename in os.listdir():
        try:
            if filename.lower().endswith((".jpg", ".jpeg", ".png")):
                print(f"Comprimiendo {filename}...")
                compress_image(filename, quality)
                print(Fore.GREEN + f"{filename} comprimido con éxito." + Style.RESET_ALL)
                success_count += 1
        except Exception as e:
            print(Fore.RED + f"Error al comprimir {filename}: {e}" + Style.RESET_ALL)
            error_count += 1
    total_count = success_count + error_count
    print(f"----Procesadas un total de {total_count} imágenes.----")
    print(f"{success_count} imágenes comprimidas con éxito.")
    if error_count > 0:
        print(Fore.RED + f"{error_count} imágenes con errores." + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "Todas las imágenes fueron comprimidas con éxito." + Style.RESET_ALL)


# Ejemplo de uso
compress_all_images(80)
