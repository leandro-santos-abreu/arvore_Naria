import copy


class NoArvNaria:
    m = 0 #Armazena o numero que indica a quantidade de filhos que a arvore vai ter
    info = None #Armazena o dado correspondende ao nó
    filhos = [None] * m #Cria o vetor de filhos com "None" baseado na quantidade de filhos que o usuario deseja
    raiz = None #Cria a Raiz

    def __init__(self, info=None, m=2): #Responsavel por inicializar a classe
        self.info = info
        self.filhos = [None] * m

    def inicArvnaria(self, m=2): #Metodo responsavel por inicializar uma arvore vazia e retornar a arvore criada, recebe a quantidade de filhos que o usuario deseja que cada arvore tenha (por defult e passado o valor 2)
        return NoArvNaria(None, m)

    def criaArvNaria(self, tipoAN): #Metodo responsavel por Criar a arvoreNaria com recebendo o valor que sera a raiz como parametro
        self.info = tipoAN

    def subArvNaria(self): #Metodo responsavel por retornar as subArvores da arvore
        return self.filhos

    def raizArvoreNaria(self): #Metodo responsavel por retornar a raiz da arvore
        if self.info is not None: # Verifica se a raiz possui valor
            return self.info
        else:
            return

    def vazioArvNaria(self): #Metodo responsavel por veriificar se a arvore esta vazia
        if self.info is None and len(self.filhos) == 0: #verifica se a arvore nao possui raiz nem subarvores
            return True
        else:
            return False

    def insereArvNaria(self, noFilho, noPai): #Metodo responsavel por inserir um no no inicio do array de subArvores
        subArvores = self.subArvNaria() #Chama o metodo que retorna as subArvores da arvore
        if self.info == noPai: # Verifica se o pai do no que sera adicionado e a raiz
            if subArvores.count(None) == 0: # Verifica se o array de subArvores esta cheio
                return False
            for f in range(len(subArvores)): # Faz um loop para percorrer todas as Subarvores
                index = self.filhos.index(None) # Pega o primeiro indice que esta vazio (None)
                if index == 0: # Verifica que a subArvore esta completamente vazia
                    self.filhos[index] = copy.deepcopy(noFilho) # Adiciona o no no array de subArvores da arvore pai
                    return True
                else:
                    for i in range(len(subArvores)-1, -1, -1): # Percorre o array de subArvores de tras para frente
                        self.filhos[i] = copy.deepcopy(self.filhos[i-1]) # Faz uma copia da subArvore de indice anterior para o indice atual, avancando todos em uma posicao
                    self.filhos[0] = copy.deepcopy(noFilho) #Seta o no que o usuario deseja inserir na primeira posicao do indice de subArvores da arvore
                    return True
        else:
            for f in self.filhos: # Percorre todos as subArvores
                if f is None: # Verifica se estao vazias
                    continue
                inserido = f.insereArvNaria(noFilho, noPai) # Chama novamente o metodo, dessa vez para a subArvore
                if inserido: #Verifica se o elemento foi inserido com sucesso
                    return True

    def adicionaArvNaria(self, noFilho, noPai): # Metodo responsavel por adicionar o no na ultima posicao do array de subArvores da arvore
        subArvores = self.subArvNaria() # Chama o metodo responsavel por retornar a subArvores
        if self.info == noPai: # verifica se o no pai e a raiz
            if subArvores.count(None) == 0: # Verifica se as subArvores estao cheias
                return False
            for f in range(len(subArvores) - 1, -1, -1): #Percorre o array de subArvores de forma inversa
                if self.filhos[f] is None: # Verifica se a o array de subArvores esta vazio (None)
                    self.filhos[f] = copy.deepcopy(noFilho) # Insere o no filho na posicao que esta vazia (None)
                    return True
                else:
                    for i in range(len(subArvores) - 1): # Percorre o array de subArvores
                        self.filhos[i] = copy.deepcopy(self.filhos[i+1]) # Faz uma copia da subArvore do proximo indice, retardando todos em uma posicao
                    self.filhos[len(subArvores)-1] = copy.deepcopy(noFilho) # Seta o novo no na ultima posicao do array de subArvores
                    return True
        else:
            for f in self.filhos: # Percorre todas as subArvores
                if f is None: # Verifica se a subArvore esta vazia (None)
                    continue
                adicionado = f.adicionaArvNaria(noFilho, noPai) # Chama a funcao de inserir novamente, dessa vez para a subArvore
                if adicionado: # Verifica se a adicao foi um sucesso
                    return True

    def elimSubArvNaria(self, i): # Metodo responsavel por eliminar uma subArvore
        filhos = self.subArvNaria() # Chama o metodo que retorna as subArvores
        for f in range(len(filhos)): # Verifica todos as subArvores
            if filhos[f] is None: # Verifica se a subArvore esta vazia (None)
                continue
            if filhos[f].info == i: # Verifica se o dado que deseja remover está no array de subArvores
                return self.filhos.pop(f) # Remove o no desejado do array de subArvores
            else:
                eliminado = filhos[f].elimSubArvNaria(i) # Chama o metodo novamente para a subArvore
                if eliminado: # verifica se foi eliminado com sucesso
                    return eliminado

    def destruirArvNaria(self): # Metodo responsavel por destruir a arvore
        i = 0
        while i < len(self.filhos): # Verifica se o no tem subArvores
            self.filhos.pop() # Remove as subArvores

        if len(self.filhos) == 0: # Verifica se nao ha subArvores
            return True
        else:
            return False

    def estaArvNaria(self, info): # Metodo responsavel por verificar se um elemento esta presente na arvore
        if self.info == info: # Verifica se o elemento e a raiz da arvore
            return True
        else:
            for x in self.filhos: # Verifica as subArvores
                if x is None: # Verifica se a subArvore e vazia (None)
                    continue
                elif x.info == info: # Verifica se a raiz da subArvore e o elemento procurado
                    return True

            for x in self.filhos: # Percorre as subArvores
                if x is None: # Verifica se a subArvore e vazia (None)
                    continue
                elif x.estaArvNaria(info): # Chama o metodo novamente para as subArvores
                    return True

            return False

    def imprime(self): # Metodo responsavel por imprimir a arvore
        print(str(self.info) + " -> ", end="") # Imprime a raiz da arvore
        for x in self.filhos: # Percorre as subArvores
            if x is None: # Verifica se a subArvore e vazia (None)
                continue
            print(str(x.info) + " , ", end="") # Imprime a raiz das subArvores
        print("")

        for x in self.filhos: # Verifica as subArvores
            if x is None: # Verifica se a subArvore e vazia (None)
                continue
            x.imprime() # Chama o metodo novamente para as subArvores
