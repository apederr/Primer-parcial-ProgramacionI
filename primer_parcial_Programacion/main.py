from funciones import *


# #el usuario ingresa una cadena de digitos
# cadena = input("Ingresa una cadena de digitos alfanumerica: ")

# #valida que sea alfanumerica
# if validar_alfanumerico(cadena):
#     print("La cadena es valida")
# else:
#     print("La cadena no es valida")


#MENU DE OPCIONES
def menu_opciones():
    print("---------------------")
    print("Menu de opciones:")
    print("1. Generar lista de numeros aleatorios")
    print("2. Ordenar la lista de numeros")
    print("3. Cantidad de numeros en un rango de la lista")
    print("4. El numero maximo y minimo que se encuentren dentro del rango")
    print("5. Generar la matriz de caracteres alfanumericos")
    print("6. Salir del menu")
    print("---------------------")


def main():
    lista_aleatoria = [] #inicializa lista
    bandera_menu = True
    bandera_lista = False

    while bandera_menu == True:
        menu_opciones()
        opcion = int(input("Seleciona una opcion del menu: "))

        if opcion == 1:
            #genera lista aleatoria y la muestra
            lista_aleatoria = generar_lista_aleatoria()
            print(f"Tu lista aletoria de numeros: {lista_aleatoria}")
            bandera_lista = True

        elif opcion == 2:
            #verifica primero que la lista no este vacia
            if bandera_lista == False:
                print("MENSAJE: Por favor, primero debe generar la lista de numeros con la Opcion 1")
            else:
                #pide el criterio de ordenamiento
                orden = input("Indica el criterio de ordenamiento(ASC o DESC): ")
                #ordena la lista y la muestra
                lista_ordenada = ordenar_lista(lista_aleatoria,orden)
                print(f"Te muestro la lista ordenada: {lista_ordenada}")

        elif opcion == 3:
            #verifica primero que la lista no este vacia
            if bandera_lista == False:
                print("MENSAJE: Por favor, primero debe generar la lista de numeros con la Opcion 1")
            else:
                #pide el rango para buscar
                valor_inicial = int(input("Ingrese el rango inferior: "))
                valor_final = int(input("Ingrese el rango superior: "))

                #cuenta los numeros en el rango los muestra
                cantidad_rango = contar_numeros_rango(lista_aleatoria,valor_inicial,valor_final)
                print(f"CANTIDAD DE NÚMEROS EN EL RANGO [{valor_inicial} - {valor_final}]: {cantidad_rango}")
        
        elif opcion == 4:
            #verifica primero que la lista no este vacia
            if bandera_lista == False:
                print("MENSAJE: Por favor, primero debe generar la lista de numeros con la Opcion 1")
            elif valor_inicial == None and valor_final == None:
                print("ERROR! Antes debe ingresar la Opcion 3 y definir Valor inicial y final")

            else:
                #devuelve el numero maximo y minimo del rango en la lista
                num_minimo, num_maximo = obtener_max_min_del_rango(lista_aleatoria,valor_inicial,valor_final)
                print(f"Numero minimo: {num_minimo}")
                print(f"Numero maximo: {num_maximo}")

        elif opcion == 6:
                #Salida del menu
                bandera_menu = False
                print("Saliendo del menu..")


#ejecuta el menu de opciones
main()



