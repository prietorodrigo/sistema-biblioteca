libros = {
    "1": {"nombre": "1984", "autor": "Orwell", "género": "Distopía", "cantidad": 5},
    "2": {"nombre": "El Principito", "autor": "Saint-Exupéry", "género": "Fábula", "cantidad": 3},
    "3": {"nombre": "Cien años de soledad", "autor": "Gabriel García Márquez", "género": "Realismo mágico", "cantidad": 4},
    "4": {"nombre": "Fahrenheit 451", "autor": "Ray Bradbury", "género": "Ciencia ficción", "cantidad": 1}
}

usuarios = {
    "12345678": {"nombre": "Juan", "telefono": "46212345", "ciudad": "Rivera"},
    "87654321": {"nombre": "Ana", "telefono": "46312345", "ciudad": "Tacuarembó"},
    "43215678": {"nombre": "Pedro", "telefono": "46412345", "ciudad": "Melo"},
    "12348765": {"nombre": "Claudia", "telefono": "47712345", "ciudad": "Artigas"}
}

prestamos = [] #id, fechaPrestamo, fechaDevolucion, tipo, usuario, libro, devuelto

mantenimiento = [] #libro, fechaIngreso, nombreRestaurador, estado, situacion

def alta_libro():
    if libros:
        ultimo_codigo = max(int(c) for c in libros.keys())
        codigo = str(ultimo_codigo + 1)
    else:
        codigo = "1"
    n = input("Nombre: ")
    a = input("Autor: ")
    g = input("Género: ")
    cant = int(input("Cantidad: "))
    libros[codigo] = {"nombre": n, "autor": a, "género": g, "cantidad": cant}
    return (libros)

def modifica_libro(op1, op2):
    if op2 == 1:
        n = input("Nombre: ")
        libros[op1]["nombre"] = n
    if op2 == 2:
        a = input("Autor: ")
        libros[op1]["autor"] = a
    if op2 == 3:
        g = input("Género: ")
        libros[op1]["género"] = g
    if op2 == 4:
        cant = int(input("Cantidad: "))
        libros[op1]["cantidad"] = cant
    if op2 == 5:
        menu()

def baja_libro():
    c = input("Código: ")
    libros.pop(c)

def alta_usuario():
    ci = input("Cédula de identidad: ")
    n = input("Nombre: ")
    t = input("Teléfono: ")
    cd = input("Ciudad: ")
    usuarios[ci] = {"nombre": n, "telefono": t, "ciudad": cd}
    return (usuarios)

def modifica_usuario(op1, op2):
    if op2 == 1:
        n = input("Nombre: ")
        usuarios[op1]["nombre"] = n
    if op2 == 2:
        t = input("Teléfono: ")
        usuarios[op1]["telefono"] = t
    if op2 == 3:
        cd = input("Ciudad: ")
        usuarios[op1]["ciudad"] = cd
    if op2 == 4:
        menu()

def baja_usuario():
    ci = input("Cédula de identidad: ")
    usuarios.pop(ci)

def leer_fecha():
    d = int(input('Día: '))
    m = int(input('Mes: '))
    a = int(input('Año: '))
    if (d < 32 and (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12)):
        return(d, m, a)
    if (d < 31 and (m == 4 or m == 6 or m == 9 or m == 11)):
        return(d, m, a)
    if (m == 2 and (d < 29 or (d < 30 and a % 4 == 0))):
        return(d, m, a)
    op = input("Error fecha \nIngresa nuevamente s/n")
    if op == 's':
        return leer_fecha()
    return None

def sumar_dias(fecha, dias):
    d, m, a = fecha
    for _ in range(dias):
        d += 1
        if (d > 31 and (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12)):
            d = 1
            m += 1
            if m > 12:
                m = 1
                a += 1
        elif (d > 30 and (m == 4 or m == 6 or m == 9 or m == 11)):
            d = 1
            m += 1
        elif m == 2:
            if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
                if d > 29:
                    d = 1
                    m += 1
            else:
                if d > 28:
                    d = 1
                    m += 1
    return d, m, a

def realizar_prestamo():
    if prestamos:
        ultimo_codigo = max(int(p[0]) for p in prestamos)
        id = str(ultimo_codigo + 1)
    else:
        id = "1"
    fp = leer_fecha()
    if fp == None:
        return None
    t = input("Tipo de Préstamo (Normal o Extenso): ")
    if t == "Normal":
        fd = sumar_dias(fp, 3)
    elif t == "Extenso":
        fd = sumar_dias(fp, 7)
    u = input("Usuario: ")
    for usuario in usuarios.values():
        if u == usuario["nombre"]:
            break
    else:
        print("Error usuario")
        return None
    l = input("Libro: ")
    for libro in libros.values():
        if l == libro["nombre"]:
            if libro["cantidad"] > 0:
                libro["cantidad"] = libro["cantidad"] - 1
                d = False
                return [id, fp, fd, t, u, l, d]
            else:
                print("No hay ejemplares disponibles para este libro")
            break
    else:
        print("Error libro")
        return None
    
def registrar_devolucion():
    id = input("Digite el ID del préstamo: ")
    for prestamo in prestamos:
        if prestamo[0] == id:
            prestamo[6] = True
            for libro in libros.values():
                if prestamo[5] == libro["nombre"]:
                    libro["cantidad"] = libro["cantidad"] + 1
            break
    else:
        print("Préstamo no encontrado")

def agregar_reparacion():
    l = input("Libro: ")
    for libro in libros.values():
        if l == libro["nombre"]:
            if libro["cantidad"] > 0:
                libro["cantidad"] = libro["cantidad"] - 1
            else:
                print("No hay ejemplares disponibles para este libro")
            break
    else:
        print("Error libro")
        return None
    
    fi = leer_fecha()
    if fi == None:
        return None
    
    restaurador = input("Nombre del restaurador: ")

    estado = input("Estado: ")

    situacion = True

    return [l, fi, restaurador, estado, situacion]

def reparar_libro():
    if mantenimiento:
        for mant in mantenimiento:
            lib = mant[0]
            for libro in libros.values():
                if lib == libro["nombre"]:
                    libro["cantidad"] = libro["cantidad"] + 1
        mantenimiento.pop()
    else:
        print("No hay libros para reparar")
        
    

def menu():
    op = int(input("Menú principal: \n\n1. Libros \n2. Usuarios \n3. Préstamos \n4. Mantenimiento \n0. Salir \nOpción: "))
    if op == 1:
        opL = int(input("\n\n1. Alta \n2. Mostrar \n3. Modificación \n4. Baja \n5. Menú \nOpción: "))
        if opL == 1:
            alta_libro()
        if opL == 2:
            print(libros)
        if opL == 3:
            print(libros)
            opLc = input("Digite el código del libro que desea modificar: ")
            opLm = int(input("¿Qué atributo del libro desea modificar?: \n\n1. Nombre \n2. Autor \n3. Género \n4. Cantidad \n5. Volver \nOpción: "))
            modifica_libro(opLc, opLm)
        if opL == 4:
            baja_libro()
        if opL == 5:
            menu()
        return opL
    if op == 2:
        opU = int(input("\n\n1. Alta \n2. Mostrar \n3. Modificación \n4. Baja \n5. Menú \nOpción: "))
        if opU == 1:
            alta_usuario()
        if opU == 2:
            print(usuarios)
        if opU == 3:
            print(usuarios)
            opUc = input("Digite la cédula del usuario que desea modificar: ")
            opUm = int(input("¿Qué atributo del usuario desea modificar?: \n\n1. Nombre \n2. Teléfono \n3. Ciudad \n4. Volver \nOpción: "))
            modifica_usuario(opUc, opUm)          
        if opU == 4:
            baja_usuario()
        if opU == 5:
            menu()
        return opU
    if op == 3:
        opP = int(input("\n\n1. Realizar nuevo préstamo \n2. Registrar devolución de libro \n3. Agregar solicitud a la lista de espera \n4. Notificar al siguiente en lista \n5. Menú \nOpción: "))
        if opP == 1:
            aux = realizar_prestamo()
            if aux != None:
                prestamos.append(aux)
            print(len(prestamos), prestamos)
        if opP == 2:
            registrar_devolucion()
        if opP == 5:
            menu()
        return opP
    if op == 4:
        opM = int(input("\n\n1. Agregar libro a la pila de reparación \n2. Dar de alta libro reparado \n3. Consultar próximo libro a reparar \n4. Menú \nOpción: "))
        if opM == 1:
            aux = agregar_reparacion()
            if aux != None:
                mantenimiento.append(aux)
            print(len(mantenimiento), mantenimiento)
        if opM == 2:
            reparar_libro()
            print(len(mantenimiento), mantenimiento)
        if opM == 3:
            print(mantenimiento[-1])
        if opM == 4:
            menu()
        return opM
    return op

def inicio():
    while menu() != 0 :
        pass
    print("Fin.... nos vemos mañana")

inicio()