from lolAPI import lol_Comp

region = 'na1'
sum_Team = []
api_key = ''

team_Size = int(input("Please specify a team size:"))

print(f"Please enter {team_Size} summoner names to form the team:\n")

for i in range(0, team_Size):
  sum_Team.append(input(f'Summoner {i+1}:'))
print('')

player_Party_Profs = lol_Comp(api_key, region, sum_Team)
player_Party_Profs.create_Team()

for i in range(len(player_Party_Profs.team)):
  print(f"{sum_Team[i]}'s Profile:\n{player_Party_Profs.get_Team_Info()[i]}\n")


for i in range(len(player_Party_Profs.team)):
  print(f"{player_Party_Profs.team[i]}'s match id(s):\n{player_Party_Profs.get_Match(8)[i]}\n")

player_Kill_Comp = player_Party_Profs.team_Kills_Compare(4)

print(f"{player_Kill_Comp['kill_Leader']} achieved the most kills: {player_Kill_Comp['most_Kills']}\n{player_Kill_Comp['kill_Loser']} achieved the least kills:{player_Kill_Comp['least_Kills']}\nAverage kills for all games is {player_Kill_Comp['av_Kills']}")

player_Rank_Comp = player_Party_Profs.team_Rank_Compare()

if player_Rank_Comp == None:
  print("Your entire team is unranked and therefore does not have a rank average.")
else:
  print(f"Average player rank in party: {player_Party_Profs.team_Rank_Compare()}\n")