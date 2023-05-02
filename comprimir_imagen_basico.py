from PIL import Image

# Abrir imagen
img = Image.open('nombre_de_la_imagen.jpg')

# Guardar imagen comprimida
img.save('nombre_de_la_imagen_comprimida.jpg', optimize=True, quality=50)