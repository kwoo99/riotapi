from Riot_API import RiotAPI

def main():
    api = RiotAPI('RGAPI-3e8f7fa0-4e56-4943-9a5d-e183edb165e8')
    sum_name = input('Please enter a summoner name:')
    sumVal = api.get_summoner_by_name(sum_name)
    print (sumVal)     
    sumMatch = api.get_summoner_matches(sumVal['puuid'], 0, 5)
    print(sumMatch)
if __name__ == "__main__":
    main()  