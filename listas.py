lista1=[0,1,2,3] 
lista2=["A","B","C"]
lista3=[lista1,lista2]
print(lista3)
print(lista3[0])
print(lista3[1])
print(lista3[1][0])


d = 10
desplaza = [d + x for x in range(5)]
print(desplaza)
potencias = [3 ** x for x in range(2, 6)]
print(potencias)

lista=[4,5,-1,6,7]
lista.sort() #Demenoramayor
print(lista)
lista.sort(reverse=True) #Demayoramenor
print(lista)


#AHORA VAMOS A VER COMO SE PUEDE CREAR UNA LISTA (ARREGLO)
def lee_arreglo_enteros():
 return[int(x) for x in input("Arreglo:").split()]
print(lee_arreglo_enteros())


matriz = ([1,2,3], [4,5,6], [7,8,9])
valor = matriz [0] [0]
print (f"El valor de la cordenada es {valor}")