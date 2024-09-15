class ColorNoValidoError(Exception):
    def __init__(self, color: str) -> None:
        super().__init__(f'El color {color} no se encuentra en la lista')

def colores(color):
    lista_colores = ['azul', 'verde', 'rojo']

    if color not in lista_colores:
        raise Exception(f'El color {color} no se encuentra en la lista')
    
try:
    colores('amarillo')
except ColorNoValidoError as error:
    print(f'Error: {error}')