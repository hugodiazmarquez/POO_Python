import random

def busqueda_binaria(lista, comienzo, final, objetivo, pasos = 0):
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    pasos += 1
    if comienzo > final:
        return (False, pasos)

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return (True, pasos)
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo, pasos)
    else:
        return busqueda_binaria(lista, comienzo, medio -1, objetivo, pasos)


if __name__ == '__main__':
    tamano_de_lista = int(input('Tamano de la lista: '))
    objetivo = int(input('Numero que quieres encontrar: '))
        
    lista = sorted([random.randint(0,1000) for i in range(tamano_de_lista)])

    (encontrado, pasos) = busqueda_binaria(lista, 0, len(lista), objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"está" if encontrado else "no está"} en la lista ')
    print (pasos)