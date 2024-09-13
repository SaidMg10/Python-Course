# Entrada de datos

n = int(input('Ingrese un numero entero: '))

# if n % 2 == 0:
#     print('El numero ingresado es Par')
# else:
#     print('El numero ingresado es Impar')

if n > 0:
    print("Es Par positivos" if n % 2 == 0 else "Es Impar positivo")
elif n < 0:
    print("Es Par negativo" if n % 2 == 0 else "Es Impar negativo")
else:
    print("El número es cero")