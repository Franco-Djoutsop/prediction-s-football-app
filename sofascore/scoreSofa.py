import json
with open('sofascoreLive.json') as f:
    jsondata=json.load(f)
    
# sport=jsondata['events'][0]['tournament'].sport('name')
# sport=jsondata['events'][0]['tournament']['category']['sport']['name']
# league=jsondata['events'][0]['tournament']['name']
# hometeam=jsondata['events'][0]['homeTeam']['name']
# homescore=jsondata['events'][0]['homeScore']['current']
# awayteam=jsondata['events'][0]['awayTeam']['name']
# awayscore=jsondata['events'][0]['awayScore']['current']

for gameLive in jsondata['events']:
    sport=gameLive['tournament']['category']['sport']['name']
    league=gameLive['tournament']['name']
    hometeam=gameLive['homeTeam']['name']
    homescore=gameLive['homeScore']['current']
    awayteam=gameLive['awayTeam']['name']
    awayscore=gameLive['awayScore']['current']

    print(sport," |--> ",league,":",hometeam,homescore,"-",awayteam,awayscore)