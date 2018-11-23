import sqlite3

class DataBase():
    conexion = sqlite3.connect('SummonerDB.db')
    cursor = conexion.cursor()

    cursor.execute('''CREATE TABLE Summoner
                (Id int PRIMARY KEY NOT NULL,
                 Name text NOT NULL,
                 Level int NOT NULL,
                 Wins int NOT NULL,
                 Losses int NOT NULL,
                 Tier text NOT NULL,
                 Comportamiento text NULL) ''')

    #cursor.execute("INSERT INTO Summoner (Id, Name, Level, Wins, Losses, Tier, Comportamiento) VALUES (17544320, 'l Irving l', 46, 88, 66, 'PLATINUM', 'aqui va el comportamiento')")
    conexion.commit()
    conexion.close()
if __name__ == '__main__':
    DataBase()
