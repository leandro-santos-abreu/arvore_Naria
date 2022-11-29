import copy

from NoArvNaria import NoArvNaria

if __name__ == '__main__':

    print("Bem Vindo ao Simulador de Arvore N-aria")
    tamanhoFilhos = int(input("Insira o Tamanho Máximo de Filhos em um Nó: "))
    raiz = input("Insira o Valor a ser a Raíz da Arvore: ")
    insercoes = input(
        "\nComo Deseja Lidar com Inserções? \n1 - Início da Lista de Filhos \n2 - Fim da Lista de Filhos \nEscolha: ")
    arvoresDesassociadas = []
    escolha = -1

    arvoreNaria = NoArvNaria().inicArvnaria(tamanhoFilhos)

    arvoreNaria.info = raiz
    arvoreNaria.m = tamanhoFilhos

    while escolha != 0 and arvoreNaria is not None:
        print("\nEscolha um dos Comandos Abaixo para Prosseguir: ")
        escolha = input(
            "\n1 - Inserir Nó \n2 - Remover Nó \n3 - Apagar Arvore \n4 - Imprimir Arvore \n5 - Buscar na Arvore \n0 - Sair \nEscolha: ")

        if escolha == "1":
            elem = input("\nDigite o Valor a Ser Inserido na Arvore: ")
            noFilho = NoArvNaria(elem, tamanhoFilhos)
            noPai = input("Digite o Nó Pai a ser Associado ao Valor Anterior: ")
            noFilho.raiz = noPai
            if (insercoes == "2"):
                resultado = arvoreNaria.adicionaArvNaria(noFilho, noPai)
            else:
                resultado = arvoreNaria.insereArvNaria(noFilho, noPai)
            if resultado:
                print(elem, "incluído com sucesso")
            else:
                print("\nSubarvore Pai Já Está Cheia ou Nó Pai Inválido")
        elif escolha == "2":
            no = input("\nDigite a Subarvore que Deseja Remover: ")
            if arvoreNaria.info == no:
                arvoreNaria = None
                eliminado = True
            else:
                eliminado = arvoreNaria.elimSubArvNaria(no)
                arvoresDesassociadas.append(eliminado)
            if eliminado:
                print("\nNo removido com sucesso")
                if arvoreNaria is None:
                    print("\nArvore Naria Destruída.\nEncerrando o Programa...")
        elif escolha == "3":
            print("Arvore Naria Destruída.\nEncerrando o Programa...")
            arvoreNaria.destruirArvNaria()
            break
        elif escolha == "4":
            arvoreNaria.imprime()
        elif escolha == "5":
            no = input("\nDigite o Nó a ser Verificado: ")
            busca = arvoreNaria.estaArvNaria(no)

            if busca:
                print("Elemento Está Contino na Árvore")
            else:
                print("Elemento Não Está Contino na Árvore")
        elif escolha == "0":
            print("\nSaindo...")
            break
