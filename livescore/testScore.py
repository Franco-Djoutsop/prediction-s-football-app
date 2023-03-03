import json
with open('/home/franck_lf/root python/livescore/resultLiveScore.json') as f:
    jsondata=json.load(f)
    league=jsondata['Stages'][0]['Snm']
    hometeam=jsondata['Stages'][0]['Events'][0]['T1'][0]['Nm']
    awayteam=jsondata['Stages'][0]['Events'][0]['T2'][0]['Nm']
    
    homescore=jsondata['Stages'][0]['Events'][0]['Tr1']
    awayscore=jsondata['Stages'][0]['Events'][0]['Tr2']

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
        homescore=score['Tr1']
        awayscore=score['Tr2']
    
    print(league,"|-->",hometeam,homescore,"-",awayscore,awayteam)