print("Esta en una agenda para guardar o buscar numeros telefonicos")

agenda = {
    "Ricardo" : "632 123 123", 
    "Josselin" : "633 123 123", 
    "Kelyn" : "632 123 123"
}

def function_agendar(agenda):
    name = input("Ingresa el nombre: ")
    number = input("Ingresa el telefono:")

    if name != "" and number != "":
        agenda[name] = number
    else: 
        print("Ingrese un valor correcto" )
def function_buscar(agenda):
    name1 = input("Que contacto deseas buscar?")

    if name1 in agenda.keys():
        print("El contacto es: ", name1, agenda[name1])
    else:
        print("El contacto no se encuentra agendado")
        

while True:
    enter = input("Que desea a hacer? b/buscar un contacto o g/guardar un contacto: ")

    if enter == "b":    
        function_buscar(agenda)
        break
    elif enter == "g":
        function_agendar(agenda)
        break
    else:
        print("Ingresa un valor correcto")
        continue
