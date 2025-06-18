import random
print("Vamos a jugar \'Adivina la palabra\'")

palabras = {"desarrollador" : "Crea software", "python" : "Lenguage de programacion", "programador" : "Crea aplicaciones moviles", "informatica" : "Mundo digital", "tecnologia" : "Relacionado con la informatica",
             "internet" : "Conexion de red", "conexion" : "Comunicacion entre dos o mas ordenadores", "navegacion" : "Buscar en la web", "robotica" : "Maquinas autonomas"}
palabra = random.choice(list(palabras.keys()))          # Obtiene una palabra random de la lista
y = ["_"] * len(palabra)                                # Imprimir la cantidad de letras en '_'
pista = palabras[palabra]                               # Obtener la pista de la palabra
print(f"Comenzemos. \n La palabra que tienes que adivinar tiene {len(palabra)} letras.\n ", "La pista es: ", pista, '\n', " " .join(y))

counter = 0                                             # Contador de intentos 

while True:                                             # Ingreso al bucle
    letra = input("Ingresa una letra: ")                # Input del usuario
    letra = letra.lower()                               # Interpretarlas todas por minusculas 

    if len(letra) == 1 and letra.isalpha():             # Comprobar que se ha ingresado un caracter y que es una letra
        if letra in palabra:                            # Buscar la letra en la lista
            for i in range(len(palabra)):               # Iterar por cada letra
                if palabra[i] == letra:                 
                    y[i] = letra                        # Ingresar la letra en la posicion en que corresponde
            print("Bien hecho")
        else:
            counter += 1                                # Suma del contador si nos equivocamos de letra
            print(f"Letra incorrecta.\n Llevas {counter}\\3 intentos")
            
            if counter == 3:                            # Si el numero de intentos llega a 3, salir del bucle
                print("No haz acertado.\n Game Over")
                break
        print("El estado actual es:", " ".join(y))      # Mostrar el estado de la palabra
    else:
        print("Valor incorreco. Ingresa una letra.")

    if "_" not in y:
        print("Haz adivinado la palabra.\n Congragulations")        # Cuando la palabra este completa, salir del bucle con mensaje de felicitaciones
        break
