import requests
import json
url = "https://prod-public-api.livescore.com/v1/api/app/date/soccer/20230215/1"

querystring = {"MD":"1"}

payload = ""
headers = {
    "authority": "prod-public-api.livescore.com",
    "accept": "*/*",
    "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "origin": "https://www.livescore.com",
    "referer": "https://www.livescore.com/",
    # "sec-ch-ua": ""Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"",
    "sec-ch-ua-mobile": "?0",
    # "sec-ch-ua-platform": ""Linux"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
jsondata=json.loads(response.text)

# rounded=jsondata['Stages'][0]["Snm"]
# league=jsondata['Stages'][0]["Ccd"]
# hometeam=jsondata['Stages'][0]['Events'][0]['T1'][0]['Nm']
# homescore=jsondata['Stages'][0]['Events'][0]["Tr1"]

# awayteam=jsondata['Stages'][0]['Events'][0]['T2'][0]['Nm']
# awayscore=jsondata['Stages'][0]['Events'][0]["Tr2"]
# print(rounded," : ",league,"|-->",hometeam,homescore,"-",awayscore,awayteam)
# print(jsondata['Stages'][0]['Events'])

with open('score-15-02-23.json',"w+") as f: 
    for league in jsondata['Stages']:
        rounded=league["Snm"]
        leagues=league["Ccd"]
        scores=league['Events']
        
        for score in scores:
            hometeams=score['T1']
            awayteams=score['T2']
            if "Tr1" in score:
                homescore=score["Tr1"]
                awayscore=score["Tr2"]
            else:
                print("erreur de cle")
            
            for hteam in hometeams:
                hometeam=hteam['Nm']
            for ateam in awayteams:
                awayteam=ateam['Nm']
                
            result=(rounded," : ",leagues,"|-->",hometeam,homescore,"-",awayscore,awayteam)
            f.write(str(result)+"\n")
    f.close()