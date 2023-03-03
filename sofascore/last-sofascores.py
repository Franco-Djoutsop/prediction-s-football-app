import requests
import json
from bs4 import BeautifulSoup
import sys
url='https://www.livescore.com/en/football/spain/copa-del-rey/real-madrid-vs-barcelona/891654/h2h/'
response=requests.get(url)
html_content=response.text
soup=BeautifulSoup(html_content,'html.parser')
hometeam=[]
homescores=[]
awayscores=[]
awayteam=[]
list_scores=[]
list_teams=[]


#la variable leagues recooit la liste de tous les div qui ont la class "Jo"
leagues=soup.find('div',class_='vo')

#cette boucle permet de parcourir la liste teams_tables pour recuper toutes les div qui ont la class "To" et stocker le resultat dans la variable team_table
teams_tables=soup.find_all('div',class_='Co')
for score in teams_tables:
    scores=score.find_all('div',class_='Go')
    for score in scores:
        homescore=score.find_all('div',class_='Ho')[0].find_all('div')[0].text
        awayscore=score.find_all('div',class_='Ho')[0].find_all('div')[1].text
        homescores.append(homescore)
        awayscores.append(awayscore)
        
for team  in teams_tables:
    team_table=team.find('div',class_='Fo').find_all('div',class_='Io')

    for teams in team_table:
        team=teams.find_all('span')[-1].text
        teamexcept=teams.find_all('span')
        
        #cette condition c'est pour echapper aux erreurs
        if len(teamexcept)==4:
            team=(teams.find_all('span')[-2].text)
            list_teams.append((team))
        else:
            team=teams.find_all('span')[-1].text
            list_teams.append((team)) 

for i in range(0,len(list_teams),2):
    hometeam.append(list_teams[i])
for i in range(0,len(list_teams),2):
    awayteam.append(list_teams[i+1])
    
    
    
    
    
    
    
with open('barcelone.json','a') as f:
    # f.write("Last-Matchs-of-barcelone")
    for i in range(len(awayscores)):
    # print(list_teams[i],list_scores[id])
        result=(hometeam[i]+" "+homescores[i]+" - "+awayscores[i]+" "+awayteam[i])
        f.write("{}\n".format(result))
        