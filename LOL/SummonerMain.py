from AbstractClassDeveloper import *
from SqlCRUD import *
from Summoner import *
from time import sleep

def MainLOL():
	player = AppInvocador()
	crud = SqlCRUD()
	while True:
		opcion = int(input('''Bienvenido al sistema de menu.
	Usted Desea:
	1.-Guardar Invocador
	2.-Mostrar Lista
	3.-Mostrar Invocador
	4.-Modificar Invocador
	5.-Eliminar Invocador
	0.-Salir del menu \n'''))

		if opcion == 1: #Guardar datos de invocador en la DB
			Summoner = input('Name un nombre del invocador:		')
			invocador= player.DatosSummoner(Summoner)
			newinvocador = crud.CrearInvocador(invocador)
			print("Se ha guardado el nuevo Invocador con exito (°w°)/")
			sleep(1)
			print('\n')
			continue

		elif opcion == 2: #Consultar la lista completa de invocadores del a DB
			print('Esta es la lista de invocadores (°w°)/: ')
			ConsultarLista = crud.MostrarLista()
			print(ConsultarLista)
			sleep(1)
			print('\n')
			continue

		elif opcion == 3: #Mostrar un invocador en especifico de la DB
			Summoner=input("Ingresa el Nombre del Invocador:	")
			NewConsulta = crud.ConsultarInvocador(Summoner)
			print(NewConsulta)
			sleep(1)
			print('\n')
			continue

		elif opcion == 4:
			summoner = input("Ingrese el nombre de invocador a modificar:	")
			NewConsulta = crud.ConsultarInvocador(summoner)
			print(NewConsulta)
			sleep(1)
			comp = Comportamiento(summoner, input('Ingrese el comportamiento del invocador:	'))
			summ = crud.ModificarInvocador(comp)
			sleep(1)
			print("Se ah modificado exitosamente el invocador (°w°)/")
			print('\n')
			continue

		elif opcion == 5: #Borrar al invocador de la lista de DB
			Summoner=input("Ingresa el Nombre del Invocador:	")
			borrarInv=crud.BorrarInvocador(Summoner)
			print("Invocador eliminado")
			sleep(1)
			print('\n')
			continue

		if opcion == 0: #Salir del programa main
			print("Que tenga un exelente dia (°w°)/....bye bye")
			break

if __name__ == '__main__':
	MainLOL()
