from riotwatcher import *                   
from statistics import *

class lol_Comp:
  
  def __init__(self, api_key, region, team):
    self.api_key = api_key
    self.region = region
    self.team = team
    self.team_List = []
    self.watcher = LolWatcher(self.api_key, default_status_v4=True)

    self.lol_Ranks = {
      '': 0,
      'IRONI': 1, 
      'IRONII': 2,
      'IRONIII': 3,
      'IRONIV': 4,
      'BRONZEI': 5,
      'BRONZEII': 6,
      'BRONZEIII': 7,
      'BRONZEIV': 8,
      'SILVERI': 9,
      'SILVERII': 10,
      'SILVERIII': 11,
      'SILVERIV': 12,
      'GOLDI': 13,
      'GOLDII': 14,
      'GOLDIII': 15,
      'GOLDIV': 16,
      'PLATINUMI': 17,
      'PLATINUMII': 18,
      'PLATINUMIII': 19,
      'PLATINUMIV': 20,
      'DIAMONDI': 21,
      'DIAMONDII': 22,
      'DIAMONDIII': 23,
      'DIAMONDIV': 24,
      'MASTERI': 25,
      'MASTERII': 26,
      'MASTERIII': 27,
      'MASTERIV': 28,
      'GRANDMASTERI': 29,
      'GRANDMASTERII': 30,
      'GRANDMASTERIII': 31,
      'GRANDMASTERIV': 32,
      'CHALLENGERI': 33, 
      0: 'UNRANKED',
      1: 'IRON I',
      2: 'IRON II',
      3: 'IRON III',
      4: 'IRON IV',
      5: 'BRONZE I',
      6: 'BRONZE II',
      7: 'BRONZE III',
      8: 'BRONZE IV',
      9: 'SILVER I',
      10: 'SILVER II',
      11: 'SILVER III',
      12: 'SILVER IV',
      13: 'GOLD I',
      14: 'GOLD II',
      15: 'GOLD III',
      16: 'GOLD IV',
      17: 'PLATINUM I',
      18: 'PLATINUM II',
      19: 'PLATINUM III',
      20: 'PLATINUM IV',
      21: 'DIAMOND I',
      22: 'DIAMOND II',
      23: 'DIAMOND III',
      24: 'DIAMOND IV',
      25: 'MASTER I',
      26: 'MASTER II',
      27: 'MASTER III',
      28: 'MASTER IV',
      29: 'GRANDMASTER I',
      30: 'GRANDMASTER II',
      31: 'GRANDMASTER III',
      32: 'GRANDMASTER IV',
      33: 'CHALLENGER' 
    }

  def create_Team(self): 
  # Creates a list of lolwatcher objects using the list of team names given by user.
    for i in range(len(self.team)):
      self.team_List.append(self.watcher.summoner.by_name(self.region, self.team[i]))
    
  def get_Team_Info(self):
  # Used to format and return summoner's profile data from created team.
    formatted_Prof_Data_List = []
    
    for i in range(len(self.team)):
      formatted_Prof_Data = f"ID:{self.team_List[i]['id']}\nAccount ID:{self.team_List[i]['accountId']}\nPUUID:{self.team_List[i]['puuid']}\nProfileIconID:{self.team_List[i]['profileIconId']}\nRevision Data:{self.team_List[i]['revisionDate']}\nSummoner Level:{self.team_List[i]['summonerLevel']}"
      formatted_Prof_Data_List.append(formatted_Prof_Data)
    return formatted_Prof_Data_List

  def get_Match(self, match_Quant):
  # Returns a list of the last x matches for each summoner in the team.
    final_List = []
    
    for i in range(len(self.team)):
      match_List = [] 
      match_List.append(self.watcher.match.matchlist_by_puuid(self.region, self.team_List[i]['puuid'], None, match_Quant))
      final_List.append(match_List)
    return final_List

  def team_Rank_Compare(self):
  # Returns the highest and lowest ranking summoner as well as average rank of all summoners in the party
    summ_Ranks = []
    rank_Summary = {
      'best_Rank': '', 
      'least_Rank': '', 
      'rank_Leader': self.team[0], 
      'rank_Loser': self.team[0],
      'average_Rank': '',
      'unranked_Members': []
    }
    best_Rank_Val = 0
    least_Rank_Val = 34
    
    no_Rank_Deduct = 0 # not sure if this does anything
    
    for i in range(len(self.team) - no_Rank_Deduct): # Traverses through the team to get each ranked profile
      rank_Prof = self.watcher.league.by_summoner(self.region, self.team_List[i]['id'])
      
      if rank_Prof != []: # Checks if the summoner has a ranked profile
        summ_Rank = rank_Prof[0]['tier'] + rank_Prof[0]['rank']
        summ_Ranks.append(self.lol_Ranks[summ_Rank])
        
        print(f"{self.team[i]}: {rank_Prof[0]['tier']} {rank_Prof[0]['rank']}\n")
        
        if self.lol_Ranks[summ_Rank] > best_Rank_Val: # Checks if the current summoner has the highest rank and sets it if they do
          best_Rank_Val = self.lol_Ranks[summ_Rank] 
          rank_Summary['rank_Leader'] = self.team[i]
          rank_Summary['best_Rank'] = self.lol_Ranks[self.lol_Ranks[summ_Rank]]
          
        if self.lol_Ranks[summ_Rank] < least_Rank_Val: # Checks if the current summoner has the lowest rank and sets it if they do
          least_Rank_Val = self.lol_Ranks[summ_Rank]
          rank_Summary['rank_Loser'] = self.team[i]
          rank_Summary['least_Rank'] = self.lol_Ranks[self.lol_Ranks[summ_Rank]]
      else:
        rank_Summary['unranked_Members'].append(self.team[i])
        
    if len(summ_Ranks) < 1: # If there were no ranked summoners found
      no_Rank_Deduct += 1
      return None
      
    rank_Summary['average_Rank'] = self.lol_Ranks[int(round(mean(summ_Ranks)))]
    return rank_Summary
    
  def team_Kills_Compare(self, match_Quant):
  # Returns summoner in the team with the highest number of kills from the last x matches.
    target_Matches = []
    sum_Kills = []
    kills = 0
    kill_Summary = {'kill_Leader': self.team[0], 'most_Kills': 0, 'kill_Loser': self.team[0], 'least_Kills': 99999, 'av_Kills': 0}
    
    for i in range(len(self.team)): 
    # Populates target matches with list of x matches for each summoner
      target_Matches.append(self.watcher.match.matchlist_by_puuid(self.region, self.team_List[i]['puuid'], None, match_Quant))
    print(f"Target Matches:\n{target_Matches}")
    
    for i in range(len(target_Matches)):
    # Traverses the target matches for each summoner
      print(f"Processing {self.team[i]}'s kills:")
      
      for j in range(len(target_Matches[i])):
      # Creates an api call to fetch details for the ith match 
        print(f"{self.team[i]}'s kills for match {target_Matches[i][j]}:")
        match_Results = self.watcher.match.by_id(self.region, target_Matches[i][j])
        converted_Results = match_Results['info']['participants']
        
        for x in range(len(converted_Results)):
        # Traverses participants in the match data to find a matching puuid from team list
          if converted_Results[x]['puuid'] == self.team_List[i]['puuid']:
          # If puuid is recognized, adds kills to summoner's total kills
            print(converted_Results[x]['kills'])
            kills = kills + converted_Results[x]['kills']
            
      sum_Kills.append(kills) # Appends each players total kills to a list and resets kill count for next player
      kills = 0
      print(sum_Kills)
      
      if sum_Kills[i] > kill_Summary['most_Kills']: # Determines which player has the most total kills
        kill_Summary['most_Kills'] = sum_Kills[i]
        kill_Summary['kill_Leader'] = self.team[i]
        
      if sum_Kills[i] < kill_Summary['least_Kills']: # Determines which player has the least kills
        kill_Summary['least_Kills'] = sum_Kills[i]
        kill_Summary['kill_Loser'] = self.team[i]
        
    kill_Summary['av_Kills'] = int(sum(sum_Kills) / len(self.team))
    
    return kill_Summary # Returns a dict containing the player with highest kill's name and kill total

  def team_Compare_