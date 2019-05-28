class NO:
    def __init__(self, valor):
        self.chave = valor
        self.proximo = None
        self.anterior = None

    def __str__(self):
        return str(self.chave)


class ListaDupla:
    def __init__(self, tipo=None):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0
        self.tipo = tipo

    def __len__(self):
        return self.tamanho

    def __str__(self):
        saida = '{'

        atual = self.primeiro
        while atual is not None:
            saida += atual.__str__() + ','
            atual = atual.proximo

        saida = saida[:-1]
        saida += '}'

        return saida

    def validar_tipo(self, valor):
        if self.tipo is not None:
            if type(valor) != self.tipo:
                return False
            return True
        return True

    def inserir(self, indice, valor):

        if not self.validar_tipo(valor):
            raise TypeError('Tipo de valor não permitido para a lista')

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
        elif indice == self.tamanho:
            novoNo.anterior = self.ultimo
            self.ultimo.proximo = novoNo

            self.ultimo = novoNo

        # inserindo no meio da lista
        else:

            i = 0
            atual = self.primeiro

            while i <= indice:

                if i == indice - 1:
                    novoNo.proximo = atual.proximo
                    atual.proximo.anterior = novoNo

                    atual.proximo = novoNo
                    novoNo.anterior = atual
                    break

                atual = atual.proximo
                i += 1

        self.tamanho += 1

    def inserir_inicio(self, valor):
        self.inserir(0, valor)

    def inserir_fim(self, valor):
        self.inserir(self.tamanho, valor)

    def remover(self, indice):

        i = 0
        atual = self.primeiro

        while i <= indice:

            if i == indice:

                if len(self) == 1:
                    self.primeiro = None
                    self.ultimo = None

                elif i == 0:  # removendo o primeiro elemento da lista
                    self.primeiro = atual.proximo
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

                self.tamanho -= 1
                return

            i += 1
            atual = atual.proximo

    def remover_fim(self):
        self.remover(len(self) - 1)

    def remover_inicio(self):
        self.remover(0)

    def __getitem__(self, indice):

        i = 0
        atual = self.primeiro
        while atual is not None:

            if i == indice:
                return atual.chave

            i += 1
            atual = atual.proximo


lista = ListaDupla(int)
lista.inserir_fim(4)
lista.inserir_fim(3)
lista.inserir_fim(7)
lista.inserir_inicio(8)
lista.inserir_inicio(9)
lista.inserir_fim(8.7)
print(lista)
