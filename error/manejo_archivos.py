try:
    archivo = open("archivo.txt", "r")
    contenido = archivo.read()

    print('Contenido del archivo:')
    print(contenido)
except FileNotFoundError:
    print('El archivo no se ha encontrado.')
    print('Creando el archivo...')
    archivo = open("archivo.txt", "w")
    archivo.write('Hola mundo')
else:
    print("Contenido del archivo:")
    print(contenido)
finally:
    if archivo:
        archivo.close()
    

    
try:
    with open('archivo.txt', 'r') as archivo:
        contenido = archivo.read()
    print('Contenido del archivo:')
    print(contenido)
except FileNotFoundError:
    print('El archivo no se ha encontrado.')
    print('Creando el archivo...')
    with open('archivo.txt', 'w') as archivo:
        archivo.write('Hola mundo')
else:
    print("Contenido del archivo:")
    print(contenido)
finally:
    if archivo:
        archivo.close()
    

