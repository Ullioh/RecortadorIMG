import os
from glob import glob
from PIL import Image

# Rutas de carpetas
carpeta_origen = "D:/USUARIO 001/Nueva carpeta/images/recortadas"
carpeta_destino = "D:/USUARIO 001/Nueva carpeta/images/recortadas/ampliadas"

# Asegurarse de que la carpeta destino existe
if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)

# Dimensiones del área adicional (ancho igual al de la imagen, altura superior e inferior especificadas)
altura_adicional_arriba = 200  # Altura que deseas añadir arriba
altura_adicional_abajo = 220   # Altura que deseas añadir abajo

# Obtener todas las imágenes del formato especificado
imagenes = glob(os.path.join(carpeta_origen, "*.png"))

for imagen_path in imagenes:
    # Abrir la imagen original
    imagen = Image.open(imagen_path)
    
    # Obtener el tamaño de la imagen original
    ancho_original, altura_original = imagen.size
    
    # Crear una nueva imagen más alta (altura original + espacio adicional arriba y abajo)
    nueva_altura = altura_original + altura_adicional_arriba + altura_adicional_abajo
    imagen_ampliada = Image.new("RGB", (ancho_original, nueva_altura), (255, 255, 255))  # Color de fondo blanco
    
    # Pegar la imagen original en el centro (dejando espacio arriba y abajo)
    imagen_ampliada.paste(imagen, (0, altura_adicional_arriba))
    
    # Si quieres agregar una imagen adicional o algún contenido en las áreas añadidas, puedes hacerlo aquí
    # Puedes cargar otra imagen, dibujar, o agregar texto en esas áreas.

    # Guardar la imagen ampliada con el mismo nombre de archivo en la carpeta de destino
    nombre_archivo = os.path.basename(imagen_path)
    imagen_ampliada.save(os.path.join(carpeta_destino, nombre_archivo))

# Salir del programa
sys.exit()