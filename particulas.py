from particula import Particula

# Administrador de Particulas

class Particulas:
    def __init__(self):
        self.__parti = [] # Lista
    
    def agregar_inicio(self, particula:Particula):
        self.__parti.insert(0, particula)

    def agregar_final(self, particula:Particula):
        self.__parti.append(particula)
    
    def mostrar(self):
        for particula in self.__parti:
            print(particula)

p01 = Particula(id="14", origen_x="2", origen_y="2", destino_x="4", destino_y="4", velocidad="100", red="12", green="54", blue="15", distancia="")
p02 = Particula("13", "2", "2", "4", "4", "101", "15", "16", "17", "")

particulas = Particulas()
particulas.agregar_inicio(p01)
particulas.agregar_final(p02)
particulas.agregar_inicio(p01)
particulas.mostrar()
