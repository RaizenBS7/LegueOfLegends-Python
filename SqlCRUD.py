import	sqlite3
from Summoner import *
from AbstractClassDeveloper import *
import sys

class SqlCRUD(AbstractLOL):

    def __init__(self):
        self.conexion = sqlite3.connect('SummonerDB.db')
        self.cursor = self.conexion.cursor()

    def CrearInvocador(self, Invocador):
        inv = (Invocador.Id, Invocador.Name, Invocador.Level, Invocador.Wins, Invocador.Losses, Invocador.Tier, Invocador.Comportamiento)
        self.cursor.execute("INSERT INTO Summoner (Id, Name, Level, Wins, Losses, Tier, Comportamiento) VALUES (?,?,?,?,?,?,?)", inv)
        self.conexion.commit()#guarda cambios
        Invocador.Name = self.cursor.lastrowid
        return Invocador

    def MostrarLista(self):
        self.cursor.execute("SELECT * from Summoner")
        for Summoner in self.cursor.fetchall():
            summ = Invocador(Summoner[1], Summoner[2], Summoner[3], Summoner[4], Summoner[5], Summoner[6], Summoner[0])
            print(Summoner)

    def ConsultarInvocador(self, Name):
        self.cursor.execute("SELECT * from Summoner where Name = ?", [Name])
        for Summoner in self.cursor.fetchall():
            summ = Invocador(Summoner[0], Summoner[1], Summoner[2], Summoner[3], Summoner[4], Summoner[5], Summoner[6])
        return print(summ)

    def ModificarInvocador(self, Comportamiento):
        inv = (Comportamiento.Comportamiento, Comportamiento.Name)
        self.cursor.execute("UPDATE Summoner SET Comportamiento=? where Name=?", inv)
        self.conexion.commit()

    def BorrarInvocador(self, Name):
        self.cursor.execute("DELETE from Summoner WHERE Name=?", [Name])
        self.conexion.commit()
        return True

if __name__ == "__main__":
    player = AppInvocador()
    crud = SqlCRUD()
#    invocador1 = player.DatosSummoner('Raizen blackshot')
#    invocador2 = player.DatosSummoner('SleightTheBeast')
#    invocador3 = player.DatosSummoner('l irving l')
#    NewInvocador = crud.CrearInvocador(invocador3)
#    NewConsulta = crud.ConsultarInvocador('l Irving l')
    ConsultarInvocador = crud.ConsultarInvocador('Raizen blackshot')
#    Borrar = crud.BorrarInvocador('l Irving l')
#    Borrar = crud.BorrarInvocador('Raizen blackshot')
#    comp= Comportamiento('l Irving l', 'Toxico el chavo')
#    Modificar = crud.ModificarInvocador(comp)
