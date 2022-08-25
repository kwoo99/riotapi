from Riot_API import RiotAPI


def main():
    api = RiotAPI('')  # ('Put your own riot api key here')
    sum_name = input('Please enter summoner name:')
    sumVal = api.get_summoner_by_name(sum_name)
    print(f"Here is the profile of the summoner you requested:\n{sumVal}")
    sumMatch = api.get_summoner_matches(sumVal['puuid'], 0, 5)
    print(f"Here are the ids of the last 5 matches this summoner has participated in:\n{sumMatch}\n")
    matchP = api.get_match_details(sumMatch[0])
    print(matchP)


if __name__ == "__main__":
    main()
