class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado,lado)

if __name__ == '__main__':
    
    Menu = """
    Selecciona la opcion deseada:
    1 - Area de rectangulo
    2 - Area de cuadrado

    """
    
    opcion = int(input(Menu))
    
    if opcion == 1:
        base = int(input("Introduce la base: "))
        altura = int(input("Introduce la altura: "))
        rectangulo = Rectangulo(base, altura)
        print(f'El area es {rectangulo.area()} unidades cuadradas')
    elif opcion == 2:
        lado = int(input("Introduce el valor del lado: "))
        cuadrado = Cuadrado(lado)
        print(cuadrado.area())
    else:
        print('Selecciona una opcion valida')