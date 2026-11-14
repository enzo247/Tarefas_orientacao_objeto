class livro:
    def __init__(self, titulo, autor, paginas,):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def mostrar_paginas(self) -> str:
        return (f'O livro {self.titulo}, escrito por {self.autor} tem {self.paginas}')

livro_1 = livro('Diario de um Banana', 'Enzo Hayashi', 355)
livro_2 = livro('Crepusculo', 'Marvel', 666)


print(livro_1.mostrar_paginas())
print(livro_2.mostrar_paginas())