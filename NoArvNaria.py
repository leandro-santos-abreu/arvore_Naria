import copy


class NoArvNaria:
    m = 2
    info = ""
    filhos = [None] * 2

    def __init__(self, info=None, m=m):
        self.info = info
        self.filhos = [None]*m

    def inicArvnaria(self):
        return NoArvNaria(None)

    def criaArvNaria(self, tipoAN):
        self.info = tipoAN

    def subArvNaria(self):
        if self.filhos.count(None) == self.m:
            return False
        else:
            return self.filhos


    def raizArvoreNaria(self):
        if self.info is not None:
            return self.info
        else:
            return False
