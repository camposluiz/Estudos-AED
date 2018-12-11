package ListaEncadeada;


class LinkedList {

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

            while (i <= chave) {

                if (atual == null) {
                    break;
                }

                if (i == chave - 1) {

                    novo.proximo = atual.proximo;
                    atual.proximo = novo;

                }

                atual = atual.proximo;
                i += 1;

            }

        }

        this.tamanho += 1;

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
