import random
print("Vamos a jugar \'Adivina la palabra\'")

palabras = ["desarrollador", "python", "programador", "informatica", "computacion", "tecnologia", "internet", "conexion", "navegacion"]
palabra = random.choice(palabras)           # Obtiene una palabra random de la lista

y = ["_"] * len(palabra)

print(f"Comenzemos. \n La palabra que tienes que adivinar tiene {len(palabra)} letras.\n ", " " .join(y))


counter = 0

while True: 
    letra = input("Ingresa una letra: ")      # Ingresar datos de usuario
    letra = letra.lower()
    
    if len(letra) == 1 and letra.isalpha():      # Comprobar si el dato introducido contiene un solo caracter y es una letra
        if letra in palabra:                     # Comprobar si [letra] esta en [palabra]
            for i in range(len(palabra)):        # Iterar cada letra de la palabra
                if palabra[i] == letra:          # Comprobar en que ubicacion las letras son iguales
                    y[i] = letra
            print("Bien hecho")
        else:
            print("Letra incorrecta")
            counter += 1                        # Contador de intentos fallidos, al 3er intento se cierra.
            if counter == 3:
                print("No haz acertado.\n Game Over")
                break
        print("El estado actual es:", " ".join(y))
    else:
        print("Valor incorreco. Ingresa una letra.")

    if "_" not in y:
        print("Haz adivinado la palabra.")
        break
