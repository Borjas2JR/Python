
print("Esta en una agenda para guardar o buscar numeros telefonicos")

agenda = {
    "Ricardo" : "123 123 123", 
    "Josselin" : "111 222 333", 
    "Kelyn" : "444 555 666"
}

def guardar_contacto(agenda, nombre="Anonimo", numero="000 000 000"):
    name = input("Ingresa el nombre: ")
    number = input("Ingresa el telefono: ")

    if name not in agenda:   # Verificar si el nombre existe en la agenda
        if name != "" and number != "":   # Verificar que los inputs no sean cadenas vacias
            if name in agenda and agenda[name] == number:    #Verificar si el nombre y numero ya estan guardados
                print("El conctacto ya esta guardado")
            else:
                agenda[name] = number   # Guardar el contacto
                print("Se guardo el contacto: ", name,":", number)
        elif name == "" and number == "":   #  Si los inputs son cadenas vacias, guardar un contacto por defecto
            agenda[nombre] = numero
            print("Se guardo el contacto: ", nombre,":", numero)
        else: 
            print("Los valores ingresados no son correctos." )  
    else:
        print("Ya existe un contacto con el mismo nombre.")

def buscar_contacto(agenda):
    name1 = input("Que contacto deseas buscar: ")

    if name1 in agenda.keys():  # Verificar si el contacto esta guardado
        print("El contacto es: ", name1, agenda[name1])
    else:
        print("El contacto no se encuentra registrado.")

def contact_del(agenda):
    name_del = input("Ingrese el nombre del contacto que desea eliminar: ")

    if name_del in agenda:   # Verificar que el contacto esta gaurdado para eliminarlo
        del agenda[name_del]
    else:
        print("El contacto que desea elimiar no existe.")


while True:
    enter = input("Que desea a hacer?\n b/buscar un contacto.\n g/guardar un contacto.\n d/para eliminar un contacto: ")
  
    if enter == "b":    
        buscar_contacto(agenda)
        break
    elif enter == "g":
        guardar_contacto(agenda)
        break
    elif enter == "d":
        contact_del(agenda)
        break
