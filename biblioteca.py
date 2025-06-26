

libros = [
    {"id": 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "ISBN": "978-0307474728", "paginas": 432, "cantidad_disponible": 5},
    {"id": 2, "titulo": "1984", "autor": "George Orwell", "ISBN": "978-0451524935", "paginas": 328, "cantidad_disponible": 3},
    {"id": 3, "titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "ISBN": "978-1451673319", "paginas": 194, "cantidad_disponible": 7},
    {"id": 4, "titulo": "Don Quijote", "autor": "Miguel de Cervantes", "ISBN": "978-0060934347", "paginas": 992, "cantidad_disponible": 2},
    {"id": 5, "titulo": "Crónica de una muerte anunciada", "autor": "Gabriel García Márquez", "ISBN": "978-1400034956", "paginas": 128, "cantidad_disponible": 4},
    {"id": 6, "titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "ISBN": "978-0156013987", "paginas": 96, "cantidad_disponible": 10},
    {"id": 7, "titulo": "Ensayo sobre la ceguera", "autor": "José Saramago", "ISBN": "978-0156007757", "paginas": 352, "cantidad_disponible": 3},
    {"id": 8, "titulo": "La sombra del viento", "autor": "Carlos Ruiz Zafón", "ISBN": "978-0143034902", "paginas": 512, "cantidad_disponible": 6},
    {"id": 9, "titulo": "El túnel", "autor": "Ernesto Sabato", "ISBN": "978-9500420305", "paginas": 160, "cantidad_disponible": 2},
    {"id": 10, "titulo": "Pedro Páramo", "autor": "Juan Rulfo", "ISBN": "978-6073142360", "paginas": 144, "cantidad_disponible": 8}
]

usuario = [
    {"nombre": "Ana", "apellido": "González", "rut": "13816108-7", "libros": []},
    {"nombre": "Luis", "apellido": "Rodríguez", "rut": "13872719-2", "libros": []},
    {"nombre": "Camila", "apellido": "Pérez", "rut": "12182343-5", "libros": []},
    {"nombre": "Jorge", "apellido": "Muñoz", "rut": "14044461-9", "libros": []},
    {"nombre": "María", "apellido": "Rojas", "rut": "16149391-0", "libros": []},
    {"nombre": "Diego", "apellido": "Díaz", "rut": "10407062-4", "libros": []},
    {"nombre": "Lucía", "apellido": "Soto", "rut": "19306158-3", "libros": []},
    {"nombre": "Pablo", "apellido": "Torres", "rut": "14864522-5", "libros": []},
    {"nombre": "Valentina", "apellido": "Contreras", "rut": "15592214-1", "libros": []},
    {"nombre": "Tomás", "apellido": "Silva", "rut": "10516040-5", "libros": []}
]

def buscar_usuarios():
    rut = input("Ingrese su rut: ")
    encontrados = False
    for i in usuarios:
        if i["rut"] == rut:
            print(f"Bienvenido/a {i['nombre']} {i['apellido']}")
            encontrados = True
            menu()
            break
    if not encontrados:
        print("El rut del usuario no esta registrado")
        registrar_usuario()

def registrar_usuario():
    nombre = input("Ingrese el nombre del usuario:  ")
    apellido = input("Ingrese el apellido:  ")
    rut = input("Ingrese el RUT: ")
    libros = []

    for i in usuarios:
        if i["rut"] == rut:
            print("El RUT ya se encuentra registrado.")
            return

    nuevo_usuario = {
        "nombre": nombre,
        "apellido": apellido,
        "rut": rut,
        "libros": libros
    }

    usuarios.append(nuevo_usuario)
    print("Usuario agregado exitosamente.")

def prestamo_libro():
    libro = input("Ingrese el nombre del libro que desea pedir de prestamo:   ")

    encontrados = False
    for i in libros:
        if i["titulo"].lower() == libro.lower():
            encontrados = True

            if i["cantidad_disponible"] > 0:
                i["cantidad_disponible"] -= 1
                print(f"Se ha realizado con exito el prestamo del libro quedan la cantidad de:{i['cantidad_disponible']} ")

                if i["cantidad_disponible"] == 0:
                    print("No quedan mas libros disponibles para prestamo ")
            else:
                print("No quedan ejemplares disponibles para prestamo")
            break

    if not encontrados:
        print("El libro ingresado no se encuentra en la biblioteca")

def devolucion_libro():
    libro = input("Ingrese el nombre del libro a devolver:   ")

    encontrado = False
    for i in libros:
        if i["titulo"].lower() == libro.lower():
            i["cantidad_disponible"] += 1
            print(f"Libro devuelto exitosamente. Ahora hay {i['cantidad_disponible']} ejemplares disponibles.")
            encontrado = True
            break

    if not encontrado:
        print("No hay registrado en la biblioteca ese libro.")
        registro_libro()

def registro_libro():
    try:
        id = int(input("Ingrese el id (a partir del 11): "))
        if id < 11:
            print("El id debe ser a partir del 11 en adelante")
            return
    except ValueError as error:
        print("Error:", error)
        return
    
    titulo = input("Ingrese el nombre del libro: ")
    autor = input("Ingrese el nombre del autor: ")
    ISBN = input("Ingrese el ISBN en números: ")

    try:
        paginas = int(input("Ingrese la cantidad de páginas del libro: "))
        if paginas <= 0:
            print("La cantidad de páginas debe ser mayor a 0")
            return
    except ValueError as error:
        print("Error:", error)
        return

    try:
        cantidad_disponible = int(input("Ingrese la cantidad disponible: "))
        if cantidad_disponible <= 0:
            print("La cantidad de libros debe ser mayor a 0")
            return
    except ValueError as error:
        print("Error:", error)
        return

    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            print("El libro ya se encuentra registrado.")
            return
        
        if libro["id"] == id:
            print(f"El id {id} ya está asignado a otro libro.")
            return

    nuevo_libro = {
        "id": id,
        "titulo": titulo,
        "autor": autor,
        "ISBN": ISBN,
        "paginas": paginas,
        "cantidad_disponible": cantidad_disponible
    }

    libros.append(nuevo_libro)
    print(f"Libro '{titulo}' agregado exitosamente.")

def salir():
    print("Saliendo del programa.....")

def menu():
    while True:
        print("1. Realizar un préstamo de un libro")
        print("2. Realizar la devolución de un libro")
        print("3. Volver al menú principal")

        try:
            opcion = int(input("Ingrese una opción: "))
        except ValueError as error:
            print("Error", error)
            continue

        if opcion == 1:
            prestamo_libro()
        elif opcion == 2:
            devolucion_libro()
        elif opcion == 3:
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción inválida, intente nuevamente.")

while True:
    print("Bienvenido al sistema de menu de biblioteca")
    print("1.Buscar usuarios")
    print("2.Registrar un nuevo libro.")
    print("3.Registrar un nuevo usuario")
    print("4.Salir")

    try:
        opcion = int(input("Ingrese una opcion:   "))
    except ValueError as error:
        print("Error", error)
        continue

    if opcion == 1:
        buscar_usuarios()
    elif opcion == 2:
        registro_libro()
    elif opcion == 3:
        registrar_usuario()
    elif opcion == 4:
        salir()
        break

