"""
    creación de clases
"""

class Persona(object):
    """
    """
    
    def __init__(self, n, ape, ed, cod, nota1, nota2):# Contructor que resive 6 parametros(nombre, apellido, edad, codigo, nota1 y nota2) 
        """
        """
        self.nombre = n
        self.edad = int(ed)
        self.codigo = int(cod)
        self.apellido = ape
        self.nota1 = int(nota1)
        self.nota2 = int(nota2)

    def agregar_nombre(self, n):
        """
        """
        self.nombre = n

    def obtener_nombre(self):
        """
        """
        return self.nombre

    def agregar_edad(self, n):
        """
        """
        self.edad = int(n)

    def obtener_edad(self):
        """
        """
        return self.edad

    def agregar_codigo(self, n):
        """
        """
        self.codigo = int(n)

    def obtener_codigo(self):
        """
        """
        return self.codigo

    def obtener_apellido(self):
        """
        """
        return self.apellido

    def agregar_nota1(self, n):
        """
        """
        self.nota1 = int(nota1)

    def obtener_nota1(self):
        """
        """
        return self.nota1

    def agregar_nota2(self, n):
        """
        """
        self.nota2 = int(nota2)

    def obtener_nota2(self):
        """
        """
        return self.nota2

    def __str__(self):#Muestra los datos que retorna la clase 
        """
        """
        return "%s - %s - %d - %d - %d - %d" % (self.nombre, self.apellido,\
                self.edad, self.codigo, self.nota1,self.nota2)


class OperacionesPersona(object):
    """
    """
    
    def __init__(self, listado):
        """
        """
        self.listado_personas = listado
    def obtener_promedio_n1(self):#Calcula el promedio de la nota 1
        suma = 0
        print("Promedio nota1")
        for n in self.listado_personas:
            suma = suma + n.obtener_nota1()#Aculumador que suma las notas 1
        promedio = suma / len(self.listado_personas)# Calcula el promedio mediante la suma de las 1 y el tamaño de la lista 
        return promedio 
    def obtener_promedio_n2(self):# Calcula el promedio de la nota 2
        suma = 0
        print("Promedio nota2")
        for n in self.listado_personas:
            suma = suma + n.obtener_nota2()# Acumulador que suma las notas 2 
        promedio = suma / len(self.listado_personas)# Calcula el promedio mediante la suma de las notas 2 y el tamaño de la lista 
        return promedio

    def obtener_listado_n1(self):#Muestra las personas con nota1 menor a 15 
        cadena = ""
        print ("Personas con nota1 menor a 15 ")
        for n in self.listado_personas:
            if(n.obtener_nota1() < 15):#Preguntamos si la nota1 es menor a 15 
                cadena = "%s - %s - %s - %d\n" % (cadena, n.obtener_nombre(), n.obtener_apellido(), n.obtener_nota1())#Realizamos concatenacion de cadenas para retornar los datos
        return cadena          
               

    def obtener_listado_n2(self):#Muestra las personas con nota2 menor a 15 
        cadena = ""
        print("Personas con nota2 menor a 15")
        for n in self.listado_personas:
            if(n.obtener_nota2() < 15):#Preguntamos si la nota2 menor a 15 
                cadena = "%s - %s - %s - %d\n" % (cadena, n.obtener_nombre(), n.obtener_apellido(), n.obtener_nota2())#Realizamos concatenacion de cadenas para retornarlos datos 
        return cadena
    def obtener_listado_personas(self, m1, m2): #Resive dos parametros y Muestra a personas con nombre que empiesan con J o R   
        cadena = ""
        print("listado de personas que empiezan con J y R")
        for n in self.listado_personas:
            if(n.obtener_nombre()[0] == m1 or n.obtener_nombre()[0] == m2):#Preguntamos si el nombre empiesa con J o R
                cadena = "%s - %s - %s \n" % (cadena, n.obtener_nombre(), n.obtener_apellido())#Realizamos concatenacion de cadenas 
        return cadena   

    def __str__(self):#Muestra los datos que retorna la clase
        cadena = " "
        for n in self.listado_personas:
            cadena = "%s - %s - %s\n" % (cadena, n.obtener_nombre(), n.obtener_apellido())#Realizamos concatenacion de cadenas para retornar los datos  
        return cadena

