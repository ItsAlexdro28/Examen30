# 2. Elabore un programa en Python que permita leer la información de un usuario
# Y la almacene en un diccionario. La información del usuario es la siguiente(15 ptos):
#   id
#   nombres
#   apellidos
#   ubicación
#       dirección
#       ciudad
#       longitud
#       latitud
#   email
#   edad
#   ocupación
diccionario = {}
def menu():
    try:
        print("""
            
            Informacion de usuarios
            
            """)
        print('1. Añadir persona \n2. mostrar diccionario') 
        opcion = int(input('>> ')) #pide la opcion segun el menu
        match opcion:
            case 1: #prgeunta valor por valor para asignarlo a una variable
                    #asigna los valores con sus respectivas llaves segun la estructura dada y agrega el diccionario con id como llave
                hold = {}
                id = int(input('Identificacion: '))
                nombres = input('Nombres: ')
                apellidos = input('Apellidos: ')
                dir = input('Dirrección: ')
                ciudad = input('Ciudad: ')
                long = input('Longitud: ')
                lat = input('Latitud: ')
                email = input('Email: ')
                edad = int(input('Edad: '))
                ocupacion = input('Ocupacion: ')
                new = {
                    'Id':id,
                    'Nombres':nombres,
                    'Apellidos':apellidos,
                    'Ubicación':{
                        'dirección':dir,
                        'ciudad':ciudad,
                        'longitud':long,
                        'latitud':lat,
                    },
                    'email':email,
                    'edad':edad,
                    'ocupación':ocupacion
                }
                hold[id] = new
                diccionario.update(hold)
                print(diccionario)
                menu()
            case 2: #imprime el diccionario
                print(diccionario)
                menu()
            case _: #si llega a dar un valor fuera de la lista, vuelve a llamar al menu
                print('La opcion ingresada no es valida: ')
                menu()
    except ValueError: #si el valor no es entero
        print('El valor ingresado no aplica, intentelo de nuevo')
        menu()
    except EOFError:
        print('intentelo de nuevo')
        menu()
    except KeyboardInterrupt: #para salir del programa sin errores
        exit()
menu()
    