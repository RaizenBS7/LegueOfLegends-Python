import sqlite3
from AbstractClassDeveloper import *

class DataBase(AbstractLOL):
    def __init__(slef):
        self.conexion = sqlite3.connect('Summoner.db')
        self.cursor = self.conexion.cursor()

	def CrearInvocador(self, invocador):
        #Coneccion para agregar summoner a la db

	def ConsultarInvocador(self, Name):
        #Coneccion para consultar datos de un summoner mediante su Nombre

	def ModificarInvocador(self):
        #Coneccion para modificar los datos de un summoner en la db

	def BorrarInvocador(self, Name):
        #Coneccion para quitar a un summoner de la DB

    def Close(self):
        self.conexion.close()
        return 'Terminar coneccion con DB'
