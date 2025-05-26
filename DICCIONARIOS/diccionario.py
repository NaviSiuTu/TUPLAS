dict_ports1={22:"SSH",80:"Http"}
dict_ports2={53:"DNS",443:"https"}
print(dict_ports1)
dict_ports1.update(dict_ports2) #Agrega el puerto 2, quedando valores d ambos desordenados
print(dict_ports1)

p = dict_ports1 [80]
print (p)

#COMO PUEDO ELIMINAR UN DATO DE UN DICCIONARIO?
puertos={22:"SSH", 23:"Telnet",80:"HTTP",3306:"MySQL"}
print(puertos)
del puertos[23] #Metodo 
print(puertos)

#Como mostrar la dupla (con clave y dato)

dict_ports = {22:"SSH", 23:"telnet", 80:"Http"}
for k,v in dict_ports.items():
#print(k, "->", v)

#Tambien se puede usar el .get

    puertosos = {80:"HTTP", 23:"SMTP", 443: "HTTPS"}
print(max(puertosos))
print(min(puertosos))
print("----------------------------------------------")
#Aqui si no puedes hacer "443" ya que la clave siepre debe ser de un mismo tipo de dato

puertosos = {"80":"HTTP", "23":"SMTP", "443": "HTTPS"}
print(max(puertosos))
print(min(puertosos))