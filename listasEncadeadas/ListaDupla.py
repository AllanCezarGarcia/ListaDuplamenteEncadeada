
from NoDuplo import No


class Lista:
    def __init__(self):
        self.__cabeca = No()
        self.__cabeca.setProximo(None)
        self.__cabeca.setAnterior(None)

    def getCabeca(self):
        return self.__cabeca

    def setCabeca(self, c):
        self.__cabeca = c

    def listaVazia(self):
        return self.__cabeca.getProximo() is None

    def insereNoInicio(self, n):
        primeiro = self.__cabeca.getProximo()

        n.setAnterior(self.__cabeca)
        n.setProximo(primeiro)

        if primeiro is not None:
            primeiro.setAnterior(n)

        self.__cabeca.setProximo(n)

    def insereNoFim(self, n):
        atual = self.__cabeca

        while atual.getProximo() is not None:
            atual = atual.getProximo()

        n.setAnterior(atual)
        n.setProximo(None)
        atual.setProximo(n)

    def insereOrdenado(self, n):
        ant = self.__cabeca
        atual = ant.getProximo()

        while atual is not None and atual.getChave() < n.getChave():
            ant = atual
            atual = atual.getProximo()

        n.setAnterior(ant)
        n.setProximo(atual)
        ant.setProximo(n)

        if atual is not None:
            atual.setAnterior(n)

    def retiraNoInicio(self):
        primeiro = self.__cabeca.getProximo()

        if primeiro is None:
            return None

        proximo = primeiro.getProximo()
        self.__cabeca.setProximo(proximo)

        if proximo is not None:
            proximo.setAnterior(self.__cabeca)

        primeiro.setProximo(None)
        primeiro.setAnterior(None)

        return primeiro

    def retiraNoFim(self):
        atual = self.__cabeca.getProximo()

        if atual is None:
            return None

        while atual.getProximo() is not None:
            atual = atual.getProximo()

        anterior = atual.getAnterior()
        anterior.setProximo(None)

        atual.setProximo(None)
        atual.setAnterior(None)

        return atual

    def retiraPelaChave(self, chave):
        atual = self.__cabeca.getProximo()

        while atual is not None and atual.getChave() != chave:
            atual = atual.getProximo()

        if atual is None:
            return None

        anterior = atual.getAnterior()
        proximo = atual.getProximo()

        anterior.setProximo(proximo)

        if proximo is not None:
            proximo.setAnterior(anterior)

        atual.setProximo(None)
        atual.setAnterior(None)

        return atual

    def mostraLista(self):
        atual = self.__cabeca.getProximo()

        while atual is not None:
            print(atual.getValores())
            atual = atual.getProximo()

    def mostraListaInvertida(self):
        atual = self.__cabeca.getProximo()

        if atual is None:
            return

        while atual.getProximo() is not None:
            atual = atual.getProximo()

        while atual is not self.__cabeca:
            print(atual.getValores())
            atual = atual.getAnterior()

    def quantidadeDeElementos(self):
        quantidade = 0
        atual = self.__cabeca.getProximo()

        while atual is not None:
            quantidade += 1
            atual = atual.getProximo()

        return quantidade
