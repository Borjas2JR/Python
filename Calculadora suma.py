import sys
print("Esta es una calculadora comun y corriente")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def product(a, b):
    return a * b

def division(a, b):
    return a / b


op = input("Indica que deseas hacer!\n s) para sumar.\n r) para restar.\n m) para multiplicar.\n d) para dividir.\n t) si deseas obtener todos los resultados." )
a = int(input("Ingresa un valor numerico: "))
b = int(input("Ingresa otro valor numerico: "))

while True:
    if op == "s":
        print("El resultado de la suma es:", suma(a, b))
        sys.exit(0)
    elif op == "r":
        print("El resultado de la resta es:", resta(a, b))
        sys.exit(0)
    elif op == "m":
        print("El resultado de la multiplicacion es:", product(a, b))
        sys.exit(0)
    elif op == "d":
        if b != 0:
            print("El resultado de la division se:", division(a, b))
            sys.exit(0)
        else: 
            print("No se puede dividir entre 0.")
            b = int(input("Ingresaa un valor diferente de 0: "))
    elif op == "t":
        print("El resultado de la suma es:", suma(a, b))
        print("El resultado de la resta es:", resta(a, b))
        print("El resultado de la multiplicacion es:", product(a, b))
        while True:
            if b != 0:
                print("El resultado de la division se:", division(a, b))
                sys.exit(0)
            else:
                print("No se puede dividir entre 0")
                b = int(input("Ingresa un valor diferente de 0: "))
                continue
    else: 
        print("Opcion no valida")
        sys.exit(1)

