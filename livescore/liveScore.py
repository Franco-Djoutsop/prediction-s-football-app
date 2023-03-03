import requests
import json
url = "https://prod-public-api.livescore.com/v1/api/app/live/soccer/1"

querystring = {"MD":"1"}

payload = ""
headers = {
    "authority": "prod-public-api.livescore.com",
    "accept": "*/*",
    "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "origin": "https://www.livescore.com",
    "referer": "https://www.livescore.com/",
    # "sec-ch-ua": ""Chromium";v="109", "Not_A Brand";v="99"",
    "sec-ch-ua-mobile": "?1",
    # "sec-ch-ua-platform": ""Android"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

jsondata=json.loads(response.text)
with open('livescore.txt',"a+") as f:
    for live in jsondata['Stages']:
        league=live['Snm']
        teams=live['Events']
        for team in teams :
            hometeams=team['T1']
            awayteams=team['T2']
            for name in hometeams:
                hometeam=name['Nm']
                # print(hometeam)
            for name in awayteams:
                awayteam=name['Nm']
                # print(awayteam)
    
        for score in teams:
            if('Tr1' or 'Tr2' in score):
                homescore=score['Tr1']
                awayscore=score['Tr2']
                result=(league," |-->",hometeam,homescore,"-",awayscore,awayteam)
                f.write(str(result)+"/n")
            else:
                print('ce match match viens de s\'achever')
    f.close()