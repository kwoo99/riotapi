import requests
import RiotConsts as Consts

class RiotAPI(object):
    def __init__(self, api_key, region=Consts.REGIONS['north_america_1']):
        self.api_key = api_key
        self.region = region

    def requests(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            Consts.URL['base'].format(
            proxy=self.region,
            region=self.region,
            url=api_url
            ),
        params=args 
        )
        print(args)
        print(response.url)
        return response.json()

    def get_summoner_by_name(self, name):
        api_url = Consts.URL['summoner_by_name'].format(
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

    def get_summoner_matches(self, puuid, start, matchQuant):
        api_url = Consts.URL['summoner_matches_by_puuid'].format(
            version=Consts.API_VERSIONS['summoner_matches'],
            summoner_puuid=puuid,
            start_date=start,
            num_of_matches=matchQuant
        )
        return self.requests(api_url)