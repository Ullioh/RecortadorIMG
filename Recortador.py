import os
from glob import glob
from PIL import Image

# ruta de la carpeta donde están las imágenes originales
carpeta_origen = "D:/USUARIO 001/Nueva carpeta/images" #bucar en la pc
carpeta_destino = "D:/USUARIO 001/Nueva carpeta/images/recortadas" #bucar en la pc y puedes poner el nombre que quieras dondes dice "recortadas"

# se crea la carpeta de destino lo mas probable e sque no exisra
if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)

# como se va a recortar va en ese orden (izquierda, arriba, derecha, abajo)
area_a_recortar = (100, 662, 1436, 1496)

# busca todas las imagenes, si es un formato dufernete se deben cambiar.
imagenes = glob(os.path.join(carpeta_origen, "*.png")) #.jpg, .png 

for imagen_path in imagenes:
    # abre la imagen
    imagen = Image.open(imagen_path)
    
    # recorta la imagen
    imagen_recortada = imagen.crop(area_a_recortar)
    
    # toma el nombre de archivo original
    nombre_archivo = os.path.basename(imagen_path)
    
    # guarda la imagen recortada en la carpeta de destino con el mismo nombre
    imagen_recortada.save(os.path.join(carpeta_destino, nombre_archivo))
#cierra el ciclo del programa para que no haya ni errores ni conflictos
sys.exit()
