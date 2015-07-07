print  # acessando os itens a lista

n = [1, 3, 5]
print n[1]


print "multiplicando e modificando os itens da lista"

n = [1, 3, 5]
n[1] = 5 * n[1]
print n

print "removendo itens da lista"

n = [1, 3, 5]
n.remove(1)
print n

print "adicionando itens a lista"

n = [1, 3, 5, ]
n.append(4)
print n

print "substituindo itens da lista"

domestic_animals = ["cachorro", "tartaruga", "hamster"]
domestic_animals[0] = "gato"
domestic_animals[1] = "papagaio"
print domestic_animals
