from Riot_API import RiotAPI
# Riot API
# Benjamin Fuller & Kyle Woo


def main():
  # Put your Riot API key here below (new key every 24 hours)
  apiKey = ""
  api = RiotAPI(apiKey)
  sum_name = input('Please enter summoner name:')
  sumVal = api.get_summoner_by_name(sum_name)
  print("Here is the profile of the summoner you requested:\n")
  print(
    f"Name:{sumVal['name']}\nSummoner Level:{sumVal['summonerLevel']}\nPuuid:{sumVal['puuid']}"
  )
  sumMatch = api.get_summoner_matches(sumVal['puuid'], 0, 5)
  print(
    f"Here are the ids of the last 5 matches this summoner has participated in:\n{sumMatch}\n"
  )

  matchP = api.get_match_details(sumMatch[0])
  print(matchP['participants'])


if __name__ == "__main__":
  main()
