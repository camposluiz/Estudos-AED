class Fila:

    def __init__(self):
        self.__primeiro = None  # Aponta para o primeiro elemento na fila
        self.__ultimo = None  # Aponta para o último elemento na fila
        self.__tamanho = 0
        self.__iterando = None

    class No:

        def __init__(self, valor):
            self.proximo = None
            self.chave = valor

    def __len__(self):
        return self.__tamanho

    def __iter__(self):
        return self

    def __next__(self):  # Iterando na fila usando o conceito de lazy evaluation

        if self.__iterando is None:
            self.__iterando = self.__primeiro  # Começando a iterar do início
        else:
            self.__iterando = self.__iterando.proximo  # Indo para o próximo da fila

        if self.__iterando is not None:
            return self.__iterando.chave  # Retornado o valor

        raise StopIteration  # Parando de iterar

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

    def enqueue(self, valor):

        """ Insere um elemento sempre no fim da fila
            Complexidade: O(1) """

        new_item = self.No(valor)

        if len(self) == 0:
            self.__primeiro = new_item
            self.__ultimo = new_item
        else:
            self.__ultimo.proximo = new_item  # Ligando o penúltimo da fila com o novo da fila
            self.__ultimo = new_item  # O último da fila agora é o elemento que foi adicionado

        self.__tamanho += 1
        self.__iterando = None

    def dequeue(self):

        """ Remove sempre o primeiro elemento da fila
            Complexidade: O(1) """

        atual_primeiro = self.__primeiro  # Primeiro elemento da fila

        if len(self) >= 1:  # Existem elementos na fila a serem removidos

            if len(self) == 1:
                self.__primeiro = None
                self.__ultimo = None
            else:

                self.__primeiro = atual_primeiro.proximo
                atual_primeiro.proximo = None

            self.__tamanho -= 1
            self.__iterando = None
            return atual_primeiro

        raise ValueError('não há elemento na fila a serem removidos')

fila = Fila()
fila.enqueue(4)
fila.enqueue(3)
fila.enqueue(1)
print(fila)
fila.dequeue()

for elemento in fila:
    print(elemento, end=' ')
