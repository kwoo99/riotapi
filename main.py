from lolAPI import lol_Comp

region = 'na1'
sum_Team = ['']
api_key = ''

sum_Team = ['someonesleftnut', 'hideonbush', 'Doublelift', 'trashley12345', 'flyingsquirrelly']

# print("Please enter 5 summoner names to form a team:\n")

# for i in range(len(sum_Team)):
#   sum_Team[i] = input(f'Summoner {i+1}:')

player_Party_Profs = lol_Comp(api_key, region, sum_Team)
player_Party_Profs.create_Team()

for i in range(len(player_Party_Profs.team)):
  print(f"{sum_Team[i]}'s info:\n{player_Party_Profs.get_Team_Info()[i]}\n")
  
print(f"{player_Party_Profs.team_Lvl_Compare()} is the highest level.\n")

for i in range(len(player_Party_Profs.team)):
  print(f"{player_Party_Profs.team[i]}'s match id(s):\n{player_Party_Profs.get_Match()[i]}\n")

player_Kill_Comp = player_Party_Profs.team_Kills_Compare()

print(f"{player_Kill_Comp['kl_Name']} achieved the most kills: {player_Kill_Comp['kl_Kills']}")