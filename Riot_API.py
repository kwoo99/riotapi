import requests
import RiotConsts as Consts

class RiotAPI(object):
    def __init__(self, api_key): #Contructor that sets the users api_key to be used for the requests, can be found in Main.py
        self.api_key = api_key
        # self.region = region

    def requests(self, api_url, params={}): #function that takes url parameters set by the get_functions and makes a request 
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(api_url, params=args)
        print(f"The request url you are using is:\n{response.url}\n")
        return response.json()

    def get_summoner_by_name(self, name): #Gets the summoners data using the summoner name
        api_url = Consts.URL['summoner_by_name'].format(
            proxy=Consts.REGIONS['north_america_1'],
            version=Consts.API_VERSIONS['summoner'],
            names=name
        )
        return self.requests(api_url)

    #Does essentially the same thing as get_summoner_name()
    # def get_tft_summoner_name(self, name):
    #     api_url = Consts.URL['tft_summoner_by_name'].format(
    #      version=Consts.API_VERSIONS['tft_summoner'],
    #      names=name   
    #     )
    #     return self.requests(api_url)

    def get_summoner_matches(self, puuid, startNum, matchQuant): #Gets the summoners match history with their puuid, can specify how many matches to get
        api_url = Consts.URL['summoner_matches_by_puuid'].format(
            proxy=Consts.REGIONS['america'],
            version=Consts.API_VERSIONS['summoner_matches'],
            summoner_puuid=puuid,
            start=startNum,
            num_of_matches=matchQuant
        )
        return self.requests(api_url)

    def get_match_details(self, matchID): #Gets match details with a given match id
        api_url = Consts.URL['match_by_match_ID'].format(
            proxy=Consts.REGIONS['america'],
            version=Consts.API_VERSIONS['match'],
            matchID=matchID
        )
        return self.requests(api_url)
