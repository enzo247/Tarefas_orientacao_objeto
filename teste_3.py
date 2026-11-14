class produtos:
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = preco

    def mostrar_preco(self):
        return (f' O nome do produto e {self.nome} é o preço do produto e {self.__preco}')

    def alterar_preco(self, novo_preco,):
        if novo_preco > 0:
            self.__preco = novo_preco
            print(f' O preço do {self.nome} atualizado e {self.__preco:.2f}')
        else:
            print(' O preço deve ser maior que 0 ')


produto = produtos('Mouse Gamer', 189)
print(produto.mostrar_preco())
produto.alterar_preco(130)
produto.alterar_preco(190)
print(produto.mostrar_preco())
