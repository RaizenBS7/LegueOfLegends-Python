import requests
from AbstractClassDeveloper import Invocador
from AbstractClassDeveloper import AbstractSummoner
import sys

#summoner = 'Raizen%20blackshot'

class AppInvocador(AbstractSummoner):
    def DatosSummoner(self, summoner):
        key = 'RGAPI-d5b1e6ba-b6f1-421c-be14-e0dcef5a4d1a'
        region = 'la1'

        chall_r = requests.get('https://' + region + '.api.riotgames.com/lol/summoner/v3/summoners/by-name/' + summoner + '?api_key=' + key)
        if(chall_r.status_code == 200):
            chall_J = chall_r.json()
            Id = chall_J['id']
            Name = chall_J['name']
            Level = chall_J['summonerLevel']
#            print(Id, Name, Level)
            Id = str(Id)
        chall_m = requests.get('https://' + region + '.api.riotgames.com/lol/league/v3/positions/by-summoner/' + Id + '?api_key=' + key)
        if(chall_m.status_code == 200):
            chall_n = chall_m.json()
#            print(chall_n[2])
            Wins =chall_n[2]['wins']
            Losses = chall_n[2]['losses']
            Tier = chall_n[2]['tier']
#            print(Tier, Wins, Losses)
        return Invocador(Id, Name, Level, Wins, Losses, Tier)

if __name__ == "__main__":
    player = AppInvocador()
    summoner = player.DatosSummoner('Raizenblackshot')

#Prueba para testing | que pasa cuando no tiene ranket registradas el summoner
