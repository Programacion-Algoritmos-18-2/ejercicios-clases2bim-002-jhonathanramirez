from paquete_archivos.miarchivo import MiArchivo
from paquete_modelo.mimodelo import Persona, OperacionesPersona

m = MiArchivo()
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista] # Separa la lista con un pipe

# print(lista)

lista = lista[1:] # Designa la posicion en la lista  
lista_personas = []
# p = Persona(lista[1][1], lista[1][2], lista[1][3], lista[1][0])
for d in lista:
    # print(d)
    p = Persona(d[1], d[2], d[3], d[0],d[4],d[5]) # Objeto tipo persona
    lista_personas.append(p)
    #print(p)
operaciones = OperacionesPersona(lista_personas) # listado de Objetos 
#print(operaciones)   
print(operaciones.obtener_promedio_n1()) # imprime el metodo que calcula el promedio nota1
print(operaciones.obtener_promedio_n2()) # imprime el metodo que calcula el promedio nota2
print(operaciones.obtener_listado_n1())  # imprime el metodo que calcula las personas con nota 1 menor a 15 
print(operaciones.obtener_listado_n2())  # imprime el metodo que calcula las personas con nota 2 menor a 15
print(operaciones.obtaener_listdo_personas("R", "J")) # imprime el metodo que calcula que la persona empiece con J o R