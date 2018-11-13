import requests
from AbstractClassDeveloper import Invocador
from AbstractClassDeveloper import AbstractSummoner
import sys

class AppInvocador(AbstractSummoner):

    def DatosSummoner(self, summoner):
        key = 'RGAPI-8e853297-ce9d-41c0-923f-2fb2e7e1eb20'
        region = 'la1'

        chall_r = requests.get('https://' + region + '.api.riotgames.com/lol/summoner/v3/summoners/by-name/' + summoner + '?api_key=' + key)
        if(chall_r.status_code == 200):
            chall_J = chall_r.json()
            Id = chall_J['id']
            Name = chall_J['name']
            Level = chall_J['summonerLevel']

        chall_m = requests.get('https://' + region + '.api.riotgames.com/lol/league/v3/positions/by-summoner/' + str(Id) + '?api_key=' + key)

        if(chall_m.status_code == 200):
            chall_n = chall_m.json()

        Wins = 0
        Losses = 0
        Tier = 'No tiene partidas en ranked'

        for i in chall_n:
            if i['queueType'] == 'RANKED_SOLO_5x5': #Veriacion que sea el diccionario de soloQ
                Wins = i['wins']
                Losses = i['losses']
                Tier = i['tier']

        return Invocador(Id, Name, Level, Wins, Losses, Tier)


if __name__ == "__main__":
    player = AppInvocador()
#    summoner = player.DatosSummoner('Raizen blackshot')
#    print(summoner)
