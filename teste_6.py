class item:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco

class carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_items(self, item):
        self.itens.append(item)

    def calcular_total(self):
        total = 0
        for i in self.itens:
            total += i._preco
        return total

item1 = item('camisa', 99)
item2 = item('sapato', 299)
meu_carrinho = carrinho()
meu_carrinho.adicionar_items(item1)
meu_carrinho.adicionar_items(item2)

print(f' Os itens do carrinho são: {item1.nome} e {item2.nome} \n e o valor unitário de cada item e R${item1._preco:.2f} e R${item2._preco:.2f}\n total da compra é R${meu_carrinho.calcular_total():.2f}')
