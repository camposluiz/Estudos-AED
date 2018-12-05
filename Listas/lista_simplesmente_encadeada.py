class LinkedList:

    def __init__(self):
        self.__head = None  # aponta para o primeiro elemento da lista
        self.__tail = None  # aponta para o último elemento da lista
        self.__length = 0
        self.__iterating = None  # auxiliar para iterar com lazy evaluation

    class Node:  # classe interna para a criação de um novo Nó

        def __init__(self, value):
            self.next = None
            self.content = value

    def __len__(self):
        return self.__length  # retornando o tamanho da lista

    def __iter__(self):
        return self

    def __next__(self):
        # iterando na lista usando o conceito de lazy evaluation
        if self.__iterating is None:
            self.__iterating = self.__head  # começando do primeiro
        else:
            self.__iterating = self.__iterating.next  # indo para o próximo

        if self.__iterating is not None:
            return self.__iterating.content

        raise StopIteration  # parando de iterar

    def __repr__(self):
        return self.__str__()

    def __str__(self):  # retornado a lista na forma bruta do python
        aux = '|'

        for i, element in enumerate(self):
            aux += element.__repr__()

            if i < len(self) - 1:
                aux += ', '

        aux += '|'

        return aux

    def __delitem__(self, key):

        if key < 0:  # tratando índices negativos (del lista[-1]) -> apaga o último elemento
            key += len(self)

        if key < 0 or key >= len(self):  # informando possíveis erros
            raise IndexError('list assignment index out of range')


        current = self.__head
        previous = None
        i = 0
        while i <= key:

            if current is None:
                break

            if i == key:

                # removendo o primeiro elemento da lista
                if previous is None:

                    self.__head = current.next
                    current.next = None

                # removendo o último elemento da lista
                elif current.next is None:

                    self.__tail = previous
                    previous.next = None

                #removendo o elemento no meio da lista
                else:

                    previous.next = current.next
                    current.next = None

                self.__length -= 1  # removendo um elemento

                return

            previous = current
            current = current.next

            i += 1

        self.__iterating = None

    def pop(self, i=-1):  # removendo o último elemento
        self.__delitem__(i)

    def insert(self, key, value):  # inserindo em qualquer posição da lista

        new_node = self.Node(value)

        # inserindo a lista estando vazia
        if len(self) == 0:

            self.__head = new_node
            self.__tail = new_node

        # inserindo no começo da lista
        elif key <= 0:

            new_node.next = self.__head
            self.__head = new_node

        # inserindo no fim da lista
        elif key >= len(self):

            self.__tail.next = new_node
            self.__tail = new_node

        #inserindo no meio da lista
        else:

            current = self.__head  # começamos do primeiro elemento
            previous = None

            i = 0
            while i <= key:

                if current is None:
                    break

                if i == key:

                    new_node.next = previous.next
                    previous.next = new_node
                    break

                # se não é o índice desejado, vamos para o próximo elemento
                previous = current
                current = current.next

                i += 1

        self.__length += 1  # um elemento adicionado
        self.__iterating = None  # Como a lista foi alterada, iterating deve ser modificado

    def append(self, value):  # inserindo um elemento na última posição
        self.insert(len(self), value)


lista = LinkedList()
lista.append(4)
lista.append(5)
lista.append(7)
print(lista)

lista.pop()
print(lista)
del lista[0]
print(lista)
