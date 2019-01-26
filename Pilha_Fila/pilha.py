""" Implementação de uma estrutura pilha usando listas simplesmente encadeada """

class Pilha:

    def __init__(self):
        self.__topo = None  # Aponta para o elemento que está no topo da pilha
        self.__tamanho = 0
        self.__iterando = None

    class No:

        def __init__(self, valor):
            self.chave = valor
            self.abaixo = None  # Aponta para o elemento que está abaixo na pilha

    def __len__(self):
        return self.__tamanho

    def __iter__(self):
        return self

    def __next__(self):  # Iterando sobre os elementos na pilha
        if self.__iterando is None:
            self.__iterando = self.__topo
        else:
            self.__iterando = self.__iterando.abaixo

        if self.__iterando is not None:
            return self.__iterando.chave

        raise StopIteration

    def __repr__(self):
        return self.__str__()

    def __str__(self):

        output = '{'

        for i, e in enumerate(self):

            output += e.__repr__()

            if i < len(self) - 1:
                output += ', '

        output += '}'

        return output

    def push(self, valor):

        novo_item = self.No(valor)

        if len(self) == 0:  # Pilha está vazia
            self.__topo = novo_item

        else:
            novo_item.abaixo = self.__topo  # O novo item aponta para o elemento que está abaixo
            self.__topo = novo_item

        self.__tamanho += 1
        self.__iterando = None

    def pop(self):

        atual_topo = self.__topo  # Elemento topo que será removido

        if len(self) >= 1:  # Caso haja no mínimo um elemento na pilha

            self.__topo = atual_topo.abaixo
            atual_topo.abaixo = None

            self.__tamanho -= 1
            self.__iterando = None
            return

        raise ValueError('Não há elementos a serem removidos da pilha')

    def vazia(self):
        return len(self) == 0

    def findpeek(self):
        return self.__topo.chave

pilha = Pilha()

pilha.push(1)
pilha.push(2)
pilha.push(3)

print(pilha)
print(len(pilha))
pilha.pop()
print(pilha)
print(len(pilha))
