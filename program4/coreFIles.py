# 4. Elabore un programa que permite registrar la información de los empleados
# De una compañía y le permita calcular el valor a pagar por concepto de nomina a
# Cada empleado. La información que se tiene por cada empleado es la siguiente (55ptos):

# id
# nombre
# cargo (Almacenista, Jefe IT, Administrador, Mensajero, Genrente)
# salario

# Para calcular el valor a pagar por cada empleado se debe tener en cuenta la
# Siguiente información:

# diasTrabajados
# horasExtras
# valorDia
# descuentoxCafeteria
# cuotaPrestamo

# El valor de la hora extra es de 5500 pesos. La información de la colilla de pago
# Se debe almacenar en caso de una solicitud de revisión por parte de algún
# Empleado que no este conforme con el pago la información que debe guardar
# La colilla de pago es la siguiente:

# mesPagado
# fechaPago(dd/mm/yyyy)
# sueldoBase
# valorTotalHrasExtras
# cuotaPrestamo
# descuentoxCafeteria
# totalAPagar

# La información se debe guardar en un archivo JSON.
# El gerente desea obtener la siguiente información:
# 1. Total pagado por concepto de nomina
# 2. Consultar la colilla de pago de un determinado empleado.
#goals = list(map(int, score.split("/"))) 
#valor dia: 43.000
import json
def writeJson(dict):
    with open('data.json', 'w') as w:
        w.write(json.dumps(dict, indent=4))
    
def readJson():
    with open('data.json', 'r') as r:
        return json.load(r)
    
diccionario = {}
blueprint = {
    'Empleados':{},
    'Calculo':{},
    'Colilla':{}
}
cargosLista = ['Almacenista', 'Jefe IT', 'Administrador', 'Mensajero', 'Genrente']

def menu():
    try:
        diccionario = readJson()
        if diccionario == {}:
            writeJson(blueprint)
        print("""
            
            Informacion de Empleados
            
            """)
        print('1. Añadir empleado \n2. Calcular sueldo de empleado \n3. Total pagado de empleado \n4. Consultar colilla de empleado ') 
        opcion = int(input('>> ')) #pide la opcion segun el menu
        match opcion:
            case 1: #prgeunta valor por valor para asignarlo a una variable
                    #asigna los valores con sus respectivas llaves segun la estructura dada y agrega el diccionario con id como llave
                hold = {}
                id = int(input('Identificacion: '))
                nombre = input('Nombre: ')
                for i in range(5):
                    print(f'{i+1}. {cargosLista[i]}')
                idCargo = int(input('Numero de cargo: '))
                cargo = cargosLista[idCargo - 1]
                salario = input('Salario: ')
                new = {
                    'Id':id,
                    'Nombres':nombre,
                    'Cargo':cargo,
                    'Salario':salario
                }
                hold[id] = new
                diccionario['Empleados'].update(hold)
                writeJson(diccionario) #guarda el archivo como 'data.json'
                menu()
            case 2: # pide id para poder asignar datos pidiendolos cada uno
                    # luego hace todos los calculos para poder asignar bien los valores
                holdCalc = {}
                holdQueue = {}
                id = input('Identificacion del empleado: ')
                if id in diccionario['Empleados'].keys():
                    dias = int(input('Dias trabajados (el mes es de 30 dias): '))
                    horas = int(input('Cuantas horas extra trabajo: '))
                    cafeteria = int(input('Cuanto debe en la cafeteria: '))
                    prestamo = int(input('Ingrese la cuota de prestamo que tiene deuda: '))
                    valorDia = (int(diccionario['Empleados'][id]['Salario']) / 30)
                    calc = {
                        'Dias':dias,
                        'Horas':horas,
                        'ValorDia':valorDia,
                        'Cafeteria':cafeteria,
                        'Prestamo':prestamo
                    }
                    calendario = input('Fecha de pago (dd/mm/yyyy): ')
                    fecha = list(map(int, calendario.split("/")))
                    fechaStr = str(fecha[0]) + '/' + str(fecha[1]) + '/' + str(fecha[2])
                    mes = fecha[1]
                    salario = valorDia * dias
                    totalHoras = horas * 5500
                    total = ((valorDia * dias) + totalHoras - (cafeteria + prestamo))
                    roundTotal = round(total,2)
                    queue = {
                        'MesPagado':mes,
                        'FechaPago':fechaStr,
                        'SalarioBase':salario,
                        'ValorHorasExtra':totalHoras,
                        'Prestamo':prestamo,
                        'Cafeteria':cafeteria,
                        'TotalPagar':roundTotal
                    }
                    holdCalc[id] = calc
                    holdQueue[id] = queue
                    diccionario['Calculo'].update(holdCalc)
                    diccionario['Colilla'].update(holdQueue)                    
                    writeJson(diccionario) #guarda el archivo como 'data.json'
                    menu()
                else:
                    print(f'El empleado con identificacion {id} no se encuentra')
                    menu()
            case 3: #verifica si hay un diccionario en 'Colilla' para tomar datos
                    #imprime el diccionario en formato JSON
                hold = {}
                id = input('Identificacion del empleado: ')
                if id in diccionario['Colilla']:
                    roundTotal = diccionario['Colilla'][id]['TotalPagar']
                    nombre = diccionario['Empleados'][id]['Nombres']
                    print(f'El total a pagar de el empleado {nombre} es {roundTotal}')
                    menu()
                elif diccionario['Colilla'] == {}:
                    print('no hay empleados con un calculo de sueldo')
                    menu()
                else:
                    print(f'El empleado con identificacion {id} no se encuentra')
                    menu()
            case 4: #verifica si hay un diccionario en 'Colilla' para imprimir el diccionario
                    #imprime el diccionario en formato JSON
                hold = {}
                id = input('Identificacion del empleado: ')
                if id in diccionario['Colilla']:
                    print(json.dumps(diccionario['Colilla'][id], indent=4))
                    menu()
                elif diccionario['Colilla'] == {}:
                    print('no hay empleados con un calculo de sueldo')
                    menu()
                else:
                    print(f'El empleado con identificacion {id} no se encuentra')
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
    except FileNotFoundError:
        writeJson(blueprint)
        menu()   
    except IndexError:
        print('La fecha esta mal ingresada')
        menu()
            
menu()