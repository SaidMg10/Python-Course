palabra = input('ingrese una palabra: ')
palabra = palabra.lower()
palabrea = palabra.replace(' ','')
palabra_invertida = palabra[::-1]

if palabra == palabra_invertida:
    print(f'la palabra {palabra} es un palindromo')
else:
    print( 'No es un palindromo')