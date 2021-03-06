#Primer programa

# Definicion

class <nombre_de_la_clase> (<super_clase>):
 
    def __init__(self, <params>):
        <expresion>

    def <nombre_del_metodo>(self,<params>):
        <expresion>









class Coordenadas:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self,otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return (x_diff + y_diff)**0.5

if __name__ == '__main__':
    coord_1= Coordenadas(3,2)
    coord_2= Coordenadas(9,8)

    print(coord_1.distancia(coord_2))