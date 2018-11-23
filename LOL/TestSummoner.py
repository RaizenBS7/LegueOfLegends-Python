import unittest
from unittest.mock import Mock #permite reemplazar partes de su sistema bajo prueba con objetos simulados y hacer afirmaciones sobre cómo se han utilizado
from Summoner import AppInvocador
from SqlCRUD import SqlCRUD
from AbstractClassDeveloper import Invocador, AbstractLOL, AbstractSummoner
#(1166018, 'Raizen blackshot', 114, 132, 129, 'PLATINUM', None)
#(402492, 'jarasdeboy', 119, 173, 192, 'PLATINUM', None)
class TestSummoner(unittest.TestCase):
    def SetUp(self): #Iniciador donde dare datos iniciales para la prueba que seran mas tarde reescribidos
        self.Summ = AppInvocador() #conecto con la clase AppInvocador Del archivo Summoner.py
        self.SummMock = Mock(Id = Summ.DatosSummoner('jarasdeboy').Id, Name = Summ.DatosSummoner('jarasdeboy').Name, Level = Summ.DatosSummoner('jarasdeboy').Level, Wins = Summ.DatosSummoner('jarasdeboy').Wins, Losses = Summ.DatosSummoner('jarasdeboy').Losses, Tier = Summ.DatosSummoner('jarasdeboy').Tier, Comportamiento = 'Toxico el men')
        self.Invocador = Invocador(self.SummMock.Id, self.SummMock.Name, self.SummMock.Level, self.SummMock.Wins, self.SummMock.Losses, self.SummMock.Tier)
        self.SQL = SqlCRUD() #Abro la coneccion con la DB
        self.SQL.CrearInvocador(self.Invocador)
        print('Invocador guarado correctamente')
        self.invocador1 = Invocador(1166018, 'Raizen blackshot', 114, 132, 129, 'PLATINUM')

    def tearDown(self): #Finalizo la prueba del mock
        print("Fin de la prueba")

    def test_close(self): #En este test pruebo que la coneccion a la DB sea abirta, el cual nos regresara un mensaje de que se abrio correctamente
        print("test_Open")
        self.SQL = SqlCRUD()
        self.assertTrue(self.sql.Open())

    def SummonerTest(self):
        print("invocador_test")
        self.assertEqual(self.invocador1.Id, 1166018)
        self.assertEqual(self.invocador1.Name, 'Raizen blackshot')
        self.assertEqual(self.invocador1.Level, 114 )
        self.assertEqual(self.invocador1.Wins, 132 )
        self.assertEqual(self.invocador1.Losses, 129 )
        self.assertEqual(self.invocador1.Tier, 'PLATINUM' )

    def CrearInvocador_test(self):
        print("CrearInvocador_test")
        self.assertIsInstance(self.sql.CrearInvocador(self.Invocador), Invocador)

    def BorrarInvocador_test(self):
        print("BorrarInvocador_test")
        self.assertTrue(self.sql.BorrarInvocador('jarasdeboy'))

if __name__ == '__main__':
    unittest.main()
