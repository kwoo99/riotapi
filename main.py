from lolAPI import lol_Comp

region = 'na1'
sum_Team = []
api_key = 'RGAPI-5cc939e3-30d1-49ee-b2e7-6456412a25f1'

# sum_Team = ['someonesleftnut', 'hideonbush', 'Doublelift', 'trashley12345', 'flyingsquirrelly']

team_Size = int(input("How many summoners will we be comparing?\n"))
print(f"Please enter {team_Size} summoner names to form a team:\n")

for i in range(team_Size):
  sum_Team.append(input(f'Summoner {i+1}:'))

player_Party_Profs = lol_Comp(api_key, region, sum_Team)
player_Party_Profs.create_Team()

for i in range(len(player_Party_Profs.team)):
  print(f"{sum_Team[i]}'s info:\n{player_Party_Profs.get_Team_Info()[i]}\n")
  
print(f"{player_Party_Profs.team_Lvl_Compare()} is the highest level.\n")

for i in range(len(player_Party_Profs.team)):
  print(f"{player_Party_Profs.team[i]}'s match id(s):\n{player_Party_Profs.get_Match()[i]}\n")

player_Kill_Comp = player_Party_Profs.team_Kills_Compare()

print(f"{player_Kill_Comp['kl_Name']} achieved the most kills: {player_Kill_Comp['kl_Kills']}")