
registro_estudiantes = []

while True:
    print("1. Registrar Estudiante")
    print("2. Mostrar Registro")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        #Registrar estudiante
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        curso = input("Ingrese el curso del estudiante: ")

        estudiante = {"Nombre": nombre, "Edad": edad, "Curso": curso }
        registro_estudiantes.append(estudiante)
        print("Estudiante registrado exitosamente!\n")

    elif opcion == '2':
        if registro_estudiantes:
            print("\nRegistro de Estudiantes:")
            for estudiante in registro_estudiantes:
                print(f"Nombre: {estudiante["Nombre"]}, Edad: {estudiante["Edad"]}, Curso: {estudiante["Curso"]} \n")
            else:
                print("El registro está vació. Registre estudiantes primero.\n")
    elif opcion == '3':
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no valida, intente de nuevo\n")




        # for indice, valor in enumerate(registro_estudiantes, start=1):
        #     print(f"{indice}. {valor}")