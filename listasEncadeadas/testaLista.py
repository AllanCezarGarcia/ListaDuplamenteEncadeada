from Elemento import Elemento
from NoDuplo import No
from ListaDupla import Lista

l = Lista()

x = int(input("Digite uma chave [-1 para sair]: "))

while x != -1:
    nome = input("Digite o nome: ")
    e = Elemento(x, nome)
    n = No(e)

    l.insereNoInicio(n)

    l.mostraLista()

    print("\nQuantidade de elementos na lista: " +
          str(l.quantidadeDeElementos()))

    x = int(input("Digite uma chave [-1 para sair]: "))


print("\nMostra Lista")
l.mostraLista()


print("\nMostra Lista Invertida")
l.mostraListaInvertida()


print("\nLimpando a Lista")

while not l.listaVazia():
    n = l.retiraNoInicio()

    if n != None:
        print(n.getValores())


print("\nQuantidade de elementos na lista: " +
      str(l.quantidadeDeElementos()))

print("Lista vazia:", l.listaVazia())