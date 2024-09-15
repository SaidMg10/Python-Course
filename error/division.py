try:
    a = int(input('Ingrese un número entero: '))
    b = int(input('Ingrese un número entero diferente de cero: '))

    resultado = a / b
    print(f'División entre {a}/{b} = {resultado}')
except ValueError:
    print('¡Error! Debes ingresar números enteros.')
except ZeroDivisionError:
    print('¡Error! No puedes dividir entre cero.')
except Exception as e:
    print('Error', e)


