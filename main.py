from lolTeam import *
from lolAPI import *

region = 'na1'
sum_Team = []
api_key = ''

sum_Team = ['someonesleftnut', 'chiva11', 'flyingsquirrelly','trashley12345']

sum_Team2 = ['goawayannaokbye', 'chiva11', 'flyingsquirrelly','zaffreX']

player_Party = lol_Team(api_key, region, sum_Team)

player_Party.create_Team()

for i in range(len(sum_Team)):
  print(f"Summoner Name:{player_Party.profiles[i]['name']}\nSummoner Level:{player_Party.profiles[i]['summonerLevel']}\nID:{player_Party.profiles[i]['id']}\nAccount ID:{player_Party.profiles[i]['id']}\nPUUID:{player_Party.profiles[i]['puuid']}\nProfile Icon ID:{player_Party.profiles[i]['profileIconId']}\nRevison Date:{player_Party.profiles[i]['revisionDate']}\n")

print(player_Party.match_Profiles)

kill_Summary = team_Stat_Compare(player_Party, 'kills',5)

print(f"{kill_Summary['stat_Leader']} achieved the most kills in your party: {kill_Summary['most_Stat']}\n{kill_Summary['stat_Loser']} achieved the least kills in your party: {kill_Summary['least_Stat']}\nAverage kills in the party was {kill_Summary['stat_Average']}\n")

tank_Summary = team_Stat_Compare(player_Party, 'totalDamageTaken',5)

print(f"{tank_Summary['stat_Leader']} achieved the most damage tanked in your party: {tank_Summary['most_Stat']}\n{tank_Summary['stat_Loser']} achieved the least damage tanked in your party: {tank_Summary['least_Stat']}\nAverage damage tanked in the party was {kill_Summary['stat_Average']}\n")

rank_Summary = team_Rank_Compare(player_Party)

print(f"Highest ranking member in the party is {rank_Summary['rank_Leader']}: {rank_Summary['best_Rank']}\nLowest ranking member in the party is {rank_Summary['rank_Loser']}: {rank_Summary['least_Rank']}\nAverage rank in the party is {rank_Summary['average_Rank']} ")

save_Team_Prof(player_Party)