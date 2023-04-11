#Arrays
notas = [7.8, 9.7, 8.1]

#Criando listas
lista = [] #lista vazia
listaa = list() #lista vazia
lista = [25, "Jeiel", 1.73, True] #pode usar vários valores numa lista
lista_de_listas = [10,[1,3,4]]

#Indexação e slices(fatiamento)
lista1 = [25, "Jeiel", 1.73, True]
#print(lista1[1]) #lista[-1] acessa o último elemento da lista

#Slices
#print(lista1[0:3]) #imprime do indíce selecionado ao outro

# > Interação com for
# 1. Utilizando os próprios elementos da lista
#for elemento in lista1:
#    print(elemento) #imprime a lista separada

#2. Utilizando o índice
print ("Comprimento da lista:", len(lista))
for i in range(len(lista1)):
    print(lista[i])
