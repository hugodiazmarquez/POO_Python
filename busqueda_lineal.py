import random

def busqueda_lineal(lista, objetivo, pasos= 0):
   
    match = False
    for elemento in lista: #O(n)
        pasos += 1
        if elemento == objetivo:
            match = True
            break
    
    return (match, pasos)

if __name__ == '__main__':
    tamano_de_lista = int(input('Tamano de la lista: '))
    objetivo = int(input('Numero que quieres encontrar: '))
        
    lista = [random.randint(0,100) for i in range(tamano_de_lista)]

    (encontrado, pasos) = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"está" if encontrado else "no está"} en la lista ')
    print(f'Total de pasos: {pasos}')
    