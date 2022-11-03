from lolTeam import *
from lolAPI import *

region = 'na1'
sum_Team = []
api_key = ''

sum_Team = ['someonesleftnut', 'chiva11', 'flyingsquirrelly','trashley12345']

player_Party = lol_Team(api_key, region, sum_Team)

player_Party.create_Team()

for i in range(len(sum_Team)):
  print(f"Summoner Name:{player_Party.profiles[i]['name']}\nSummoner Level:{player_Party.profiles[i]['summonerLevel']}\nID:{player_Party.profiles[i]['id']}\nAccount ID:{player_Party.profiles[i]['id']}\nPUUID:{player_Party.profiles[i]['puuid']}\nProfile Icon ID:{player_Party.profiles[i]['profileIconId']}\nRevison Date:{player_Party.profiles[i]['revisionDate']}\n")

print(player_Party.match_Profiles)

kill_Summary = team_Kills_Compare(player_Party, 8)

print(f"{kill_Summary['kill_Leader']} achieved the most kills in your party: {kill_Summary['most_Kills']}\n{kill_Summary['kill_Loser']} achieved the least kills in your party: {kill_Summary['least_Kills']}\nAverage kills in the party was {kill_Summary['av_Kills']}\n")

rank_Summary = team_Rank_Compare(player_Party)

print(f"Highest ranking member in the party is {rank_Summary['rank_Leader']}: {rank_Summary['best_Rank']}\nLowest ranking member in the party is {rank_Summary['rank_Loser']}: {rank_Summary['least_Rank']}\nAverage rank in the party is {rank_Summary['average_Rank']} ")


