from math import floor  # Calcula o piso de um número

class Heap:

    def __init__(self, heap=None):

        if heap is None:
            self.__heap = []
        else:
            self.__heap = heap

    @property
    def heap(self):
        return self.__heap

    @heap.setter
    def heap(self, obj):
        self.__heap = list(obj)

    def __len__(self):
        return len(self.__heap)

    def __getitem__(self, item):
        return self.__heap[item]

    def __setitem__(self, key, value):
        self.__heap[key] = value

    def __delitem__(self, key):
        del self.__heap[key]

    def __str__(self):
        return self.__heap.__str__()

    def parent(self, i):  # Método que retorna o índice do pai de um elemento com índice i
        parent = floor((i - 1) / 2)  # O floor calcula o piso do número

        return parent if parent >= 0 else None

    def right(self, i):  # Retorna quem é o filho da direita de um índice i
        right = (2 * i) + 1

        return right if right < len(self) else None

    def left(self, i):  # Retorna quem é o filho da esquerda de um índice i
        left = (2 * i) + 2

        return left if left < len(self) else None

    def max_heapify(self, i):  # Matendo a propriedade de um heap de máximo

        l = self.left(i)
        r = self.right(i)

        if l is not None and self[l] > self[i]:
            largest = l
        else:
            largest = i

        if r is not None and self[r] > self[largest]:
            largest = r

        if largest != i:  # Significa que um filho é maior do que seu pai. Logo, trocamos-os afim de manter a propriedade
            self[i], self[largest] = self[largest], self[i]

            self.max_heapify(largest)  # Chamada recursiva para o índice em que o nó deslocou-se

    def build_maxheap(self):  # Realiza a contrução de um heap

        i = floor(len(self) / 2) - 1  # Começando das folhas da árvore. E depois vamos subindo
        while i >= 0:

            self.max_heapify(i)

            i -= 1

    def heapsort(self):

        self.build_maxheap()

        sort = []  # Lista auxiliar

        i = len(self) - 1
        while i >= 0:
            # O maior elemento sempre está na raiz
            largest = self[0]

            # Colocando o último elemento na raíz
            self[0] = self[-1]

            # Já ordenou um elemento, então apagamos ele
            del self[-1]

            # Mantendo a propriedade do heap
            self.max_heapify(0)

            sort.insert(0, largest)  # Ordena de forma crescente
            # sort.append(largest)  # Ordena de forma inversa

            i -= 1

        self.__heap = sort
