import copy


class NoArvNaria:
    m = 0
    info = None
    filhos = [None] * 2
    raiz = None

    def __init__(self, info=None, m=2):
        self.info = info
        self.filhos = [None] * m

    def inicArvnaria(self):
        return NoArvNaria(None)

    def criaArvNaria(self, tipoAN):
        self.info = tipoAN

    def subArvNaria(self):
        return self.filhos

    def raizArvoreNaria(self):
        if self.info is not None:
            return self.info
        else:
            return

    def vazioArvNaria(self):
        if self.info is None and len(self.filhos) == 0:
            return True
        else:
            return False

    def insereArvNaria(self, noFilho, noPai):
        subArvores = self.subArvNaria()
        if self.info == noPai:
            if subArvores.count(None) == 0:
                return False
            for f in range(len(subArvores)):
                index = self.filhos.index(None)
                if index == 0:
                    self.filhos[index] = copy.deepcopy(noFilho)
                    return True
                else:
                    for i in range(index):
                        self.filhos[i + 1] = copy.deepcopy(self.filhos[i])
                    self.filhos[0] = copy.deepcopy(noFilho)
                    return True
        else:
            for f in self.filhos:
                if f is None:
                    continue
                inserido = f.insereArvNaria(noFilho, noPai)
                if inserido:
                    return True

    def adicionaArvNaria(self, noFilho, noPai):
        subArvores = self.subArvNaria()
        if self.info == noPai:
            if subArvores.count(None) == 0:
                return False
            for f in range(len(subArvores)-1, -1, -1):
                if self.filhos[f] is None:
                    self.filhos[f] = noFilho
                    return True
        else:
            for f in self.filhos:
                if f is None:
                    continue
                adicionado = f.adicionaArvNaria(noFilho, noPai)
                if adicionado:
                    return True

    def elimSubArvNaria(self, i):
        filhos = self.subArvNaria()
        for f in range(len(filhos)):
            if filhos[f] is None:
                continue
            if filhos[f].info == i:
                return self.filhos.pop(f)
            else:
                eliminado = filhos[f].elimSubArvNaria(i)
                if eliminado:
                    return eliminado


    def destruirArvNaria(self):
        i = 0
        while i < len(self.filhos):
            self.filhos.pop()

        if len(self.filhos) == 0:
            return True
        else:
            return False

    def estaArvNaria(self, info):
        if self.info == info:
            return True
        else:
            for x in self.filhos:
                if x is None:
                    continue
                elif x.info == info:
                    return True

            for x in self.filhos:
                if x is None:
                    continue
                elif x.estaArvNaria(info):
                    return True

            return False

    def imprime(self):
        print(str(self.info) + " -> ", end="")
        for x in self.filhos:
            if x is None:
                continue
            print(str(x.info) + " , ", end="")
        print("")

        for x in self.filhos:
            if x is None:
                continue
            x.imprime()
