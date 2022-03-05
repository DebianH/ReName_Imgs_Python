#Programa que corrige el nombre de las imagenes, este caso cuando tiene espacios en blanco.
import os

os.chdir('/Users/HP/OneDrive/Escritorio/imagenes') # <- Ubicacion de la carpeta de imagenes.

for f in os.listdir():
    nombre_archivo, extension_archivo = os.path.splitext(f)

    if extension_archivo != '.png':  #<- validamos la extension de la imagen.
        print('Imagen no valida -> ',nombre_archivo)
    else:
        nuevo_archivo = nombre_archivo.replace(" ","_")

        new = '{}{}'.format(nuevo_archivo,extension_archivo)

        os.rename(f,new)


print("[+] Nombres de imagenes actualizados!")

#By David Hernandez
