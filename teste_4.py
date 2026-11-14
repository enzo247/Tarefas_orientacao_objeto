class funcionario:
    def __init__(self, nome, salario):
        self.nome = nome;
        self.salario = salario;

    def calcular_bonus(self):
        return (self.salario * 0.10)

    def salario_total(self):
        return (self.salario + self.calcular_bonus())

class gerente(funcionario):
    def calcular_bonus(self):
        return (self.salario * 0.20)


fun1 = funcionario(' Roberto ', 1500)
ger1= gerente(' Maycon', 2500)

#print(f' O funcionario {fun1.nome}: recebeu um bonus de R${fun1.calcular_bonus():.2f} a mais do seu salario {fun1.salario:.2f}')
#print(f' O gerente {ger1.nome}: recebeu um bonus de R${ger1.calcular_bonus():.2f} a mais do seu salario {ger1.salario:.2f}')

print(f' O {fun1.nome} vai receber no total {fun1.salario_total():.2f}')
print(f' O {ger1.nome} vai receber no total {ger1.salario_total():.2f}')