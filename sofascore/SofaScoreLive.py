import requests
import json
url = "https://api.sofascore.com/api/v1/sport/football/events/live"

payload = ""
headers = {
    "authority": "api.sofascore.com",
    "accept": "*/*",
    "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    # "if-none-match": "W/"fe8b6fe157"",
    "origin": "https://www.sofascore.com",
    "referer": "https://www.sofascore.com/",
    # "sec-ch-ua": ""Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"",
    "sec-ch-ua-mobile": "?0",
    # "sec-ch-ua-platform": ""Linux"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

response = requests.request("GET", url, data=payload, headers=headers)

jsondata=json.loads(response.text)
# sport=jsondata['events'][0]['awayTeam']['sport']['name']
# league=jsondata['events'][0]['tournament']['name']
# hometeam=jsondata['events'][0]['homeTeam']['name']
# homescore=jsondata['events'][0]['homeScore']['current']
# awayteam=jsondata['events'][0]['awayTeam']['name']
# awayscore=jsondata['events'][0]['awayScore']['current']
# print(sport)

# for gameLive in jsondata['events']:
#     sport=gameLive['awayTeam']['sport']['name']
#     league=gameLive['tournament']['name']
#     hometeam=gameLive['homeTeam']['name']
#     homescore=gameLive['homeScore']['current']
#     awayteam=gameLive['awayTeam']['name']
#     awayscore=gameLive['awayScore']['current']
#     print(sport,"|-->",league,":",hometeam,homescore,"-",awayscore,awayteam)
matchs=[]
with open('sofascoreLive.txt','a+') as f:
    lignes=f.readlines()
    for gameLive in jsondata['events']:
        sport=gameLive['awayTeam']['sport']['name']
        league=gameLive['tournament']['name']
        hometeam=gameLive['homeTeam']['name']
        homescore=gameLive['homeScore']['current']
        awayteam=gameLive['awayTeam']['name']
        awayscore=gameLive['awayScore']['current']
        result=(sport,"|-->",league,":",hometeam,homescore,"-",awayscore,awayteam)
        f.write(str(result)+"\n")
        
    # if(result in lignes):
    #     print('non je suis deja la')
    # else:
    #     with open('score_16_02_2023.json','a+') as f:
    #         f.write(str(result)+"\n")
    #         f.close()

    f.close()
    
    # with open('score_17-02-23.txt','r+') as f:
    # lignes=f.readlines()
    # if homescore in lignes:
    #     pass
    # else:
    #     with open('score_17-02-23.txt','a+') as f:
    #         f.write(str(result)+"\n")
    #         f.close()
    
