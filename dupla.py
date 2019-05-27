class NO:
    def __init__(self, valor):
        self.chave = valor
        self.proximo = None
        self.anterior = None


class ListaDupla:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0

    def inserir(self, indice, valor):

        novoNo = NO(valor)

        #Lista ainda vazia
        if self.tamanho == 0:
            self.primeiro = novoNo
            self.ultimo = novoNo

        # inserindo no inicio
        elif indice == 0:
            novoNo.proximo = self.primeiro
            self.primeiro.anterior = novoNo

            self.primeiro = novoNo

        # inserindo no fim
        elif indice == self.tamanho - 1:
            novoNo.proximo = self.ultimo
            self.ultimo.proximo = novoNo

            self.ultimo = novoNo

        # inserindo no meio da lista
        else:

            i = 0
            atual = self.primeiro

            while i <= indice:

                if i == indice - 1:
                    novoNo.proximo = atual.proximo
                    novoNo = atual
                    atual.proximo = novoNo
                    atual.proximo.anterior = novoNo

                atual = atual.proximo
                i += 1

        self.tamanho += 1

    def inserir_inicio(self, valor):
        self.inserir(0, valor)

    def inserir_fim(self, valor):
        self.inserir(self.tamanho - 1, valor)

    def remover(self, indice, valor):

        i = 0
        atual = self.primeiro

        while i <= indice:

            if i == 0:  # removendo o primeiro elemento da lista
                self.primeiro = atual
                self.primeiro.anterior = None
                atual.proximo = None

            elif i == self.tamanho - 1:  # removendo o último elemento da lista
                self.ultimo = atual.anterior
                self.ultimo.proximo = None
                atual.anterior = None

            else:

                atual.anterior.proximo = atual.proximo
                atual.proximo.anterior = atual.anterior

                atual.proximo = None
                atual.anterior = None

                return

            i += 1
            atual = atual.proximo


lista = ListaDupla()
lista.inserir_inicio(4)
lista.inserir_inicio(3)
lista.inserir_inicio(8)
lista.inserir_inicio(10)
print(lista)
