import random

def Ordenamiento_de_burbuja(lista,pasos = 0):
    n = len(lista)

    for i in range(n):
        for j in range(0,n -1):
            pasos +=1
            if lista[j] > lista [j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista, pasos


if __name__ == '__main__':
    tamano_de_lista = int(input('Tamano de la lista: '))
        
    lista = [random.randint(0,100) for i in range(tamano_de_lista)]
    print(f'lista vieja: {lista}')
    (lista_ordenada, pasos) = Ordenamiento_de_burbuja(lista)
    print(f'nueva lista: {lista}')
    print(f'pasos: {pasos}')
