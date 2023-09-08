'''
Programa de registro de estudiantes que utiliza diccionarios para almacenar información sobre los estudiantes, con sus códigos, nombres y el número de fallas que han tenido.
El programa permite al usuario realizar varias acciones a través de un menú.

Se inicializan dos diccionarios vacíos, nombres_estudiantes y fallas_estudiantes, para almacenar los nombres de los estudiantes y el número de fallas, respectivamente.

Se establece la variable opcion en -1 para iniciar un bucle while que se ejecutará hasta que el usuario seleccione la opción 0 (Salir).

Dentro del bucle while, se muestra un menú de opciones al usuario y se lee la elección del usuario utilizando la función input().

Se declaran variables locales para almacenar el código, nombre y número de fallas de un estudiante, dependiendo de la opción seleccionada por el usuario.

Se utiliza una estructura match para manejar las diferentes opciones del menú:

Opción 1: Registrar estudiante, donde se solicita al usuario ingresar el código y el nombre del estudiante, y se almacenan en los diccionarios correspondientes.
Opción 2: Modificar nombre del estudiante, que permite al usuario cambiar el nombre de un estudiante existente.
Opción 3: Eliminar estudiante, que permite al usuario eliminar a un estudiante por su código.
Opción 4: Consultar estudiante, que muestra el nombre y el número de fallas de un estudiante dado su código.
Opción 5: Consultar todos los estudiantes, que muestra la información de todos los estudiantes registrados.
Opción 6: Tomar asistencia, que permite al usuario registrar la asistencia de un estudiante existente, incrementando el contador de asistencias.
Opción 0: Salir del programa.
El bucle continúa hasta que el usuario selecciona la opción 0 (Salir), momento en el que se muestra un mensaje de despedida y el programa termina.

'''

nombres_estudiantes = {}
asistencias_estudiantes = {}

opcion = -1

while opcion != 0:
    print("Ingresa la opción:")
    print("1. Registrar estudiante")
    print("2. Modificar nombre del estudiante")
    print("3. Eliminar estudiante")
    print("4. Consultar estudiante")
    print("5. Consultar todos los estudiantes")
    print("6. Tomar asistencia")
    print("0. Salir")

    opcion = int(input())

    codigo = ""
    nombre = ""
    asistencias = 0

    match opcion:
        case 1:
            print("Ingrese el código del estudiante")
            codigo = input()
            if codigo not in nombres_estudiantes:
                print("Ingrese el nombre del estudiante")
                nombre = input()
                nombres_estudiantes[codigo] = nombre
                asistencias_estudiantes[codigo] = asistencias
            else:
                print("El código " + codigo + " ya existe")
        case 2:
            print("Ingrese el código del estudiante")
            codigo = input()
            if codigo in nombres_estudiantes:
                print("Ingresa el nuevo nombre del estudiante")
                nombre = input()
                nombres_estudiantes[codigo] = nombre
            else:
                print("NO existe un estudiante con el código " + codigo)
        case 3:
            print("Ingrese el código del estudiante")
            codigo = input()
            del nombres_estudiantes[codigo]
            del asistencias_estudiantes[codigo]
        case 4:
            print("Ingrese el código del estudiante")
            codigo = input()
            if codigo in nombres_estudiantes:
                nombre = nombres_estudiantes[codigo]
                asistencias = asistencias_estudiantes[codigo]
                print("Los datos del estudiante con código: " + codigo)
                print("Nombre: " + nombre)
                print("asistencias: " + str(asistencias))
            else:
                print("NO existe un estudiante con el código " + codigo)
        case 5:
            codigos = nombres_estudiantes.keys()
            print()
            print("Estudiantes registrados: " + str(len(codigos)))
            for cod in codigos:
                nombre = nombres_estudiantes[cod]
                asistencias = asistencias_estudiantes[cod]
                print("Estudiante con Código: " + cod)
                print("Nombre: " + nombre)
                print("asistencias: " + str(asistencias))
                print()
        case 6:
            print("Ingrese el código del estudiante")
            codigo = input()
            if codigo in nombres_estudiantes:
                asistencias = asistencias_estudiantes[codigo]
                asistencias_estudiantes[codigo] = asistencias + 1
            else:
                print("NO existe un estudiante con el código " + codigo)
        case 0:
            print("Chao!!!!")
        case _:
            print("Opción inválida")

    print()
    print()
    print()
    print()
