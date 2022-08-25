URL = {  # Predefined urls that are used to get the request from riots api by changing certain elements functions from
    # Riot_API 'base': 'https://{proxy}.api.riotgames.com/{url}',
    'summoner_by_name': 'https://{proxy}.api.riotgames.com/lol/summoner/v{version}/summoners/by-name/{names}',
    # 'tft_summoner_by_name': 'tft/summoner/v{version}/summoners/by-name/{names}',
    'summoner_matches_by_puuid': 'https://{proxy}.api.riotgames.com/lol/match/v{version}/matches/by-puuid/{summoner_puuid}/ids?start={start}&count={num_of_matches}',
    'match_by_match_ID': 'https://{proxy}.api.riotgames.com/lol/match/v{version}/matches/{matchID}'
}

API_VERSIONS = {
    # Stored version variables used as parameters from functions in Riot_API to be inserted in the request url
    'summoner': '4',  # for summoner_by_name
    # 'tft_summoner': '1',
    'summoner_matches': '5',  # for summoner_matches_by_puuid
    'match': '5'  # for match_by_match_ID
}

REGIONS = {  # Stored Region variables used as parameters from function in Riot_API to be inserted in teh request url
    'north_america_1': 'na1',  # for summoner_by_name
    'america': 'americas'  # for summoner_matches_by_puuid
}
