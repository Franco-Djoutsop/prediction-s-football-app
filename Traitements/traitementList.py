listData=[]
home_team_file="real_madrid.json"
away_team_file="barcelone.json"
name_home_search="Real"
second_name_home_search="Madrid"
name_away_search="Barcelona"
second_name_away_search=None
with open(home_team_file,"r") as f:
    datajson=f.readlines()
datajson.pop(0)
##recuper les elements de maniere separee 
for data in datajson:
    data_list=data.split(' - ')
    for data in data_list:
        listData.append(data.split(" "))
    

#BTTS Overall Home Team
def bbts_ofht():
    right_score=[]
    left_score=[]
    btts_ofht=[]
        #tous ce qui concerne le right part
    for i in range(0,len(listData),2):
        right_score.append(listData[i][-1])
    for i in range(1,len(listData),2):
        left_score.append(listData[i][0])

    for i,j in zip(right_score,left_score):
        if(int(i)>0 and int(j)>0):
            btts_ofht.append((i,j))
    return {"#BTTS Overall Home Team":len(btts_ofht)}

#BTTS overall for Away Team
def btts_ofat():
    listData=[]
    with open(away_team_file,"r") as f:
        datajson=f.readlines()
    datajson.pop(0)
    ##recuper les elements de maniere separee 
    for data in datajson:
        data_list=data.split(' - ')
        for data in data_list:
            listData.append(data.split(" "))
    right_score=[]
    left_score=[]
    btts_ofat=[]
        #tous ce qui concerne le right part
    for i in range(0,len(listData),2):
        right_score.append(listData[i][-1])
    for i in range(1,len(listData),2):
        left_score.append(listData[i][0])

    for i,j in zip(right_score,left_score):
        if(int(i)>0 and int(j)>0):
            btts_ofat.append((i,j))
    return {"#BTTS overall for Away Team":len(btts_ofat)}


#BTTS last 10 games home for Home Team
def btts_ofht_last_10():
    right_score=[]
    left_score=[]
    btts_ofht=[]
        #tous ce qui concerne le right part
    for i in range(0,10,2):
        right_score.append(listData[i][-1])
    for i in range(1,10,2):
        left_score.append(listData[i][0])

    for i,j in zip(right_score,left_score):
        if(int(i)>0 and int(j)>0):
            btts_ofht.append((i,j))
    return {"#BTTS last 10 games home for Home Team":len(btts_ofht)}

#BTTS last 10 games away for away Team
def btts_ofat_last_10():
    with open(away_team_file,"r") as f:
        datajson=f.readlines()
    datajson.pop(0)
    ##recuper les elements de maniere separee 
    for data in datajson:
        data_list=data.split(' - ')
        for data in data_list:
            listData.append(data.split(" "))
    
    right_score=[]
    left_score=[]
    btts_ofat=[]
        #tous ce qui concerne le right part
    for i in range(0,10,2):
        right_score.append(listData[i][-1])
    for i in range(1,10,2):
        left_score.append(listData[i][0])

    for i,j in zip(right_score,left_score):
        if(int(i)>0 and int(j)>0):
            btts_ofat.append((i,j))
    return {"#BTTS last 10 games away for away Team":len(btts_ofat)}


#Goals conceded by Home Team
def goal_cbht():
    goal_cbht=[]
    for i in listData:
        if((name_home_search in i[0] and second_name_home_search in i[1]) or (name_home_search in i[1] and second_name_home_search in i[2])):
            pass
        else:
            goal_cbht.append(i)
    input_int=[]
    result=0
    for i in goal_cbht:
        try:
            input_int.append(int(i[-1]))
        except ValueError:
            input_int.append(int(i[0]))
    for i in range(0,len(goal_cbht)):
        if(input_int[i]>0):
            result+=input_int[i]
        
    return {"#Goals conceded by Home Team":(result)}

#Goals conceded by away Team
def goal_cbat():
    listData=[]
    with open(away_team_file,"r") as f:
        datajson=f.readlines()
    datajson.pop(0)
    ##recuper les elements de maniere separee 
    for data in datajson:
        data_list=data.split(' - ')
        for data in data_list:
            listData.append(data.split(" "))
    goal_cbat=[]
    for i in listData:
        if(second_name_away_search==None):
            if(name_away_search in i[0]  or name_away_search in i[1]):
                pass
            else:
                goal_cbat.append(i)    
        else:
            if((name_away_search in i[0] and second_name_away_search in i[1]) or (name_away_search in i[1] and second_name_away_search in i[2])):
                pass
            else:
                goal_cbat.append(i)
    print(goal_cbat)
    input_int=[]
    result=0
    for i in goal_cbat:
        try:
            input_int.append(int(i[-1]))
        except ValueError:
            input_int.append(int(i[0]))
    for i in range(0,len(goal_cbat)):
        if(input_int[i]>0):
            result+=input_int[i]
        
    return {"#Goals conceded by away Team":(result)}

#number of goals conceeded in last 10 games home.
def goal_cbht_last_10():
    goal_cbht=[]
    for i in range(1,20,2):
        if(int(listData[i][0])>0):
            goal_cbht.append(int(listData[i][0]))
    result=0
    for i in goal_cbht:
        result+=i
    return {"number of goals conceeded in last 10 games home":(result)}

#number of goals conceeded in last 10 games away.
def goal_cbat_last_10():
    listData=[]
    with open(away_team_file,"r") as f:
        datajson=f.readlines()
    datajson.pop(0)
    ##recuper les elements de maniere separee 
    for data in datajson:
        data_list=data.split(' - ')
        for data in data_list:
            listData.append(data.split(" "))
    goal_cbat=[]
    for i in range(0,20,2):
        if(int(listData[i][-1])>0):
            goal_cbat.append(int(listData[i][-1]))
    result=0
    for i in goal_cbat:
        result+=i
    return {"number of goals conceeded in last 10 games away":(result)}
    
#Games during which home team made a clean sheet
def clean_cheet_home():
    datas=[]
    for i in listData:
        if(name_home_search in i[0]):
            datas.append(int(i[-1]))
        elif(name_home_search in i[-2]):
            datas.append(int(i[0]))
        else:
            pass
    clean_cheet_home=[]
    for i in datas:
        if(i==0):
            clean_cheet_home.append(i)
    return {"#Games during which home team made a clean sheet":(len(clean_cheet_home))}

#Games during which away team made a clean sheet
def clean_cheet_away():
    listData=[]
    with open(away_team_file,"r") as f:
        datajson=f.readlines()
    datajson.pop(0)
    ##recuper les elements de maniere separee 
    for data in datajson:
        data_list=data.split(' - ')
        for data in data_list:
            listData.append(data.split(" "))
    datas=[]
    for i in listData:
        if(name_away_search in i[0]):
            datas.append(int(i[-1]))
        elif(name_away_search in i[1]):
            datas.append(int(i[0]))
        else:
            pass
        
    clean_cheet_away=[]
    for i in datas:
        if(i==0):
            clean_cheet_away.append(i)
    
    return {"#Games during which away team made a clean sheet":(len(clean_cheet_away))}

#Games Home Team Made clean sheet home last 10 games
def clean_cheet_otl_10_home():    
    result=[]
    for i in range(0,20,2):
        if((int(listData[i][-1]))==0 and name_home_search in listData[i][0]):
            result.append(listData[i][-1])
            return {"#Games Home Team Made clean sheet home last 10 games":(len(result))}

#Games away Team Made clean sheet away last 10 games
def clean_cheet_otl_10_away():
    listData=[]
    with open(away_team_file,"r") as f:
        datajson=f.readlines()
    datajson.pop(0)
    ##recuper les elements de maniere separee 
    for data in datajson:
        data_list=data.split(' - ')
        for data in data_list:
            listData.append(data.split(" "))

    result=[]
    for i in range(1,20,2):
        if((int(listData[i][0]))==0 and name_home_search in listData[i][1]):
            result.append(listData[i][0])
            return {"#Games away Team Made clean sheet away last 10 games":(len(result))}

#BTTS home for home Team
def btts_hfht():
    listData=[]
    left_score_team_home=[]
    right_score_team_away=[]
    result=[]
    with open(home_team_file,"r") as f:
        datajson=f.readlines()
    datajson.pop(0)
    ##recuper les elements de maniere separee 
    for data in datajson:
        data_list=data.split(' - ')
        for data in data_list:
            listData.append(data.split(" "))
    for i in range(0,len(listData),2):
        if(second_name_home_search==None):
            if((name_home_search in listData[i][0]) and int(listData[i][-1])>0):
                right_score_team_away.append(listData[i][-1])
                left_score_team_home.append(listData[i+1][0])
        else:
            if(((name_home_search in listData[i][0]) and (second_name_home_search in listData[i][1])) and int(listData[i][-1])>0):
                right_score_team_away.append(listData[i][-1])
                left_score_team_home.append(listData[i+1][0])
    for i in left_score_team_home:
        if(int(i)>0):
            result.append(len(i))

    return {"#BTTS home for home Team":len(result)}
        

#BTTS Away for Away Team
def btts_afat():
    listData=[]
    left_score_team_home=[]
    right_score_team_away=[]
    result=[]
    with open(away_team_file,"r") as f:
        datajson=f.readlines()
    datajson.pop(0)
    ##recuper les elements de maniere separee 
    for data in datajson:
        data_list=data.split(' - ')
        for data in data_list:
            listData.append(data.split(" "))
    for i in range(1,len(listData),2):
        if(second_name_away_search==None):
            if((name_away_search in listData[i][1]) and int(listData[i][0])>0):
                right_score_team_away.append(listData[i][0])
                left_score_team_home.append(listData[i-1][-1])
        else:
            if(((name_away_search in listData[i][1])and second_name_away_search in listData[i][2]) and int(listData[i][0])>0):
                right_score_team_away.append(listData[i][0])
                left_score_team_home.append(listData[i-1][-1])
    for i in left_score_team_home:
        if(int(i)>0):
            result.append(len(i))

    return {"#BTTS Away for Away Team":len(result)}
        
#games home team did not score in last 10 games home.
def clean_cheet_team_home():
    listData=[]
    right_score_team_home=[]
    result=[]
    with open(home_team_file,"r") as f:
        datajson=f.readlines()
    datajson.pop(0)
    ##recuper les elements de maniere separee 
    for data in datajson:
        data_list=data.split(' - ')
        for data in data_list:
            listData.append(data.split(" "))
    for i in range(0,20,2):
        if((name_home_search in listData[i][0]) and int(listData[i][-1])==0):
            right_score_team_home.append(listData[i][-1])
    return {"#games home team did not score in last 10 games home":len(right_score_team_home)}
        
#games away team did not score in last 10 games away.
def clean_cheet_team_away():
    listData=[]
    right_score_team_away=[]
    result=[]
    with open(away_team_file,"r") as f:
        datajson=f.readlines()
    datajson.pop(0)
    ##recuper les elements de maniere separee 
    for data in datajson:
        data_list=data.split(' - ')
        for data in data_list:
            listData.append(data.split(" "))
    for i in range(1,20,2):
        if((name_away_search in listData[i][-1]) and int(listData[i][0])==0):
            right_score_team_away.append(listData[i][0])
    return {"#games away team did not score in last 10 games away":len(right_score_team_away)}

#games home team did not score in last 10 games overall
def clean_cheet_home_team_overall():
    listData=[]
    datas=[]
    result=[]
    with open(home_team_file,"r") as f:
        datajson=f.readlines()
    datajson.pop(0)
    ##recuper les elements de maniere separee 
    for data in datajson:
        data_list=data.split(' - ')
        for data in data_list:
            listData.append(data.split(" "))
    for i in listData:
        if(second_name_home_search==None):
            if(name_home_search in i[0]):
                datas.append(int(i[-1]))
            elif(name_home_search in i[1]):
                datas.append(int(i[0]))
            else:
                pass
        else:
            if(name_home_search in i[0] and second_name_home_search in i[1]):
                datas.append(int(i[-1]))
            elif(name_home_search in i[1] and second_name_home_search in i[2]):
                datas.append(int(i[0]))
            else:
                pass
    for i in range(10):
        if(datas[i])==0:
            result.append(datas[i])
        else:
            pass
    return {"#games home team did not score in last 10 games overall":len(result)}


#games away team did not score in last 10 games overall
def clean_cheet_away_team_overall():
    listData=[]
    datas=[]
    result=[]
    with open(away_team_file,"r") as f:
        datajson=f.readlines()
    datajson.pop(0)
    ##recuper les elements de maniere separee 
    for data in datajson:
        data_list=data.split(' - ')
        for data in data_list:
            listData.append(data.split(" "))
    for i in listData:
        if(name_away_search in i[0]):
            datas.append(int(i[1]))
        elif(name_away_search in i[-1]):
            datas.append(int(i[0]))
        else:
            pass
    for i in range(10):
        if(datas[i])==0:
            result.append(datas[i])
        else:
            pass
    return {"#games away team did not score in last 10 games overall":len(result)}

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        #insere un element a la fin de la liste
    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        current_node=self.head
        while current_node.next:
            current_node=current_node.next
        current_node.next=new_node
    
    #insere un element au debut de la liste
    def insert(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        
    def print_list(self):
        #affiche tous les elements de la liste
        current_node=self.head
        while current_node:
            print(current_node.data)
            current_node=current_node.next
    
    def delete(self,data):
        #supprime un element dans la liste
        if not self.head:
            return
        if self.head.data==data:
            self.head=self.head.next
            return
        current_node=self.head
        while current_node.next:
            if current_node.next.data==data:
                current_node.next=current_node.next.next
                return
            current_node=current_node.next
            
    def size(self):
        #retourne le nombre d'elelement dans la liste
        count=0
        current_node=self.head
        while current_node:
            count+=1
            current_node=current_node.next
        return count
    
home_team=LinkedList()
home_team.append(bbts_ofht())
home_team.append(btts_ofht_last_10())
home_team.append(goal_cbht())
home_team.append(goal_cbht_last_10())
home_team.append(clean_cheet_home())
home_team.append(clean_cheet_otl_10_home())
home_team.append(clean_cheet_team_home())
home_team.append(clean_cheet_home_team_overall())
home_team.append(btts_hfht())

away_team=LinkedList()
away_team.append(btts_ofat())
away_team.append(btts_ofat_last_10())
away_team.append(btts_afat())
away_team.append(goal_cbat())
away_team.append(clean_cheet_otl_10_away())
away_team.append(goal_cbat_last_10())
away_team.append(clean_cheet_away())
away_team.append(clean_cheet_team_away())
away_team.append(clean_cheet_away_team_overall())
away_team.print_list()
print("\n")
home_team.print_list()