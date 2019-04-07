# Función que muestra el Menú
def Menu():
    print("""************
CALCULADORA
************
Menú\n
(1) Suma
(2) Resta
(3) Multiplicación
(4) División
(5) Exponencial
(6) Salir\n""")

# Función para Calcular Operaciones Aritméticas
def Calculadora():
    Menu()
    try:
        opcion = int(input("Seleccione Opción\n"))
        # Bucle para valores fuera del rango de 1 a 6
        while (opcion <= 0 or opcion > 6):
            print("\nSeleccione del Menú una de las Opciones:\n * OPCIONES del (1) al (6) *\n")
            Menu()
            opcion = int(input("Seleccione Opción\n"))
        # Bucle para valores dentro del rango de 1 a 6
        # Las siguientes Condiciones se tiene en cuenta el 6 y se utiliza para apagar la Calculadora, y el 0 para continuar
        while (opcion >= 0 and opcion <= 6):
            if opcion == 6:
                print("__Apagando Calculadora__")
                break
            elif opcion == 0:
                print("\nSeleccione un número dentro de las OPCIONES del (1) al (6):\n")
                Menu()
                opcion = int(input("Seleccione Opción\n"))
                continue
            x = float(input("Ingrese Número\n"))
            y = float(input("Ingrese otro Número\n"))
            if opcion == 1:
                print("La Suma es:", x + y)
                opcion = int(input("Seleccione Opción\n"))
            elif opcion == 2:
                print("La Resta es:", x - y)
                opcion = int(input("Seleccione Opción\n"))
            elif opcion == 3:
                print("La Multiplicación es:", x * y)
                opcion = int(input("Seleccione Opción\n"))
            elif opcion == 4:
                try:
                    print("La División es:", x / y)
                    opcion = int(input("Seleccione Opción\n"))
                except ZeroDivisionError:
                    print("No se Permite la División Entre 0")
                    opcion = int(input("Seleccione Opción\n"))
            elif opcion == 5:
                print("La Exponencial es:", x ** y)
                opcion = int(input("Seleccione Opción\n"))
    except:
        print("\nSeleccione del Menú una de las Opciones:\n* OPCIONES del (1) al (6) *\n\n- NO se admiten Caracteres -\n- NO se admiten Números Decimales -\n")
        Calculadora()

Calculadora()