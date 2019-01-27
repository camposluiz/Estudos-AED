class TabelaHash:
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__qnt_elementos = 0
        self.__tabela = []
        self.__init_tabela()

    class Elemento:
        def __init__(self, chave, valor):
            self.chave = chave
            self.valor = valor

    def __iter__(self):
        return iter(self.keys())

    # Método para retornar a quantidade de elementos que existem na tabela
    def __len__(self):
        return self.__qnt_elementos

    # Método para retornar os valores na representação padrão do python
    def __repr__(self):
        return self.__str__()

    # Método que imprimi a tabela visualmento igual a forma que o python faz
    def __str__(self):
        output = '{'

        i = 0
        for chave, valor in self.items():
            output += chave.__repr__() + ': ' + valor.__repr__()

            if i < len(self) - 1:
                output += ', '

            i += 1

        output += '}'

        return output

    def __atualizar_chave(self, elemento, value):
        elemento.valor = value

    def __delitem__(self, key):
        elemento, existe, indice_tabela, indice_lista = self.__informacoes_elemento(key)

        if existe:
            del self.__tabela[indice_tabela][indice_lista]
            self.__qnt_elementos -= 1
            return

        raise KeyError(key)

    def __criar_nova_chave(self, key, value):
        indice = self.__funcao_hash(key)
        novo_item = self.Elemento(key, value)
        self.__tabela[indice].append(novo_item)

    def __setitem__(self, key, value):

        """ Caso uma chave não exista, ela é criada. Se ela já existe, é atualizada """

        elemento, existe, _, _= self.__informacoes_elemento(key)

        # Se o elemento existir, atualizamos a chave
        if existe:
            self.__atualizar_chave(elemento, value)
            return

        # Se não existir, criamos uma nova chave
        self.__criar_nova_chave(key, value)
        self.__qnt_elementos += 1

    # Método para verificar se uma chave existe
    def __contains__(self, key):
        _, existe, _, _ = self.__informacoes_elemento(key)

        if existe:
            return True

        return False

    def __getitem__(self, key):
        elemento, existe, _, _ = self.__informacoes_elemento(key)
        if existe:
            return elemento.valor
        raise KeyError(key)


    def __informacoes_elemento(self, key):
        """ Método que retorna uma tupla contento:

            referência ao objeto, valor booleano se o elemento existe,
            índice na tabela, índice na lista ligada dentro da tabela"""

        indice = self.__funcao_hash(key)

        for i, elemento in enumerate(self.__tabela[indice]):
            if elemento.chave == key:
                return elemento, True, indice, i

        return None, False, None, None


    # Método que retorna uma lista contendo todas as chaves da tabela
    def keys(self):
        chaves = []
        for lista in self.__tabela:
            for elemento in lista:
                chaves.append(elemento.chave)

        return chaves

    # Método que retorna uma lista contendo todos os valores da tabela
    def values(self):
        valores = []
        for lista in self.__tabela:
            for elemento in lista:
                valores.append(elemento.valor)

        return valores

    # Método que retorna uma lista contendo todos os valores (chave - valor) da tabela
    def items(self):
        items = []
        for lista in self.__tabela:
            for elemento in lista:
                tupla = elemento.chave, elemento.valor
                items.append(tupla)

        return items

    # Função para calcular o índice de uma dada chave
    def __funcao_hash(self, key):
        return hash(key) % self.__tamanho

    # Método para inicializar a tabela (colocar as listas ligadas no seus índices)
    def __init_tabela(self):
        for i in range(self.__tamanho):
            self.__tabela.append([])

doramas = TabelaHash(23)
doramas['something'] = 10
doramas['jardim'] = 9
doramas['bom-dia'] = 13
doramas['o'] = 11
doramas['something'] = 1

print(doramas)
del doramas['o']
doramas['something'] += 9
print(doramas)
a = doramas['something']
print(a)
