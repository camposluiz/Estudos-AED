class AVL:
    def __init__(self):
        self.__raiz = None
        self.soma = 0

    class No:
        def __init__(self, pai, valor):
            self.pai = pai
            self.esquerda = None
            self.direita = None
            self.valor = valor
            self.altura = 1

        def __str__(self):
            return str(self.valor)

        def __repr__(self):
            return self.__str__()

    def minimo(self, atual=None):
        # se atual não tem valor inicial, começar da raiz
        if atual is None:
            atual = self.__raiz

        # enquanto houver um filho a esquerda, caminhar nessa direção
        while atual.esquerda is not None:
            atual = atual.esquerda

        # não tem mais filho a esquerda
        # então atual é o menor elemento da árvore
        return atual

    def maximo(self, atual=None):
        # se atual não tem valor inicial, começar da raiz
        if atual is None:
            atual = self.__raiz

        # enquanto houver um filho a direita, caminhar nessa direção
        while atual.direita is not None:
            atual = atual.direita

        # não tem mais filho a direita
        # então atual é o maior elemento da árvore
        return atual

    def buscar(self, valor):
        atual = self.__raiz

        # enquanto atual existir e o valor for diferente do desejado
        # ir descendo na árvore pela esquerda (se for menor)
        # ou pela direita (se for maior)
        while atual is not None and valor != atual.valor:
            if valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita

        # se encontrou, atual é o próprio nó
        # caso contrário, atual é None
        return atual

    def buscar_recursivo(self, valor):

        def recursao(atual, valor):

            # é igual ou nulo?
            if valor == atual.valor or atual is None:
                # se encontrou, atual é o próprio nó buscado
                # caso contrário, atual é None
                return atual

            if valor < atual.valor:
                # se o valor buscado for menor que o atual
                # buscar na sub-árvore da esquerda
                return recursao(atual.esquerda, valor)
            else:
                # se o valor buscado for maior que o atual
                # buscar na sub-árvore da direita
                return recursao(atual.direita, valor)

        return recursao(self.__raiz, valor)

    def inserir(self, valor):

        pai_atual = None
        atual = self.__raiz  # começando pela raiz
        novo = self.No(None, valor)  # criando o novo nó com o valor

        while atual is not None:
            pai_atual = atual

            if novo.valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita

        novo.pai = pai_atual
        self.soma += novo.valor

        if pai_atual is None:
            self.__raiz = novo
        elif novo.valor < pai_atual.valor:
            pai_atual.esquerda = novo
        else:
            pai_atual.direita = novo

        self.rebalanciar(novo)

    def rebalanciar(self, no):
        while no is not None:
            self.atualizarAltura(no)

            if self.getAltura(no.esquerda) >= 2 + self.getAltura(no.direita):
                # rotação a direita
                if self.getAltura(no.esquerda.esquerda) >= self.getAltura(no.esquerda.direita):
                    self.rotacaoDireita(no)
                # rotação dupla a direita
                else:
                    self.rotacaoEsquerda(no.esquerda)
                    self.rotacaoDireita(no)
            elif self.getAltura(no.direita) >= 2 + self.getAltura(no.esquerda):
                # rotação a esquerda
                if self.getAltura(no.direita.direita) >= self.getAltura(no.direita.esquerda):
                    self.rotacaoEsquerda(no)
                # rotação dupla a esquerda
                else:
                    self.rotacaoDireita(no.direita)
                    self.rotacaoEsquerda(no)

            no = no.pai


    def getAltura(self, no):
        if no is None:
            return -1
        return no.altura

    def atualizarAltura(self, no):
        no.altura = max(self.getAltura(no.esquerda), self.getAltura(no.direita)) + 1

    def rotacaoEsquerda(self, no):
        y = no.direita
        y.pai = no.pai

        if y.pai is None:
            self.__raiz = y
        else:
            if y.pai.esquerda is no:
                y.pai.esquerda = y
            elif y.pai.direita is no:
                y.pai.direita = y

        no.direita = y.esquerda
        if no.direita is not None:
            no.direita.pai = no

        y.esquerda = no
        no.pai = y

        self.atualizarAltura(no)
        self.atualizarAltura(y)

    def rotacaoDireita(self, no):

        y = no.esquerda
        y.pai = no.pai
        if y.pai is None:
            self.__raiz = y
        else:
            if y.pai.esquerda is no:
                y.pai.esquerda = y
            elif y.pai.direita is no:
                y.pai.direita = y

        no.esquerda = y.direita
        if no.esquerda is not None:
            no.esquerda.pai = no

        y.direita = no
        no.pai = y

        self.atualizarAltura(no)
        self.atualizarAltura(y)


    def sucessor(self, valor):
        atual = self.buscar(valor)

        # se o elemento não existe, não possui sucessor
        if atual is None:
            return atual

        if atual.direita is not None:
            # (é uma busca de cima pra baixo)
            return self.minimo(atual.direita)

        pai_atual = atual.pai

        while pai_atual is not None and atual == pai_atual.direita:
            atual = pai_atual
            pai_atual = pai_atual.pai

        # sem sucessor
        if pai_atual is None:
            return pai_atual

        # com sucessor
        return pai_atual

    def predecessor(self, valor):
        atual = self.buscar(valor)

        # se o elemento não existe, não possui predecessor
        if atual is None:
            return atual

        # se existir uma sub-árvore a esquerda
        # o predecessor será o elemento da extrema direita dessa sub-árvore
        if atual.esquerda is not None:
            # (é uma busca de cima pra baixo)
            return self.maximo(atual.esquerda)

        pai_atual = atual.pai

        while pai_atual is not None and atual == pai_atual.esquerda:
            # subindo um nível hierárquico por repetição
            atual = pai_atual
            pai_atual = pai_atual.pai

        # sem predecessor
        if pai_atual is None:
            return pai_atual

        # com predecessor
        return pai_atual

    def apagar(self, valor):
        sera_removido = self.buscar(valor)

        if sera_removido.esquerda is None:
            self.recortar(sera_removido, sera_removido.direita)
        elif sera_removido.direita is None:
            self.recortar(sera_removido, sera_removido.esquerda)
        else:
            sucessor = self.sucessor(sera_removido.valor)

            if sucessor.pai != sera_removido:
                self.recortar(sucessor, sucessor.direita)

                sucessor.direita = sera_removido.direita
                sucessor.direita.pai = sucessor

            self.recortar(sera_removido, sucessor)

            # a sub-árvore da esquerda do nó recortado será a que pertencia ao nó removido
            sucessor.esquerda = sera_removido.esquerda
            sucessor.esquerda.pai = sucessor

        self.rebalanciar(sera_removido.pai)

    # recorta um nó para o lugar do nó removido (o pai do recortado é atualizado)
    # o nó recortado não carrega os filhos
    def recortar(self, sera_removido, sera_recortado):
        if sera_removido.pai is None:
            # se o nó a ser removido não tiver pai, a raiz está sendo removida
            # o nó que será colocado no lugar será a nova raiz
            self.__raiz = sera_recortado
        elif sera_removido == sera_removido.pai.esquerda:
            # removendo um nó que é o filho a esquerda
            sera_removido.pai.esquerda = sera_recortado
        else:
            # removendo um nó que é o filho a direita
            sera_removido.pai.direita = sera_recortado

        if sera_recortado is not None:
            # o pai do que foi removido será pai agora do nó que foi para seu lugar
            sera_recortado.pai = sera_removido.pai

    def listar(self):
        # irá retornar uma lista ordenada
        lista = []

        def em_ordem(atual):
            if atual is not None:
                em_ordem(atual.esquerda)
                lista.append(atual.valor)  # cadastrando atual
                em_ordem(atual.direita)

        em_ordem(self.__raiz)

        return lista

    def preOrder(self, root):

        if not root:
            return

        print("{0} ".format(root.valor), end="")
        self.preOrder(root.esquerda)
        self.preOrder(root.direita)

    def getRaiz(self):
        return  self.__raiz

arvore = AVL()

# arvore.inserir(5)
# arvore.inserir(8)
# arvore.inserir(9)
# arvore.inserir(7)
# arvore.inserir(6)
# arvore.inserir(2)

arvore.inserir(10)
arvore.inserir(20)
arvore.inserir(30)
arvore.inserir(40)
arvore.inserir(50)
arvore.inserir(25)
a = arvore.getRaiz()
print(a.esquerda)