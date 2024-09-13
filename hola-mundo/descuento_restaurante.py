insumo = float(input('Ingrese el monto de consumo en el restaurante: '))

disc_10 = insumo * 0.1
disc_20 = insumo * 0.2
disc_30 = insumo * 0.3

if insumo > 50 and insumo < 100 :
    print('El insumo fue de: ', insumo,
          'El descuento fue de: ', disc_10,
          'El total con descuento fue de: ', insumo - disc_10)
elif insumo > 100 and insumo <= 200:
    print('El insumo fue de: ', insumo,
          'El descuento fue de: ', disc_20,
          'El total con descuento fue de: ', insumo - disc_20)
elif insumo > 200:
    print('El insumo fue de: ', insumo,
          'El descuento fue de: ', disc_30,
          'El total con descuento fue de: ', insumo - disc_30)
elif insumo <= 50 :
    print('El insumo fue de: ', insumo,
          'El descuento no aplica',
          'El total fue de: ', insumo )