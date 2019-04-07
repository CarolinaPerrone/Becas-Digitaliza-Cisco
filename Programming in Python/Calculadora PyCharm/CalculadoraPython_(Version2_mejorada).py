# Funciones con las Operaciones Aritméticas

def suma(a,b):
    print("La Suma es:",a+b)

def resta(a,b):
    print("La Resta es:",a-b)

def multiplicacion(a,b):
    print("La Multiplicación es:",a*b)

def division(a,b):
    try:
        print("La División es:",a/b)
    except ZeroDivisionError:
        print("No se Permite la División Entre 0")

def exponencial(a,b):
    print("La Exponencial es:",a**b)

# Diccionario con las opciones posibles

op={1:suma,2:resta,3:multiplicacion,4:division,5:exponencial}

while True:
    print("\n---- Calculadora Python ----\n\n----------- MENU -----------\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Exponencial\n0. Exit\n----------------------------\n")
    try:
        menu = int(input("Seleccione Opción\n"))
        # Condición para valores fuera del rango de 1 a 5
        # La siguiente Condición se tiene en cuenta el 0 y se utiliza para apagar la Calculadora
        if menu < 0 or menu >= 6:
            print("\nSeleccione del Menú una de las Opciones:\n\n * OPCIONES del 1 al 5 - O bien Opción 0 para salir *\n")
            continue
        if menu == 0:
            print("\n#### Apagando Calculadora ####\n")
            break
        else:
            a = float(input("Ingrese un Número:\n"))
            b = float(input("Ingrese otro Número:\n"))
            op[menu](a,b)
    except:
        print("\nSeleccione del Menú una de las Opciones:\n\n * OPCIONES del 1 al 5 - O bien Opción 0 para salir * \n\n ---- No se admiten Caracteres ----")
