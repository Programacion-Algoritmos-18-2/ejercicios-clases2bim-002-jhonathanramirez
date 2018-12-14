import  codecs #Importamos las librerias 
import sys

# sys.path.append('./')
from paquete_modelo.mimodelo import Persona

class MiArchivo:
    """
    """
    
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/demo_notas.csv", "r") # Abrimos el archivo y asignamos la direccion  

    def obtener_informacion(self):
        return self.archivo.readlines()

    def cerrar_archivo(self): # Cierra el archivo 
        self.archivo.close()


class MiArchivoEscribir:
    """
    """
    
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/demo2.csv", "a") # Abrimos el archivo y asignamos la direccion 

    def agregar_informacion(self, p):
        self.archivo.write("%s-%s-%d-%d\n" % (p.nombre, p.apellido,\
                p.edad, p.codigo))

    def cerrar_archivo(self): # Cierra el archivo 
        self.archivo.close()
