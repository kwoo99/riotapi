from riotwatcher import LolWatcher

class lol_Comp:
  
  def __init__(self, api_key, region, team):
    self.api_key = api_key
    self.region = region
    self.team = team
    self.team_List = []
    self.sum_Prof = LolWatcher(self.api_key, default_status_v4=True)

    # self.team_List = [self.team_List.append(sum_Prof.summoner.by_name(self.region, self.team[i])) for i in range(0,5)]
    
    # for i in range(0, 5):
    #   self.team_List.append(sum_Prof.summoner.by_name(self.region, self.team[i]))

  def create_Team(self):
    for i in range(len(self.team)):
      self.team_List.append(self.sum_Prof.summoner.by_name(self.region, self.team[i]))
    print(type(self.team_List[0]))
    print(self.team_List[0]['name'])

  def get_Team_Info(self):
    final_Info_List = []
    for i in range(0, len(self.team)):
      team_List_Info = []
      team_List_Info.append(self.team_List[i])
      final_Info_List.append(team_List_Info)
    return final_Info_List
                            
    return team_List_Info
  
  def team_Lvl_Compare(self):
    highest_Lvl = 0
    highest_Lvl_Name = ''
    for i in range(len(self.team)):
      if self.team_List[i]['summonerLevel'] > highest_Lvl:
        highest_Lvl = self.team_List[i]['summonerLevel']
        highest_Lvl_Name = self.team_List[i]['name']
    return highest_Lvl_Name

  def get_Match(self):
    final_List = []
    for i in range(len(self.team)):
      match_List = [] 
      match_List.append(self.sum_Prof.match.matchlist_by_puuid(self.region, self.team_List[i]['puuid'], None, 5))
      final_List.append(match_List)
    return final_List

  def team_Kills_Compare(self):
    target_Matches = []
    sum_Kills = []
    kills = 0
    kill_Leader = self.team[0]
    most_Kills = 0
    leader_Prof = {'kl_Name': '', 'kl_Kills': 0}
    
    for i in range(len(self.team)):
      target_Matches.append(self.sum_Prof.match.matchlist_by_puuid(self.region, self.team_List[i]['puuid'], None, 3))
    print(f"Target Matches:\n{target_Matches}")
    
    for i in range(len(target_Matches)):
      print(f"Processing {self.team[i]}'s kills:")
      
      for j in range(len(target_Matches[i])):
        print(f"{self.team[i]}'s kills for match {target_Matches[i][j]}:")
        match_Results = self.sum_Prof.match.by_id(self.region, target_Matches[i][j])
        converted_Results = match_Results['info']['participants']
        
        for x in range(len(converted_Results)):
          if converted_Results[x]['puuid'] == self.team_List[i]['puuid']:
            print(converted_Results[x]['kills'])
            kills = kills + converted_Results[x]['kills']
            
      sum_Kills.append(kills)
      kills = 0
      print(sum_Kills)
      
      if sum_Kills[i] > most_Kills:
        most_Kills = sum_Kills[i]
        kill_Leader = self.team[i]
        
    leader_Prof['kl_Name'] = kill_Leader
    leader_Prof['kl_Kills'] = most_Kills
    return leader_Prof