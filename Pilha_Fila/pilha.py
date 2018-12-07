
""" Implementação de uma estrutura pilha usando listas simplesmente encadeada """


class Stack:

    def __init__(self):

        self.__head = None
        self.__tail = None
        self.__length = 0
        self.__iterating = None  # Auxiliar para iterar na lista

    class Node:

        def __init__(self, value):
            self.next = None
            self.item = value

    def __len__(self):
        return self.__length  # Retornando o tamanho da lista

    def __iter__(self):
        return self

    def __next__(self):
        # Iterando na lista com o conceito de lazy evaluation
        if self.__iterating is None:
            self.__iterating = self.__head  # Começando a iterar do primeiro elemento
        else:
            self.__iterating = self.__iterating.next  # Indo para o próximo elemento

        if self.__iterating is not None:
            return self.__iterating.item  # Retornando o valor do elemento da vez

        raise StopIteration  # Não há mais nada para iterar, então paramos

    def __repr__(self):
        return self.__str__()

    def __str__(self):  # Retornando a pilha da forma bruta do python

        aux = '|'

        for i, element in enumerate(self):

            aux += element.__repr__()

            if i < len(self) - 1:
                aux += ', '

        aux += '|'

        return aux

    def push(self, value):  # Insere no inicio da pilha

        new_item = self.Node(value)

        if len(self) == 0:  # Inserindo na pilha se ela estiver vazia

            self.__head = new_item
            self.__tail = new_item

        else:

            new_item.next = self.__head
            self.__head = new_item

        self.__length += 1
        self.__iterating = None

    def pop(self):  # Remove o primeiro item da pilha

        current = self.__head

        if len(self) == 0:  # Não há nenhum item na pilha para se poder remover
            raise IndexError('no items in the stack')

        elif len(self) == 1:  # Se houver apenas um elemento

            self.__head = None
            self.__tail = None

        else:

            self.__head = current.next
            current.next = None

        self.__length -= 1
        self.__iterating = None  # Como a pilha foi alterarda, iterando deve ser reinicializado

    def findpeek(self):  # Retorna o elemento que está no topo da pilha
        return self.__head.item

    def isempty(self):  # Se a pilha está ou não vazia
        return len(self) == 0

pilha = Stack()
pilha.push(5)
pilha.push(6)
pilha.push(8)
pilha.push(7)

for item in pilha:
    print(item)

print(pilha)
print(pilha.findpeek())

pilha.pop()
print(pilha)
print(pilha.findpeek())
