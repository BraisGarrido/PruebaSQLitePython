from Paquete6 import menu

def mostrar_opciones():
    valor=True
    while(valor==True):
        print('Bienvenido al menú de opciones')
        print('(1)Crear base de datos')
        print('(2)Crear una categoría')
        print('(3)Introducir plato')
        print('(4)Ver menú')
        print('(5)Salir')
        eleccion=int(input('Escoge una de las opciones: '))
        if(eleccion==1):
            menu.crear_bd()
        elif(eleccion==2):
            menu.agregar_categoria()
        elif(eleccion==3):
            menu.agregar_plato()
        elif(eleccion==4):
            menu.mostrar_menu()
        elif(eleccion==5):
            valor=False
        else:
            print('Por favor escoge una opcion válida')  
    else:
        print('Has salido de la aplicación')
mostrar_opciones()