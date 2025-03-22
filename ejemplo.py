# Funciones básicas de la calculadora
def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Error: No se puede dividir por cero"
    else:
        return x / y

def potencia(x, y):
    return x ** y

# Función para mostrar el menú
def mostrar_menu():
    print("\nSelecciona una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Salir")

# Función principal de la calculadora
def calculadora():
    while True:
        mostrar_menu()
        
        # Obtener la operación del usuario
        operacion = input("Ingresa el número de la operación (1/2/3/4/5/6): ")
        
        if operacion == '6':
            print("¡Gracias por usar la calculadora! ¡Hasta luego!")
            break
        
        # Verificar que la operación seleccionada sea válida
        if operacion not in ['1', '2', '3', '4', '5']:
            print("Opción no válida. Por favor elige una opción entre 1 y 5.")
            continue
        
        # Obtener los números para la operación
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Por favor ingresa valores numéricos válidos.")
            continue
        
        # Realizar la operación seleccionada
        if operacion == '1':
            print(f"{num1} + {num2} = {sumar(num1, num2)}")
        elif operacion == '2':
            print(f"{num1} - {num2} = {restar(num1, num2)}")
        elif operacion == '3':
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
        elif operacion == '4':
            print(f"{num1} / {num2} = {dividir(num1, num2)}")
        elif operacion == '5':
            print(f"{num1} ^ {num2} = {potencia(num1, num2)}")
        
        # Preguntar si el usuario quiere hacer otro cálculo
        continuar = input("\n¿Quieres realizar otro cálculo? (s/n): ")
        if continuar.lower() != 's':
            print("¡Gracias por usar la calculadora! ¡Hasta luego!")
            break

# Ejecutar la calculadora
calculadora()
