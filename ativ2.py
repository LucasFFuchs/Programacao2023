#Objetivo: Criar um programa que printe os numeros de uma lista e, depois, eles multiplicados por 2
#Bonus: Colocar os numeros multiplicados em uma outra lista e printa-la


lista=[2,3,7,12,2]
lista2=[]
num=1
for i in lista:
    lista2.append(i*2)
    print(f"{num}º numero da primeira lista = {i}")
    num=num+1
print("")
num=1
for i in lista2:
    print(f"{num}º numero da segunda lista = {i}")
    num=num+1

print(f"lista 1:{lista}")
print(f"lista 2:{lista2}")
