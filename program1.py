#1. Elabore un programa en Python que permita convertir de pesos a dólares, de
#pesos a euros, de euros a pesos, de pesos a yenes. (10 ptos)
#1 yen = 26.30 pesos
#1 dólar = 3944 pesos
#1 euro = 4279 pesos

def menu():
    try:
        print("""
            
            Cambio de divisas
            
            """)
        print('1. Pesos a Dólares\n2. Pesos a Euros \n3. Euros a Pesos \n4. Pesos a yenes') 
        opcion = int(input('>>')) #pide la opcion segun el menu
        match opcion:
            case 1: #en el caso 1 de pesos a dolares, ingresa el valor racional, 
                    #verifica si es positivo y lo divide entre 3944 que es el valor dado y lo imprime
                valor = float(input('Ingresa la cantidad de pesos para convertir a dólares \n>> '))
                if valor < 0:
                    print('Error, el valor no puede ser negativo')
                else:
                    convertido = valor/3944
                    redondeado = round(convertido, 3)
                    print(f'{valor} son {redondeado} dólares')
                    menu()
            case 2: #en el caso 2 de pesos a euros, ingresa el valor racional, 
                    #verifica si es positivo y lo divide entre 4279 que es el valor dado y lo imprime
                valor = float(input('Ingresa la cantidad de pesos para convertir a euros \n>> '))
                if valor < 0:
                    print('Error, el valor no puede ser negativo')
                else:
                    convertido = valor/4279
                    redondeado = round(convertido, 3)
                    print(f'{valor} son {redondeado} euros')
                    menu()
            case 3: #en el caso 3 de euros a pesos, ingresa el valor racional, 
                    #verifica si es positivo y lo multiplica entre 4279 que es el valor dado y lo imprime
                valor = float(input('Ingresa la cantidad de euros para convertir a pesos \n>> '))
                if valor < 0:
                    print('Error, el valor no puede ser negativo')
                else:
                    convertido = valor*4279
                    redondeado = round(convertido, 3)
                    print(f'{valor} son {redondeado} pesos')
                    menu()
            case 4: #en el caso 4 de pesos a yenes, ingresa el valor racional, 
                    #verifica si es positivo y lo divide entre 26.30 que es el valor dado y lo imprime
                valor = float(input('Ingresa la cantidad de pesos para convertir a yenes \n>> '))
                if valor < 0:
                    print('Error, el valor no puede ser negativo')
                else:
                    convertido = valor/26.30
                    redondeado = round(convertido, 3)
                    print(f'{valor} son {redondeado} yenes')
                    menu()
            case _: #si llega a dar un valor fuera de la lista, vuelve a llamar al menu
                print('La opcion ingresada no es valida: ')
                menu()
    except ValueError: #si el valor no es entero
        print('El valor ingresado no es un numero, intentelo de nuevo')
        menu()
    except EOFError:
        print('intentelo de nuevo')
        menu()
    except KeyboardInterrupt: #para salir del programa sin errores
        exit()
    
menu()