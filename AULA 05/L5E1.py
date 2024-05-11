class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2* (self.base + self.altura)

t_base = int(input('DIGITE A BASE DO RETANGULO: '))
t_altura = int (input('\nDIGITE A ALTURA DO RETANGULO: '))

testar_retangulo = Retangulo(t_base, t_altura)
print ('\nA ÁREA DO RETANGULO É: ', testar_retangulo.area())
print ('\nO PERIMETRO DO RETANGULO É: ', testar_retangulo.perimetro())