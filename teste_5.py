class contaDigital:
    def __init__(self, nome, saldo=0):
        self.nome = nome
        self.__saldo = saldo

    def depositar_valor(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f' deposito de {valor:.2f} realizado com sucesso, novo saldo: {self.__saldo:.2f} ')
        else:
            print('Erro: saldo não pode ser negativo para realizar um deposito, Por favor inserir um valor valido!')


    def sacar_valor(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            print(f' Saque de {valor:.2f} realizado com sucesso, novo saldo: {self.__saldo:.2f}')

    def consultar_saldo(self):
        return f'Titular: {self.nome}, Saldo Atual: {self.__saldo:.2f}'

conta = contaDigital('Enzo')
print(conta.consultar_saldo())

conta.depositar_valor(500)
conta.sacar_valor(400)
print(conta.consultar_saldo())