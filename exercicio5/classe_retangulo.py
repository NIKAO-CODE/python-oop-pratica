
class Retangulo:

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    
    def calcular_area(self):
        area = self.largura * self.altura

        return area
    
    def calcular_perimetro(self):
        perimetro = ( (2 * self.largura) + (2 * self.altura) )

        return perimetro
    

retangulo = Retangulo(8, 8)

print("A área do retângulo é {}cm²".format(retangulo.calcular_area()))
print("O perímetro do retângulo é {}cm".format(retangulo.calcular_perimetro()))
