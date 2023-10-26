import math

class Ponto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def distancia(self, outro_ponto):
        deltaX = self.x - outro_ponto.x
        deltaY = self.y - outro_ponto.y
        distancia = math.sqrt( ((deltaX ** 2) + (deltaY ** 2)) )

        return distancia


ponto1 = Ponto(1, 1)
ponto2 = Ponto(1, 5)

distancia = ponto1.distancia(ponto2)

print("A distância entre o ponto1 e ponto2 é: {}".format(distancia))
