
import random

lista = [random.randint(0,100) for i in range(20)]
lista_ordenada = []

def orden_por_insercion(lista):

    for i in range(len(lista)):
        print(lista_ordenada) 
        if i != 0:

            for j in range(len(lista_ordenada)):

                if lista[i] <= lista_ordenada[j]:

                    lista_ordenada.insert(j, lista[i])
                    break

                elif j == len(lista_ordenada) - 1:

                    lista_ordenada.insert(j + 1, lista[i])

        else:

            lista_ordenada.insert(0,lista[0])
        
    return lista_ordenada


if __name__ == "__main__":

    print(lista)
    print(orden_por_insercion(lista))