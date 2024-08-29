#items () devuelve las key (claves) y values (valores) del diccionario . 

d={"a":1, "b":2, "c":3, "d":5}
id=d.items()
print(id)
#print(d.items())

#keys() devuelve un lista de las key (claves) 

k= d.keys() # devuelve la lista de la clave
print(k) # muestra las clave del diccionario
print(list(k)) #imprime como lista

# values() devuelve un lista los valores del diccionario

v=d.values()

print(v) # muestra los valores del diccionario
print(list(v)) #imprime como lista

#pop()  busca y elimina la clave que se pasa como parametros y devuelve su valor asociado 
d.pop("a")
print(d)

#popitem() busca y elimina la clave aleatorio 

d.popitem()
print(d)

# update() se llama sobre el diccion y tiene como entrada otro diccionario

d2={"a:":1, "b":2, "c":3, "e":4 , "d":5}
d.update(d2)
print(d)


 