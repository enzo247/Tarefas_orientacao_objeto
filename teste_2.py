class lampada:
    def __init__(self):
        self.ligada = False

    def ligar(self):
        self.ligada = True
        print('A luz está ligada')

    def desligar(self):
        self.ligada = False
        print('A luz está desligada')

    def checar_luz(self):
        if self.ligada:
            print(' Status da luz e acessa')
        else:
            print(' Status da luz está desligada ')





minha_lampada = lampada()
minha_lampada.ligar()
minha_lampada.checar_luz()
minha_lampada.desligar()
minha_lampada.checar_luz()