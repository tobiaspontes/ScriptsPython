x = int(input('Digite um número ou zero para terminar: '))

lista=[]

while x != 0:
    lista.append(x)
    x = int(input('Digite um número ou zero para terminar: '))

l = len(lista)

while l > 0:
    print(lista[l - 1])
    l = l - 1
    
