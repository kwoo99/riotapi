URL = {
    #'base': 'https://{proxy}.api.riotgames.com/{url}',
    'summoner_by_name': 'https://{proxy}.api.riotgames.com/lol/summoner/v{version}/summoners/by-name/{names}',
    #'tft_summoner_by_name': 'tft/summoner/v{version}/summoners/by-name/{names}',
    'summoner_matches_by_puuid': 'https://{proxy}.api.riotgames.com/lol/match/v{version}/matches/by-puuid/{summoner_puuid}/ids?start={start}&count={num_of_matches}',
    'match_by_match_ID': 'https://{proxy}.api.riotgames.com/lol/match/v{version}/matches/{matchID}'
}

API_VERSIONS = {
    'summoner': '4',          #for summoner_by_name
    #'tft_summoner': '1',
    'summoner_matches': '5',  #for summoner_matches_by_puuid
    'match': '5'              #for match_by_match_ID  
}

REGIONS = {
    'north_america_1': 'na1', #for summoner_by_name
    'america': 'americas'     #for summoner_matches_by_puuid
}