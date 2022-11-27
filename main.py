import copy

from NoArvNaria import NoArvNaria

if __name__ == '__main__':
    def vazioArvNaria(arvNaria): #Funcionando
        if arvNaria.info is None and arvNaria.filhos.count(None) == arvNaria.m:
            return True
        else:
            return False


    def insereArvNaria(arvNariaPai, arvNariaFilho): #Funcionando
        if vazioArvNaria(arvNariaPai) or vazioArvNaria(arvNariaFilho):
            print("Uma das Arvores é inválida")
        else:
            if arvNariaPai.filhos.count(None) == 0:
                subArvoresPai = arvNariaPai.subArvNaria()
                for i in range(len(subArvoresPai)):
                    if subArvoresPai[i].filhos.count(None) == arvNariaPai.m - i:
                        insereArvNaria(subArvoresPai[i], arvNariaFilho)
                        break
            else:
                arvNariaFilho.filhos
                index = arvNariaPai.filhos.index(None)
                if index == 0:
                    arvNariaPai.filhos[index] = copy.deepcopy(arvNariaFilho)
                else:
                    for i in range(index):
                        arvNariaPai.filhos[i+1] = copy.deepcopy(arvNariaPai.filhos[i])
                    arvNariaPai.filhos[0] = copy.deepcopy(arvNariaFilho)


    def adicionaArvNaria(arvNariaPai, arvNariaFilho): #Funcionando
        if vazioArvNaria(arvNariaPai) or vazioArvNaria(arvNariaFilho):
            print("Uma das Arvores é inválida")
        else:
            if arvNariaPai.filhos.count(None) == 0:
                subArvoresPai = arvNariaPai.subArvNaria()
                for i in range(len(subArvoresPai)):
                    if subArvoresPai[i].filhos.count(None) == arvNariaPai.m - i:
                        adicionaArvNaria(subArvoresPai[i], arvNariaFilho)
                        break
            else:
                index = arvNariaPai.filhos.index(None)
                arvNariaPai.filhos[index] = arvNariaFilho

    def elimSubArvNaria(arvNaria, i):
        if vazioArvNaria(arvNaria):
            return "Arvore Invalida"
        else:
            for i in range(i+1, i+1):
                arvNaria = arvNaria.subArvNaria()
                arvoresDesassociadas.append(arvNaria.filhos.pop())


    def destruirArvNaria(arvNaria):
        arvNaria = None

    def estaArvNaria(arvNaria, elem): #Funcionando
        if arvNaria.info == elem:
            return True
        else:
            subArvores = copy.deepcopy(arvNaria.subArvNaria())
            if subArvores == False:
                return False
            else:
                for a in subArvores:
                    existe = estaArvNaria(a, elem)
                    return existe



    def imprime(arvNaria):
        print(arvNaria.info)
        filhos = arvNaria.subArvNaria()
        if filhos:
            for f in filhos:
                imprime(f)


    print("Bem Vindo ao Simulador de Arvore N-aria")
    raiz = input("Insira o Valor a ser a Raíz da Arvore: ")
    insercoes = input("Como Deseja Lidar com Inserções? \n1 - Início da Lista de Filhos \n2 - Fim da Lista de Filhos")
    arvoresDesassociadas = []
    escolha = -1

    arvoreNaria = NoArvNaria().inicArvnaria()

    arvoreNaria.info = raiz

    while escolha != 0:
        print("Escolha um dos Comandos Abaixo para Prosseguir: ")
        escolha = input("1 - Inserir Nó \n2 - Remover Nó \n3 - Apagar Arvore \n4 - Imprimir Arvore \n5 - Buscar na Arvore \n0 - Sair \nEscolha:")

        if escolha == "1":
            elem = input("\nDigite o Valor a Ser Inserido na Arvore: ")
            no = NoArvNaria(elem)
            if (insercoes == "1"):
                insereArvNaria(arvoreNaria, no)
            else:
                adicionaArvNaria(arvoreNaria, no)
            print("\n", elem, "incluído com sucesso")
        elif escolha == "2":
            i = input("Digite o Número da I-Ésima Subarvore que Deseja Apagar: ")
            elem = elimSubArvNaria(arvoreNaria, i)
            print("\nNó contendo o valor ", elem, " apagado")
        elif escolha == "3":
            destruirArvNaria(arvoreNaria)
        elif escolha == "4":
            imprime(arvoreNaria)
        elif escolha == "5":
            i = input("Digite o Elemento que Deseja Buscar: ")
            existe = estaArvNaria(arvoreNaria, i)
            if existe:
                print("Elemente Existe na Árvore\n")
            else:
                print("Elemento Não Existe na Árvore\n")
        elif escolha == "0":
            print("\nSaindo...")
            break
