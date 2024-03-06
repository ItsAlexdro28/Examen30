# 3. Elabore un programa en Python que permita registrar los productos de una
# Tienda de viveres. La información se debe almacenar en un archivo JSON. La
# Información de los productos es la siguiente (20ptos):

# id
# nombre
# valorUnitario
# stockmin
# stockmax
# valorUnitario
import json

def writeJson(dict):
    with open('data.json', 'w') as w:
        json.dump(dict, w, indent=4)

diccionario = {}
def menu():
    try:
        print("""
            
            Informacion de Productos
            
            """)
        print('1. Añadir producto \n2. mostrar productos') 
        opcion = int(input('>> ')) #pide la opcion segun el menu
        match opcion:
            case 1: #prgeunta valor por valor para asignarlo a una variable
                    #asigna los valores con sus respectivas llaves segun la estructura dada y agrega el diccionario con id como llave
                hold = {}
                id = int(input('Identificacion: '))
                nombre = input('Nombre: ')
                valUnit = input('Valor Unitario: ')
                stockmin = input('Stock Minimo: ')
                stockmax = input('Stock Maximo: ')
                new = {
                    'Id':id,
                    'Nombres':nombre,
                    'ValorUnitario':valUnit,
                    'StockMinimo':stockmin,
                    'StockMaximo':stockmax,
                }
                hold[id] = new
                diccionario.update(hold)
                print(json.dumps(diccionario, indent=4))
                writeJson(diccionario) #guarda el archivo como 'data.json'
                menu()
            case 2: #imprime el diccionario en formato JSON
                print(json.dumps(diccionario, indent=4))
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