
""" Implementação de uma estrutura do tipo fila, usando uma lista simplesmente encadeada """

class Queue:

    def __init__(self):
        self.__head = None  # Aponta para o primeiro elemento da lista
        self.__tail = None  # Aponta para o último elemento da lista
        self.__length = 0
        self.__iterating = None  # Auxilar para iterar na lista

    class Node:  # Criação de um nó

        def __init__(self, value):
            self.next = None
            self.item = value

    def __len__(self):
        return self.__length

    def __iter__(self):
        return self

    def __next__(self):
        # Iterando na lista usando o conceito de lazy evaluation
        if self.__iterating is None:
            self.__iterating = self.__head  # Iterando no primeiro elemento
        else:
            self.__iterating = self.__iterating.next  # Indo para o próximo elemento

        if self.__iterating is not None:
            return self.__iterating.item  # Retornando o elemento

        raise StopIteration  # Parando de iterar

    def __repr__(self):
        return self.__str__()

    def __str__(self):  # Iprimindo a lista na forma bruta do python
        aux = '|'

        for i, element in enumerate(self):

            aux += element.__repr__()

            if i < len(self) - 1:

                aux += ', '

        aux += '|'

        return aux

    def enqueue(self, value):  # Insere um item na última posição da fila

        new_item = self.Node(value)

        if len(self) == 0:  # Caso a lista esteja vazia

            self.__head = new_item
            self.__tail = new_item

        else:  # Se não, vamos sempre iserir no fim

            self.__tail.next = new_item
            self.__tail = new_item

        self.__length += 1
        self.__iterating = None

    def dequeue(self):  # Remove o primeiro item da fila

        if len(self) == 0:  # Se a fila estiver vazia, não há quem remover

            raise IndexError('list assignment index out of range')

        else:

            if len(self) == 1:  # Se tiver apenas um elemento na fila

                self.__head = None
                self.__tail = None

            else:

                current = self.__head  # Primeiro elemento

                self.__head = current.next
                current.next = None

            self.__length -= 1  # Um elemento foi removido
            self.__iterating = None  # Lista alterar, iterating é reinicializado

fila = Queue()
fila.enqueue('física 1')
fila.enqueue('física teórica')
fila.enqueue('física de partículas')

print(fila)
fila.dequeue()
print(fila)

for item in fila:  # Conseguindo iterar na lista
    print(item)
