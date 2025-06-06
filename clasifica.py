import os
import shutil

def mover_archivos_por_tipo(directorio):
    # Asegurarse de que el directorio exista
    if not os.path.isdir(directorio):
        print(f"El directorio {directorio} no existe.")
        return
    
    # Crear la carpeta "otros" si no existe
    carpeta_otros = os.path.join(directorio, 'otros')
    if not os.path.exists(carpeta_otros):
        os.makedirs(carpeta_otros)
    
    # Listar todos los archivos en el directorio
    archivos = os.listdir(directorio)
    
    for archivo in archivos:
        # Obtenemos la ruta completa del archivo
        archivo_path = os.path.join(directorio, archivo)
        
        # Verificar si es un archivo (no una carpeta)
        if os.path.isfile(archivo_path):
            # Intentamos obtener la extensión del archivo
            extension = archivo.split('.')[-1]
            
            # Si no tiene extensión, moverlo a "otros"
            if archivo == extension:  # Es un archivo sin extensión
                destino = os.path.join(carpeta_otros, archivo)
            else:
                # Si tiene extensión, moverlo a una carpeta con el nombre de la extensión
                carpeta_destino = os.path.join(directorio, extension)
                if not os.path.exists(carpeta_destino):
                    os.makedirs(carpeta_destino)
                destino = os.path.join(carpeta_destino, archivo)
            
            # Mover el archivo al destino adecuado
            shutil.move(archivo_path, destino)
            print(f"Archivo {archivo} movido a {destino}")

# Ejemplo de uso
directorio = "C:\\Users\\Q188560\\Downloads"  # Cambia esta ruta por la que desees
mover_archivos_por_tipo(directorio)
