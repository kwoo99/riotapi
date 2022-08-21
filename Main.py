from Riot_API import RiotAPI

def main():
    api = RiotAPI('RGAPI-3e8f7fa0-4e56-4943-9a5d-e183edb165e8') #('Put your own riot api key here')
    sum_name = input('Please enter summoner name:')
    sumVal = api.get_summoner_by_name(sum_name)
    print (f"Here is the profile of the summoner you requested:\n{sumVal}")
    sumMatch = api.get_summoner_matches(sumVal['puuid'], 0, 5)
    print(f"Here are the ids of the last 5 matches this summoner has participated in:\n{sumMatch}\n") 
if __name__ == "__main__":
    main()  