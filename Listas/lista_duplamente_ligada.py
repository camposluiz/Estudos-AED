class DoublyLinked:

    def __init__(self):

        self.__head = None  # Aponta para o primeiro elemento da lista
        self.__tail = None  # Aponta para o último elemento da lista
        self.__length = 0
        self.__iterating = None  # Axiliar para iterar com lazy evaluation

    class Node:

        def __init__(self, value):

            self.next = None
            self.previous = None
            self.content = value

    def __len__(self):
        return self.__length  # Retornando o tamanho da lista

    def __iter__(self):
        return self

    def __next__(self):
        # Iterando na lista usando o conceito de lazy evaluation
        if self.__iterating is None:
            self.__iterating = self.__head  # Iterando no primeiroe elemento
        else:
            self.__iterating = self.__iterating.next  # Indo para o próximo elemento

        if self.__iterating is not None:
            return self.__iterating.content  # Retornando o elemento da vez

        raise StopIteration  # Não há mais itens para iterar. Logo, paramos de iterar

    def __repr__(self):
        return self.__str__()

    def __str__(self):

        aux = '|'

        for i, element in enumerate(self):
            aux += element.__repr__()

            if i < len(self) - 1:
                aux += ', '

        aux += '|'

        return aux

    def __delitem__(self, key):

        if key < 0:  # Tratando índices negativos. Ex(del list[-1])
            key += len(self)

        if key < 0 or key >= len(self):  # Informando possíveis erros
            raise IndexError('list assignment index out of range')

        i = 0
        current = self.__head

        while i <= key:

            if current is None:
                break

            if i == key:

                # Caso a lista tenha apenas um único elemento
                if len(self) == 1:
                    self.__head = None
                    self.__tail = None

                # Removendo o primeiro elemento da lista
                elif i == 0:

                    self.__head = current.next
                    self.__head.previous = None
                    current.next = None

                # Removendo o último elemento da lista
                elif i == len(self) - 1:

                    self.__tail = current.previous
                    self.__tail.next = None
                    current.previous = None

                # Removendo um elemento no meio da lista
                else:

                    current.previous.next = current.next
                    current.next.previous =  current.previous

                    current.next = None
                    current.previous = None

                self.__length -= 1
                self.__iterating = None

                return current.content

            current = current.next
            i += 1

    def pop(self, i=-1):  # Remover o último elemento da lista
        del self[i]

    def insert(self, key, value):

        new_node = self.Node(value)

        # Inserindo em uma lista vazia
        if len(self) == 0:

            self.__head = new_node
            self.__tail = new_node

        # Inserindo no começo da lista
        elif key <= 0:

            new_node.next = self.__head
            self.__head.previous = new_node

            self.__head = new_node

        # Inserindo no fim da lista
        elif key >= len(self):

            new_node.previous = self.__tail
            self.__tail.next = new_node

            self.__tail = new_node

        # Inserindo no meio da lista
        else:

            i = 0
            current = self.__head

            while i <= key:

                if current is None:
                    break

                if i == key - 1:

                    new_node.next = current.next
                    current.next.previous = new_node

                    current.next = new_node
                    new_node.previous = current

                    break

                current = current.next
                i += 1

        self.__length += 1  # Um elemento foi adicionado
        self.__iterating = None  # Como a lista foi alterada, iterating é reinicializado

    def append(self, value):  # Adiciona um elemento na última posição da lista
        self.insert(len(self), value)

    def push(self, value):  # Adiciona um elemento na primeira posição da lista
        self.insert(0, value)


lista = DoublyLinked()
print(lista)

lista.insert(0, 7)
lista.insert(0, 5)

for item in lista:  # Conseguindo iterar na lista
    print(item)

lista.pop()
print(lista)

lista.push(7)
print(lista)