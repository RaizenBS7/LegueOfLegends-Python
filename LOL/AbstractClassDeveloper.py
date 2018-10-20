from abc import ABC, abstractmethod

class Invocador():
	def __init__(self, Id, Name, Level, Wins, Losses, Tier, Comportamiento = None):
		self.Id = id
		self.Name = Name
		self.Level = Level
		self.Wins = Wins
		self.Losses = Losses
		self.Tier = Tier
		self.Comportamiento = Comportamiento

###################################################################################################################

class Comportamiento():
	def __init__(self, Name):
		self.Name = Name

###################################################################################################################

class AbstractLOL(ABC):

	@abstractmethod
	def CrearInvocador(self, invocador):
		#Toma como parámetro nombre (instancia clase iNVOCADOR) y lo guarda en la BD.
		pass

	@abstractmethod
	def ConsultarInvocador(self, Name):
        #regresa un invocador que este guardado en la db
		pass

	@abstractmethod
	def ModificarInvocador(self):
    	#toma un objeto tipo invocador y asigna nuevos parametros que se almacenaran en la db
		pass

	@abstractmethod
	def BorrarInvocador(self, Name):
        #Toma el nombre de un invocador y lo borra de la base de datos
		pass

###################################################################################################################
class AbstractSummoner(ABC):
	@abstractmethod
	def DatosSummoner(self, name):
		#esta clase toma el nombre del invocador y retorna un objeto de tipo Invocador
		pass

if __name__ == "__main__":
	comportamiento = Comportamiento('Nombre')
	print(comportamiento.Name)
