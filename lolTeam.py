# lolTeam.py
# This file holds functions used to analyze team statistics and give specific results and acknowledgements based off of them. 

from riotwatcher import *
from statistics import *
from lolAPI import *
import json

lol_Titles = [
  'Tank', # Has highest damage taken to least deaths ratio
  'Inter', # Closest stats to "inter level" stats, must meet a minimun threshold to qualify
  'Baller', # Most gold collected
  'Headhunter', # Most kills regardless of damage dealt
  'Bounty Hunter', # Has highest bounty gold collected
  'Swiper', # Biggest kill stealer
  'Wizard', # Most magic damage dealt to champions
  'Sniper', # Most skill shots landed on champions
  'Scrapper' # Most physical damage dealt to champions
]

lol_Ranks = {
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

def team_Rank_Compare(team):
# Returns the highest and lowest ranking summoner as well as average rank of all summoners in the party
  summ_Ranks = []
  rank_Summary = {
    'best_Rank': '', 
    'least_Rank': '', 
    'rank_Leader': '', 
    'rank_Loser': '',
    'average_Rank': '',
    'unranked_Members': []
  }
  best_Rank_Val = 0
  least_Rank_Val = 34
  
  no_Rank_Deduct = 0 # not sure if this does anything
  
  for i in range(len(team.roster) - no_Rank_Deduct): # Traverses through the team to get each ranked profile
    rank_Prof = team.rank_Profiles[i]
    
    if rank_Prof != []: # Checks if the summoner has a ranked profile
      summ_Rank = rank_Prof[0]['tier'] + rank_Prof[0]['rank']
      summ_Ranks.append(lol_Ranks[summ_Rank])
      
      print(f"{team.roster[i]}: {rank_Prof[0]['tier']} {rank_Prof[0]['rank']}\n")
      
      if lol_Ranks[summ_Rank] > best_Rank_Val: # Checks if the current summoner has the highest rank and sets it if they do
        best_Rank_Val = lol_Ranks[summ_Rank] 
        rank_Summary['rank_Leader'] = team.roster[i]
        rank_Summary['best_Rank'] = lol_Ranks[lol_Ranks[summ_Rank]]
        
      if lol_Ranks[summ_Rank] < least_Rank_Val: # Checks if the current summoner has the lowest rank and sets it if they do
        least_Rank_Val = lol_Ranks[summ_Rank]
        rank_Summary['rank_Loser'] = team.roster[i]
        rank_Summary['least_Rank'] = lol_Ranks[lol_Ranks[summ_Rank]]
    else:
      rank_Summary['unranked_Members'].append(team.roster[i])
      
  if len(summ_Ranks) < 1: # If there were no ranked summoners found
    no_Rank_Deduct += 1
    return None
    
  rank_Summary['average_Rank'] = lol_Ranks[int(round(mean(summ_Ranks)))]
  return rank_Summary # Returns a dict containing rank information
  
#Stat COMPARE****************************************************************************
def team_Stat_Compare(team, target_Stat, match_Quant):
  sum_Stat = []
  stat = 0
  stat_Summary = {
    'stat_Leader': team.roster[0],
    'most_Stat': 0, 
    'stat_Loser': team.roster[0],
    'least_Stat': 999999,
    'stat_Average': None
  }
  
  team.get_Matches(match_Quant)
  # Populates target matches with list of x matches for each summoner
  print(f"Target Matches:\n{team.match_Profiles}")
  
  for i in range(len(team.match_Profiles)):
  # Traverses the target matches for each summoner
    print(f"Processing {target_Stat} for {team.roster[i]}:")
    for j in range(len(team.match_Profiles[i])):
    # Creates an api call to fetch details for the ith match 
      print(f"{team.roster[i]}'s {target_Stat} for match {team.match_Profiles[i][j]}:")
      match_Results = team.get_Match_Data(team.match_Profiles[i][j])
      converted_Results = match_Results['info']['participants']

      for x in range(len(converted_Results)):
      # Traverses participants in the match data to find a matching puuid from team list
        if converted_Results[x]['puuid'] == team.profiles[i]['puuid']:
        # If puuid is recognized, adds specified stat to summoner's total of the specified stat
          print(converted_Results[x][target_Stat])
          stat = stat + converted_Results[x][target_Stat]
          
    sum_Stat.append(stat) # Appends each players total of the specified stat to a list and resets specified stat count for next player
    stat = 0
    print(sum_Stat)
    
    if sum_Stat[i] > stat_Summary['most_Stat']: # Determines which player has the most the specified stat
      stat_Summary['most_Stat'] = sum_Stat[i]
      stat_Summary['stat_Leader'] = team.roster[i]
      
    if sum_Stat[i] < stat_Summary['least_Stat']: # Determines which player has the least of the specified stat
      stat_Summary['least_Stat'] = sum_Stat[i]
      stat_Summary['stat_Loser'] = team.roster[i]
      
  stat_Summary['stat_Average'] = int(sum(sum_Stat) / len(team.roster))

  return stat_Summary # Returns a dict containing stats

def save_Team_Prof(team_Profile, prof_Name):
  profiles_List = []
  profiles = {}
  isDuplicate = True
  isEmpty = False
  for i in range(len(team_Profile.roster)):
    prof = {
      'name': team_Profile.roster[i],
      'level': team_Profile.profiles[i]['summonerLevel'],
      'id': team_Profile.profiles[i]['id'],
      'puuid': team_Profile.profiles[i]['puuid'],
      'acctid': team_Profile.profiles[i]['accountId'],
      'achievements': []
    }
    profiles['prof_List_Name'] = prof_Name
    profiles[f'Prof {i + 1}'] = prof
  
  with open("profiles.json") as jsonFile:
    try:
      data = json.load(jsonFile)
      for i in range(len(data)):
        profiles_List.append(data[i])
      print("Debug 1")
    except:
      isEmpty = True
      print("Debug 2")
      
  if isEmpty:
    print("Debug 3")
    profiles_List.append(profiles)
    save_Profile = json.dumps(profiles_List, indent=4)
    with open("profiles.json", "w") as outfile:
      outfile.write(save_Profile)
  else:
    tempProf = {}
    for i in range(len(profiles) - 1):
      tempProf[f'Prof {i + 1}'] = profiles[f'Prof {i + 1}']
    for i in range(len(data)):
      tempDataProf = {}
    # print("Debug 4")
    # print(f"There exist {len(data)} profile list(s)")
    # for i in range(len(data)):
    #   if isDuplicate == False:
    #     break
    #   print(f"Length of data:{len(data)}")
    #   print(f"Current iteration of i:{i}")
    #   for j in range(len(data[i]) - 1):
    #     if isDuplicate == False:
    #       break
    #     print(f"Length of data[i]: {len(data[i])}")
    #     print(f"Current iteration of j:{j}")
    #     for x in range(len(profiles_List)):
    #       if isDuplicate == False:
    #         break
    #       print(data[i][f'Prof {j + 1}']['puuid'])
    #       print("-------------------------------------------")
    #       print(profiles[f'Prof {x + 1}']['puuid'])
    #       if data[i][f'Prof {j+1}']['puuid'] == profiles[f'Prof {x + 1}']['puuid']:
    #         print("Debug 5")
    #         isDuplicate = True
    #       else:
    #         print("Debug 6")
    #         print(f"{profiles_List[i][f'Prof {x + 1}']['name']} is different.\n")
    #         isDuplicate = False
    #         break
          
    print(f"{profiles['prof_List_Name']} is a duplicate profile is {isDuplicate}")
    
    if isDuplicate == False:
      print("Debug 7")
      profiles_List.append(profiles)
      save_Profile = json.dumps(profiles_List, indent=4)
      with open("profiles.json", "w") as outfile:
        outfile.write(save_Profile)
          
   
    

