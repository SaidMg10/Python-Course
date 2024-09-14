from mascotas import Mascota, RegistroMascotas

registro = RegistroMascotas()


while True:
    menu = """--- Menú ---
1. Agregar mascota
2. Listar mascotas
3. Editar mascota
4. Eliminar mascota
5. Salir
Ingrese una opción: """

    opcion = input(menu)
    if opcion == "1":
        nombre = input('Nombre de la mascota: ' )
        especie= input('Especie de la mascota: ')
        edad = input('Edad de la mascota: ')
        mascota = Mascota(especie, edad, nombre)
        registro.agregar_mascota(mascota)

    elif opcion == "2":
        registro.listar_mascotas()

    elif opcion == "3":
        index = int(input("Ingrese indice del registro: "))
        nombre = input('Nombre de la mascota: ' )
        especie= input('Especie de la mascota: ')
        edad = input('Edad de la mascota: ')
        nueva_mascota = Mascota(especie, edad, nombre)
        registro.editar_mascota(index-1, nueva_mascota)

    elif opcion == "4":
        index = int(input("Ingrese indice del registro: "))
        registro.eliminar_mascota(index-1)

    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print('Opción inválida. Por favor, elija una opción válida.')