#   tupla

tup2 = (1,2,3,4,5,6) #Las tuplas inician en posiciones de 0,1,2,3.. por tanto el elemento 2 sería el numero 3
#Las tublas no se pueden modificar una vez definidas
print (f"Estos son los elementos totales{tup2}")
print (f"El elemento en su parte 2 es {tup2[2]}")

x= tup2 [2] * 3 

print (x)

tupla = (1,-2, 3)
a, b, c = tupla
print("a =", a)
print("b =", b)
print("c =", c)
 #Se asignan variables a la tupla que representen cda uno de los datos

tupla= (11,9,-2,3,8,5)
var1,var2,var3=(tupla[i]for i in(1,3,5))
print("var1=",var1,",var2=",var2,",var3=",var3)
var1,var2,var3=((tupla[i]for i in range(0,6,2)))
print("var1=",var1,",var2=",var2,",var3=",var3)

#Basicamente i lo que hace que muestre el nnumero en esa posicion, el for in range nos dice que sera entre el valor 
#0 y 6 de dos en dos

def minmax(a,b):
    if a<b:
        return a,b
    else:
        return b,a
x,y=minmax(5,13)
print("min=",x,",","max=",y)
x,y=minmax(12,-4)
print("min=",x,",","max=",y)

t = ("4", "5","-1", "6", "7")
print(max(t))
print(min(t))