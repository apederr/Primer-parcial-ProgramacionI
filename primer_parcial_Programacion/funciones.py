import random 
#ENUNCIADO
#PUNTO 1
def generar_lista_aleatoria(tamaño=50,min=1,max=100):
    """
    Genera una lista de numeros enteros aleatorios
    """
    return [random.randint(min,max) for i in range(tamaño)]

#PUNTO 3
def ordenar_lista(lista, orden= "ASC"): #por defecto el orden es ascendente
    """
    Ordena una lista de numeros enteros
    """
    if orden.upper() == "ASC":
        return sorted(lista) 
    elif orden.upper() == "DESC":
        return sorted(lista, reverse=True)
    else: 
        return print("ERROR! el criterio debe ser ASC o DESC")#si pasan un criterio no existente tira error
    
#PUNTO 4 
def validar_alfanumerico(digitos):
    """
    Valida si una cadena de digitos es alfanumerica
    """
    return digitos.isalnum()
    
def contar_numeros_rango(lista, valor_inicial,valor_final)-> int: 
    """
    Cuenta la cantidad de numeros en el rango indicado de la lista
    """
    contador_numeros = 0

    for numero in lista:
        if valor_inicial <= numero <= valor_final:
            contador_numeros += 1 #suma si el numero esta en el rango

    return contador_numeros 

def obtener_max_min_del_rango(lista, valor_inicial, valor_final):
    """
    Saca el numero maximo y minimo de la lista
    """
    num_minimo = None 
    num_maximo = None

    for numero in lista:
        if valor_inicial <= numero <= valor_final:
            if num_minimo is None or numero < num_minimo:
                num_minimo = numero
            if num_maximo is None or numero > num_maximo:
                num_maximo = numero

    return num_minimo, num_maximo