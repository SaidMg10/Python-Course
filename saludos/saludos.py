import random

def formato_aleatorio()->str:
    '''
    Retorna un saludo aleatorio formateado con el nombre proporcionado.
    
    Returns:
        str: Saludo aleatorio con el formato adecuado.
    '''
    formatos = [
        "¡Hola, {}! ¡Bienvenido!",
        "¡Es genial verte, {}!",
        "¡Saludos, {}! ¡Encantado de conocerte!",
    ]

    return random.choice(formatos)

def hola(nombre:str)->str:
    '''
    Genera un saludo personalizado utilizando un nombre.

    Args:
        nombre (str): Nombre del destinatario del saludo.
    Returns:
        str: Saludo personalizado.
    '''
    if nombre == "":
        return "Error: Nombre vació."
    
    saludo = formato_aleatorio().format(nombre)
    return saludo

def holas(nombres:list)->dict:
    '''
    Genera saludos personalizados para una lista de nombres.
    
    Args:
            nombres (List[str]): Lista de nombres para los cuales se generarán saludos.
    
    Returns:
            Dict[str, str]: Diccionario donde las claves son nombres y los valores son saludos personalizados.
    '''
    saludos = {}
    for nombre in nombres:
        saludo = hola(nombre)
        saludos[nombre] = saludo
    return saludos


