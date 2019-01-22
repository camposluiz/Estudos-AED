""" Luiz Antônio """

class BST:

    def __init__(self):
        self.__raiz = None

    class No:
        def __init__(self, valor):
            self.pai = None
            self.esquerda = None
            self.direita = None
            self.valor = valor

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        """ Recebe a lista com os elementos da árvore da função em_ordem() e imprimi-a na tela """

        elementos = self.em_ordem(self.__raiz)
        aux = '{'

        for i, elemento in enumerate(elementos):

            aux += elemento.__repr__()

            if i < len(elementos) - 1:
                aux += ', '

        aux += '}'

        return aux

    def em_ordem(self, atual=None, lista = None, visitou_raiz=False):
        """ Retorna uma lista com os elementos já na ordem correta
            Tem complexidade: Θ(n) """

        if not visitou_raiz:
            lista = []
            atual = self.__raiz
            visitou_raiz = True

        if atual is not None:
            self.em_ordem(atual.esquerda, lista, visitou_raiz)
            lista.append(atual.valor)
            self.em_ordem(atual.direita, lista, visitou_raiz)

        return lista

    def minimo(self, atual=None):
        """ Retorna o menor elemento presente na árvore
            Tem complexidade: O(h) sobre uma árvore de altura h """

        atual = self.__raiz

        while atual.esquerda is not None:
            atual = atual.direita

        return atual

    def maximo(self, atual=None):
        """ Retorna o maior elemento presente na árvore
            Tem complexidade: O(h) sobre uma árvore de altura h """

        atual = self.__raiz

        while atual.direita is not None:
            atual = atual.direita

        return atual

    def buscar(self, elemento, atual=None, visitou_raiz=False):
        """ Busca se um elemento está ou não presente na árvore
            Tem complexidade: O(h) sobre uma árvore de altura h """

        if not visitou_raiz:
            atual = self.__raiz
            visitou_raiz = True

        if atual is not None and elemento != atual.valor:  # Condição de existência
            if elemento < atual.valor:
                return self.buscar(elemento, atual.esquerda, visitou_raiz)
            else:
                return self.buscar(elemento, atual.direita, visitou_raiz)

        return atual

    def inserir(self, valor):
        """ Insere um elemento na árvore respeitando suas propriedades
            Tem complexidade: O(h) para uma árvore de altura h """

        pai_atual = None
        atual = self.__raiz

        novo = self.No(valor)

        while atual is not None:
            pai_atual = atual

            if novo.valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita

        novo.pai = pai_atual

        if pai_atual is None:
            self.__raiz = novo
        elif novo.valor < pai_atual.valor:
            pai_atual.esquerda = novo
        else:
            pai_atual.direita = novo

    def __delitem__(self, chave):

        """ Apaga e retorna o elemento que foi removido da árvore
            Tem complexidade: O(h) para uma árvore de altura h """

        remover = self.buscar(chave)  # Caso o elemento a ser removido exista

        if remover:
            if remover.esquerda is None or remover.direita is None:
                sucessor = remover  # O elemento tem no máximo um filho
            else:
                sucessor = self.sucessor(remover)  # O elemento tem dois filhos

            if sucessor.esquerda is not None:
                aux = sucessor.esquerda
            else:
                aux = sucessor.direita  # Sucessor não tem nenhum filho

            if aux is not None:
                aux.pai = sucessor.pai

            if sucessor.pai is None:
                self.__raiz = aux
            elif sucessor == sucessor.pai.esquerda:
                sucessor.pai.esquerda = aux
            else:
                sucessor.pai.direita = aux

            if sucessor != remover:

                remover.valor = sucessor.valor

            return sucessor

    def sucessor(self, chave):
        """ Retorna o sucessor de um número na sua sequência ordenada
                    Tem complexidade: O(h) sobre uma árvore de altura h """

        if isinstance(chave, BST.No):
            elemento = self.buscar(chave.valor)
        else:
            elemento = self.buscar(chave)

        if elemento is not None:  # O elemento procurado existe
            if elemento.direita is not None:
                return self.minimo(elemento.direita)

            ancestral = elemento.pai

            while ancestral is not None and elemento == ancestral.direita:
                elemento = ancestral
                ancestral = ancestral.pai

            return ancestral

    def antecessor(self, valor):
        """ Retorna o antecessor de um número na sua sequência ordenada
            Tem complexidade: O(h) sobre uma árvore de altura h """

        if isinstance(valor, BST.No):
            elemento = self.buscar(valor.valor)
        else:
            elemento = self.buscar(valor)

        if elemento:  # O elemento existe
            if elemento.esquerda is not None:
                return self.maximo(elemento.esquerda)

            ancestral = elemento.pai

            while ancestral is not None and elemento == ancestral.esquerda:
                elemento = ancestral
                ancestral = ancestral.pai

            if isinstance(valor, BST.No):
                return ancestral

            return ancestral.valor


arvore = BST()

arvore.inserir(15)
arvore.inserir(5)
arvore.inserir(3)
arvore.inserir(12)
arvore.inserir(10)
arvore.inserir(13)
arvore.inserir(6)
arvore.inserir(7)
arvore.inserir(16)
arvore.inserir(20)
arvore.inserir(18)
arvore.inserir(23)

print(arvore)

print('O maior elemento da árvore é: {}'.format(arvore.maximo()))
print('O menor elemento da árvore é: {}'.format(arvore.minimo()))
del arvore[15]
print(arvore)
