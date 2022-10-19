from particula import Particula
class Particulas:
    def __init__(self):
        self.__particulas = []
    
    def agregar_inicio(self,particula:Particula):
        self.__particulas.insert(0,particula)

    def agregar_final(self,particula:Particula):
        self.__particulas.append(particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

    def __str__(self):
        return "".join(
            str(particula) + '\n' for particula in self.__particulas
        )
#p= Particula(1,2,1,3,4,5,6,7,8,9)
#p1= Particula(20,69,59,41,55,66,99,80,52,63)
#p2= Particula(2,69,50,200,55,66,100,80,52,63)
#particulas=Particulas()
#particulas.agregar_inicio(p2)
#particulas.mostrar()
#particulas.agregar_final(p)
#particulas.mostrar()
##particulas.agregar_inicio(p1)
#particulas.mostrar()