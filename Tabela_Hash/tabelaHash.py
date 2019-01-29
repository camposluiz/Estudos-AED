class TabelaHash:
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__qnt_elementos = 0
        self.__tabela = []
        self.__init_tabela()


    class Elemento:
        """ Representação interna do elemetno dentro da tabela """

        def __init__(self, key, value):
            self.chave = key
            self.valor = value


    def __len__(self):
        """ Retorna a quantidade de elementos presentes na tabela """

        return self.__qnt_elementos


    def __repr__(self):
        """ Retorna o objeto na forma bruta do python """

        return self.__str__()


    def __iter__(self):
        """ Iterando sobre a lista que guarda as chaves """

        return iter(self.keys())


    def __str__(self):
        """ Imprime a tabela de forma visualmente semelhante aos dicionários built-in do python """

        output = '{'

        i = 0
        for chave, valor in self.items():
            output += chave.__repr__() + ': ' + valor.__repr__()

            if i < len(self) - 1:
                output += ', '

            i += 1

        output += '}'
        return output


    def __setitem__(self, key, value):
        """ Se a chave informada existir, atualizamos o seu valor.
            Caso contrário, criamos uma nova chave """

        # Utilizando o empacotamento e desempacotamento do python (ver comentário no método informacoes)
        elemento, existe, _, _ = self.__informacoes_elemento(key)

        if existe:
            # Se a chave já existe na tabela, atualizamos o seu valor
            self.__atualiza_chave(elemento, value)

        else:
            # Se o elemento não existir, criamos uma nova chave
            self.__cria_chave(key, value)


    def __getitem__(self, key):

        """ Se o elemento estiver presente na tabela, retorna o seu valor.
            Caso contrário lança uma exceção do tipo KeyError """

        elemento, existe, _, _ = self.__informacoes_elemento(key)

        if existe:
            # Se o elemento existe na tabela, retornamos o seu valor
            return elemento.valor

        # O elemento não está presente na tabela
        raise KeyError(key)


    def __delitem__(self, key):

        """ Se uma chave estiver presente na tabela, ela(referência_elemento) vai ser apagada """

        _, existe, indice_tabela, indice_lista = self.__informacoes_elemento(key)

        if existe:
            # Como a chave está presente, a mesma é apagada
            del self.__tabela[indice_tabela][indice_lista]
            self.__qnt_elementos -= 1
            return

        # A chave não está presente na tabela
        raise KeyError(key)


    def __contains__(self, key):
        """ Retorna um valor verdadeiro ou falso se a chave está presente na tabela """

        _, existe, _, _ = self.__informacoes_elemento(key)

        return existe


    def __atualiza_chave(self, elemento, value):
        """ Método que toma com parâmetro uma referência ao objeto e seu novo
            valor que será atualizado """

        elemento.valor = value


    def __cria_chave(self, key, value):
        """ Método que cria uma nova chave e já adiciona à tabela """

        indice = self.__calcula_indice(key)
        novo_item = self.Elemento(key, value)

        self.__tabela[indice].append(novo_item)
        self.__qnt_elementos += 1


    def __informacoes_elemento(self, key):
        """ Método que retorna uma tupla contendo as seguintes informações sobre o elemento:
        (referência ao objeto,
         valor boolenao se o elemento existe na tabela,
         seu índice na tabela,
         seu índice dentro da lista ligada) """

        indice = self.__calcula_indice(key)

        for i, elemento in enumerate(self.__tabela[indice]):
            if elemento.chave == key:
                # A chave existe na tabela
                return elemento, True, indice, i

        # A chave não existe na tabela
        return None, False, None, None


    def keys(self):
        """ Método para retornar todos os valores do tipo chave presentes na tabela """

        keys = []
        for lista in self.__tabela:
            for elemento in lista:
                keys.append(elemento.chave)
        return keys


    def values(self):
        """ Método para retornar todos os valores do tipo valor presentes na tabela """

        values = []
        for lista in self.__tabela:
            for elemento in lista:
                values.append(elemento.valor)
        return values


    def items(self):
        """ Método para retornar todos os valores (Chave-Valor) presentes na tabela """

        items = []
        for lista in self.__tabela:
            for elemento in lista:
                tupla = elemento.chave, elemento.valor
                items.append(tupla)
        return items

    def __calcula_indice(self, key):
        """ Retornando o índice do elemento na chave a partir da sua chave """

        return hash(key) % self.__tamanho


    def __init_tabela(self):
        """ Criandos as listas ligadas dentro da tabela """

        for i in range(self.__tamanho):
            self.__tabela.append([])


doramas = TabelaHash(23)
doramas['something'] = 10
doramas['jardim'] = 12
print(doramas)
del doramas['something']
a = doramas['jardim']
print(a)
