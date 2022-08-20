from Riot_API import RiotAPI

def main():
    api = RiotAPI('') #('Put your own riot api key here')
    sum_name = input('Please enter a summoner name:')
    sumVal = api.get_summoner_by_name(sum_name)
    print (sumVal)     
    sumMatch = api.get_summoner_matches(sumVal['puuid'], 0, 5)
    print(sumMatch)
if __name__ == "__main__":
    main()  