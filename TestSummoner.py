import unittest
from unittest.mock import Mock #permite reemplazar partes de su sistema bajo prueba con objetos simulados y hacer afirmaciones sobre cómo se han utilizado
from Summoner import AppInvocador
from SqlCRUD import SqlCRUD
from AbstractClassDeveloper import Invocador, AbstractLOL, AbstractSummoner
#(1166018, 'Raizen blackshot', 114, 132, 129, 'PLATINUM', None)
#(402492, 'jarasdeboy', 119, 173, 192, 'PLATINUM', None)
class TestSummoner(unittest.TestCase):
    def setUp(self): #Iniciador donde dare datos iniciales para la prueba que seran mas tarde reescribidos
        self.summ = AppInvocador() #conecto con la clase AppInvocador Del archivo Summoner.py
        self.sql = SqlCRUD() #Abro la coneccion con la DB
    #    self.sql.CrearInvocador(self.Invocador)
        self.invocador1 = Invocador(1166018, 'Raizen blackshot', 115, 132, 129, 'PLATINUM', None)
#        print('Invocador guarado correctamente')

    def tearDown(self): #Finalizo la prueba del mock
        print("Fin de la prueba")

    def test_summoner(self):
        self.invocador1 = self.summ.DatosSummoner('Raizen blackshot')
        print("test_summoner")
        self.assertEqual(self.invocador1.Id, 1166018)
        self.assertEqual(self.invocador1.Name, ('Raizen blackshot'))
        self.assertEqual(self.invocador1.Level, 115 )
        self.assertEqual(self.invocador1.Wins, 132 )
        self.assertEqual(self.invocador1.Losses, 129 )
        self.assertEqual(self.invocador1.Tier, 'PLATINUM' )
        self.assertEqual(self.invocador1.Comportamiento, None )

    def test_CrearInvocador(self):
        print("test_CrearInvocador")
        self.assertIsInstance(self.sql.CrearInvocador(self.invocador1), Invocador)

    def test_BorrarInvocador(self):
        print("test_BorrarInvocador")
        self.assertTrue(self.sql.BorrarInvocador('Raizen blackshot'))

if __name__ == '__main__':
    unittest.main()
