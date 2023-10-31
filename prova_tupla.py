lista1 = [1,2,3,4,5,6]
lista2 = [4,5,6,7,8,9]
lista3 = []
soma = 0

for num in lista1:
    if num in lista1 and num in lista2:
        lista3.append(num)
        soma += num

tupla = (lista3, soma)

print(tupla)