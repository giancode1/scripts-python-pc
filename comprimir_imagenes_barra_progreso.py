import os
import colorama
from colorama import Fore, Style
from PIL import Image
from tqdm import tqdm


def compress_image(filename, quality):
    # Abrir la imagen
    img = Image.open(filename)

    # Obtener el nombre y la extensión del archivo
    name, ext = os.path.splitext(filename)

    # Crear la carpeta "compressed" si no existe
    if not os.path.exists("compressed"):
        os.makedirs("compressed")

    # Comprimir la imagen y guardarla en la carpeta "compressed"
    compressed_filename = f"compressed/{name}_compressed{ext}"
    img.save(compressed_filename, optimize=True, quality=quality)


def compress_all_images(quality):
    colorama.init()
    error_count = 0
    success_count = 0
    total_original_size = 0
    total_compressed_size = 0
    images = [filename for filename in os.listdir() if filename.lower().endswith((".jpg", ".jpeg", ".png"))]
    with tqdm(total=len(images), desc="Comprimiendo imágenes") as pbar:
        for filename in images:
            try:
                # Obtener el tamaño de la imagen original
                original_size = os.path.getsize(filename)
                total_original_size += original_size
                
                compress_image(filename, quality)
                
                # Obtener el tamaño de la imagen comprimida
                compressed_size = os.path.getsize(f"compressed/{os.path.splitext(filename)[0]}_compressed{os.path.splitext(filename)[1]}")
                total_compressed_size += compressed_size
                
                success_count += 1
            except Exception as e:
                print(Fore.RED + f"Error al comprimir {filename}: {e}" + Style.RESET_ALL)
                error_count += 1
            pbar.update(1)
    total_count = success_count + error_count
    print(f"----Procesadas un total de {total_count} imágenes----")
    print(f"{success_count} imágenes comprimidas con éxito.")

    if error_count > 0:
        print(Fore.RED + f"{error_count} imágenes con errores." + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "Todas las imágenes fueron comprimidas con éxito." + Style.RESET_ALL)
        
    total_reduction = (total_original_size - total_compressed_size) / (1024 * 1024) # Convertir a MB
    total_reduction_percentage = (total_reduction / (total_original_size / (1024 * 1024))) * 100 # Calcular el porcentaje
    
    print(f"Reducción total de {total_reduction:.2f} MB ({total_reduction_percentage:.2f}%)")


# Ejemplo de uso
compress_all_images(80)
