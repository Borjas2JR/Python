print("Esta en una agenda para guardar o buscar numeros telefonicos")

agenda = [
    ["Borjas", "Javi", "Kelyn"],
    ["123 456 789", "112 334 445", "556 667 778"]
]

def function_agendar(agenda):
    entrada = input("Ingresa el nombre: ")
    entrada2 = input("Ingresa el telefono:")

    if entrada != "":
        if entrada2 != "":
            agenda[0].append(entrada)
            agenda[1].append(entrada2)

def function_buscar(agenda):
    name1 = input("Que contacto deseas buscar?")

    if name1 in agenda[0]:
        index = agenda[0].index(name1)
        telefono = agenda[1][index]

        print("El contacto es: ", name1, "Telefono: ", telefono )

name = input("Que desea a hacer? b/buscar un contacto o g/guardar un contacto")

if name == "b":
    function_buscar(agenda)
elif name == "g":
    function_agendar
else:
    print("Ingresa un valor correcto")
    
