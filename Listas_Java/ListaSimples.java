package ListaEncadeada;

class LinkedList  {

    private No primeiro;
    private No ultimo;
    private int tamanho;

    LinkedList() {  // contrutor da clase Lista

        this.primeiro = null;
        this.ultimo = null;
        this.tamanho = 0;
    }


    // criação da classe interna Nó
    private static class No {

        No proximo;
        int valor;

        No(int value) {

            valor = value;
            proximo = null;
        }

    }

    void inserir(int chave, int valor) {

        No novo = new No(valor);

        // inserindo em uma lista vazia
        if (this.tamanho == 0) {

            this.primeiro = novo;
            this.ultimo = novo;
        }

        // inserindo no começo da lista
        else if (chave <= 0) {

            novo.proximo = this.primeiro;
            this.primeiro = novo;
        }

        // inserindo no fim da lista
        else if (chave >= this.tamanho) {

            this.ultimo.proximo = novo;
            this.ultimo = novo;

        }

        // inserindo no meio da lista
        else {

            int i = 0;
            No atual = this.primeiro;
            No anterior = null;

            while (i <= chave) {

                if (atual == null) {
                    break;
                }

                if (i == chave) {

                    novo.proximo = anterior.proximo;
                    anterior.proximo = novo;

                }

                anterior = atual;
                atual = atual.proximo;
                i += 1;

            }

        }

        this.tamanho += 1;

    }

    void append(int value) {

        inserir(this.tamanho, value);

    }

    void remover(int key) {

        if (key < 0)  // Tratando índices negativos
            key += this.tamanho;

        if (key < 0 || key >= this.tamanho) {
            throw new IndexOutOfBoundsException("índice fora dos limites da lista");
        }

        No atual = this.primeiro;
        No anterior = null;

        int i = 0;
        while (i <= key) {

            if (atual == null)
                break;

            if (i == key) {

                // Removendo de uma lista vazia
                if (this.tamanho == 0) {

                    this.primeiro = null;
                    this.ultimo = null;
                }

                // Removendo o primeiro elemento da lista
                else if (key == 0) {

                    this.primeiro = atual.proximo;
                    atual.proximo = null;
                }

                // Removendo o último elemento da lista

                else if (key == this.tamanho - 1) {

                    this.ultimo = anterior;
                    anterior.proximo = null;
                }

                // Removendo um elemento no meio da lista
                else {

                    anterior.proximo = atual.proximo;
                    atual.proximo = null;

                }

                this.tamanho -= 1;
                break;
            }

            anterior = atual;
            i += 1;

        }

    }

    int tamanho () {
        return this.tamanho;
    }

    public String toString(){

        No atual = this.primeiro;
        StringBuilder retorno = new StringBuilder();

        retorno.append("[");
        int i = 0;
        while (i < this.tamanho) {

            retorno.append(atual.valor);

            if (i < this.tamanho - 1)
                retorno.append(", ");

            atual = atual.proximo;
            i += 1;

        }
        retorno.append("]");

        return retorno.toString();

    }
}
