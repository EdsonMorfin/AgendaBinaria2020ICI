"""Desarrolle un programa que manipule una agenda en un archivo binario, dicha agenda debe
contemplar las operaciones de: 
Agregar
Eliminar
Mostrar Agenda
Modificar
La agenda debe
contemplar los siguientes campos : Clave, Nombre, Teléfono, Domicilio."""

from io import open
import pickle

class Agenda:

    # Constructor de clase
    def __init__(self, clave,nombre,telefono,domicilio):
        self.clave = clave
        self.nombre = nombre
        self.telefono = telefono
        self.domicilio = domicilio

        print('Se ha agredado una nueva direccion:',self.nombre,' ',self.telefono,' ',self.domicilio,'con la posicion:',self.clave)

    def __str__(self):
        return '{}({} {} {})'.format(self.clave,self.nombre,self.telefono,self.domicilio)


class Catalogo:

    agenda = []

    # Constructor de clase
    def __init__(self):
        self.cargar()

    def agregar(self,p):
        self.agenda.append(p)
        self.guardar()

    def mostrar(self):
        if len(self.agenda) == 0:
            print("La agenda esta vacia está vacío")
            return
        for p in self.agenda:
            print(p)

    def cargar(self):
        fichero = open('agenda.pckl', 'ab+')
        fichero.seek(0)
        try:
            self.agenda = pickle.load(fichero)
        except:
            print("El fichero está vacío")
        finally:
            fichero.close()
            print("Se han cargado {} entradas".format(len(self.agenda)))

    def guardar(self):
        fichero = open('agenda.pckl', 'wb')
        pickle.dump(self.agenda, fichero)
        fichero.close()
        
    def eliminar(self,dato):
        pickled_file = open('agenda.pckl','rb')
        data = pickle.load(pickled_file)
        index=self.agenda.index(data[dato])
        self.agenda.remove(index)
        pickled_file.close
        
    def modificar(self,indice,data)
        eliminar(indice)
        agregar(data)        

        