#  A diferença entre as tuplas e listas é que as tuplas são imutaveis, já as litas não.
#  Para  criar uma lista basta usar os colchetes
lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
print(lanche)

#  Uma forma de mudar as listas é simplesmente selecionando a posição que deseja alterar e o que vai adicionar no lugar.
lanche[3] = 'Picole'
print(lanche)

#  .Append(novo item) Adiciona mais um item ao final da lista.
lanche.append("Pudim")
print(lanche)

#  .Insert(Posição, Objeto) Insere um novo item na posição informada
lanche.insert(1, 'Batata')
print(lanche)

#  Para apagar itens da lista podemos usar o comando del, ex: del Lanche[3].
del lanche[1]
print(lanche)

#  .pop(A posição é opicional neste caso) Deleta o ultimo item da listaa quando nao informado a posição do objeto.
lanche.pop()
print(lanche)

#  .remove(nome do objeto) remove o objeto atraves do seu nome.
lanche.remove('Pizza')
print(lanche)

#  Removendo objetos utilizando estruturas condicionais.
if 'Hamburguer' in lanche:
    lanche.remove('Hamburguer')
print(lanche)

#  Também é possivel criar listas através de método range.
valores = list(range(4,11))
print(valores)

#  É possível também colocar valores fora de ordem em uma lista e organizalos depois utilizando o metodo .sort().
valores = [8, 2, 5, 4, 9, 3, 0]
print(valores)
valores.sort()
print(valores)

#  Para ordenar os valores em ordem decrescente basta passar para o metodo .sort() o parametro reverse=True.
valores.sort(reverse=True)
print(valores)

#  Para saber o comprimento de uma lista basta usar a função Len().
print(len(valores))
