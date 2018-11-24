import unittest
from unittest.mock import Mock #permite reemplazar partes de su sistema bajo prueba con objetos simulados y hacer afirmaciones sobre cómo se han utilizado
from Summoner import AppInvocador
from SqlCRUD import SqlCRUD
from AbstractClassDeveloper import Invocador, AbstractLOL, AbstractSummoner
#(1166018, 'Raizen blackshot', 114, 132, 129, 'PLATINUM', None)
#(402492, 'jarasdeboy', 119, 173, 192, 'PLATINUM', None)
class TestSummoner(unittest.TestCase):
    def setUp(self): #Iniciador donde dare datos iniciales para la prueba que seran mas tarde reescribidos
        self.Summ = AppInvocador() #conecto con la clase AppInvocador Del archivo Summoner.py
        self.SQL = SqlCRUD() #Abro la coneccion con la DB
        print('Invocador guarado correctamente')

    def tearDown(self): #Finalizo la prueba del mock
        print("Fin de la prueba")

#    def test_close(self): #En este test pruebo que la coneccion a la DB sea abirta, el cual nos regresara un mensaje de que se abrio correctamente
#        print("test_Open")
#        self.init = SQL.__init__()

    def SummonerTest(self):
        print("invocador_test")
        self.invocador1 = Summ.DatosSummoner('Raizen blackshot')
        self.assertEqual(self.invocador1.Id, 1166018)
        self.assertEqual(self.invocador1.Name, 'Raizen blackshot')
        self.assertEqual(self.invocador1.Level, 114 )
        self.assertEqual(self.invocador1.Wins, 132 )
        self.assertEqual(self.invocador1.Losses, 129 )
        self.assertEqual(self.invocador1.Tier, 'PLATINUM' )

    def CrearInvocador_test(self):
        print("CrearInvocador_test")
        self.assertIsInstance(self.SQL.CrearInvocador(self.Invocador), Invocador)

    def BorrarInvocador_test(self):
        print("BorrarInvocador_test")
        self.assertTrue(self.SQL.BorrarInvocador('jarasdeboy'))

if __name__ == '__main__':
    unittest.main()
