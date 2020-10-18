# Actividad 09 | 18/10/20 | Baeza Mendoza Raúl Alonso
from algoritmos import distancia_euclidiana

class Particula:
    def __init__(self, id=0, origen_x=0, origen_y=0, destino_x=0, destino_y=0, velocidad=0, red=0, green=0, blue=0, distancia=0):
        self.__id = id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = distancia_euclidiana(2, 2, 4, 4) # Raíz de 8 = 2.82
    
    def __str__(self):
        return (
            "id: " + str(self.__id) + "\n" +
            "Origen en x: " + str(self.__origen_x) + "\n" + 
            "Origen en y: " + str(self.__origen_y) + "\n" +
            "Destino en x: " + str(self.__destino_x) +  "\n" + 
            "Destino en y: " + str(self.__destino_y) + "\n" + 
            "Velocidad: " + str(self.__velocidad) + "\n" + 
            "red: " + str(self.__red) + "\n" + 
            "gren: " + str(self.__green) + "\n" +
            "blue: " + str(self.__blue) + "\n" + 
            "distancia: " + str(self.__distancia) + "\n"
        )

p01 = Particula(id="14", origen_x="2", origen_y="2", destino_x="4", destino_y="4", velocidad="100", red="12", green="54", blue="15", distancia="")
print(p01)
p02 = Particula("13", "2", "2", "4", "4", "101", "15", "16", "17", "")
print(p02)
