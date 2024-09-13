
"""
Calcular el precio de venta

Enunciado: Dado el valor de venta de un producto,se debe calcular el 
Impuesto General a las Ventas (IGV) que es del 18%, y a partir de eso,
determinar el precio de venta final.

"""

# Precio sin iva
# Iva
# Precio más iva


print(' Calculadora de precios ')

ms1 = float(input( 'Ingrese el precio del producto: '))

igv = ms1 * 0.18
precio_total = ms1 + igv


print( 'El IGV es: ', igv)
print('El total es: ', precio_total )