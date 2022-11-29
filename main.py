import copy

from NoArvNaria import NoArvNaria

if __name__ == '__main__':

    print("Bem Vindo ao Simulador de Arvore N-aria")
    tamanhoFilhos = int(input("Insira o Tamanho Máximo de Filhos em um Nó: ")) #Armazena a quanitdade de nós filhos que o usuário deseja ter na subArvore
    raiz = input("Insira o Valor a ser a Raíz da Arvore: ") #Armazena o valor da raiz da arvore
    insercoes = input(
        "\nComo Deseja Lidar com Inserções? \n1 - Início da Lista de Filhos \n2 - Fim da Lista de Filhos \nEscolha: ")
    arvoresDesassociadas = [] #Armazena as subArvores que foram "eliminadas"
    escolha = -1 #Inicia a variavel escolha

    arvoreNaria = NoArvNaria().inicArvnaria(tamanhoFilhos) #Inicia a arvoreNaria recebendo como parametro o numero de nós filhos que o usuário deseja

    arvoreNaria.info = raiz # seta a raiz da arvore
    arvoreNaria.m = tamanhoFilhos # seta o tamanho de filhos da arvore

    while escolha != 0 and arvoreNaria is not None:
        print("\nEscolha um dos Comandos Abaixo para Prosseguir: ")
        escolha = input(
            "\n1 - Inserir Nó \n2 - Remover Nó \n3 - Apagar Arvore \n4 - Imprimir Arvore \n5 - Buscar na Arvore \n0 - Sair \nEscolha: ")

        if escolha == "1":
            elem = input("\nDigite o Valor a Ser Inserido na Arvore: ")
            noFilho = NoArvNaria(elem, tamanhoFilhos) #cria o nó filho
            noPai = input("Digite o Nó Pai a ser Associado ao Valor Anterior: ") # armazena qual o pai do nó que será inserido
            noFilho.raiz = noPai # seta o nó pai como saiz do nó filho
            if (insercoes == "2"): # verifica se o usuário optou por adicionar os nós no final do vetor de filhos
                resultado = arvoreNaria.adicionaArvNaria(noFilho, noPai) # Adiciona o no filho no final do vetor de filhos do no pai
            else:
                resultado = arvoreNaria.insereArvNaria(noFilho, noPai) # Adiciona o no filho no inicio do vetor de filhos do no pai
            if resultado: # Verifica se a insercao deu certo
                print(elem, "incluído com sucesso")
            else:
                print("\nSubarvore Pai Já Está Cheia ou Nó Pai Inválido")
        elif escolha == "2":
            no = input("\nDigite a Subarvore que Deseja Remover: ") #Armazena o valor do nó da subArvore que o usuario quer remover
            if arvoreNaria.info == no: #Verifica se o no e a raiz
                arvoreNaria = None #Seta a arvore como None
                eliminado = True #Seta a variavel eliminado como true
            else:
                eliminado = arvoreNaria.elimSubArvNaria(no) #Chama o metodo responsavel por eliminar a subArvore passando o no desejado como parametro
                arvoresDesassociadas.append(eliminado) #Inclui a subArvore que foi eliminada no vetor que armazena subArvores "eliminadas"
            if eliminado: # Verifica se a subArvore foi eliminada com sucesso
                print("\nNo removido com sucesso")
                if arvoreNaria is None: #Verifica se a arvore esta vazia
                    print("\nArvore Naria Destruída.\nEncerrando o Programa...")
                    break
        elif escolha == "3":
            print("Arvore Naria Destruída.\nEncerrando o Programa...")
            arvoreNaria.destruirArvNaria() #Chama o metodo responsavel por destruir a arvore
            break
        elif escolha == "4":
            arvoreNaria.imprime() #Chama o metodo responsavel por imprimir a arvore
        elif escolha == "5":
            no = input("\nDigite o Nó a ser Verificado: ") #Armazena o valor do no que o usuario deseja pesquisar
            busca = arvoreNaria.estaArvNaria(no) #Chama a funcao que verifica se o elemento esta na arvore passando o valor do no que o usuario deseja buscar como parametro

            if busca: #Verifica se o no foi encontrado
                print("Elemento Está Contino na Árvore")
            else:
                print("Elemento Não Está Contino na Árvore")
        elif escolha == "0":
            print("\nSaindo...")
            break
