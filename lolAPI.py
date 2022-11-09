# lolPAI.py
# This file holds all the basic class variables as well as functions to initialize various profiles for a party of summoners by performing api calls using the riotwatcher library

from riotwatcher import *                   
from statistics import *
import json

class lol_Team:
  
  def __init__(self, api_key, region, roster):
    self.prof_Name = f"{roster}"
    self.api_key = api_key
    self.region = region
    self.roster = roster
    
    # Used for storing player profile details
    self.profiles = []
    self.rank_Profiles = []
    self.match_Profiles = []

    # Used for match specifications
    self.match_Quant = 0
    self.queue_Type = None
    self.start_Time = None

    
    
    # Object used to fetch api requests
    self.watcher = LolWatcher(self.api_key, default_status_v4=True)
    
#CREATE TEAM----------------------------------------------------------------------------------------------------
  def create_Team(self): 
  # Creates a list of lolwatcher objects using the list of team names given by user.
    for i in range(len(self.roster)):
      self.profiles.append(self.watcher.summoner.by_name(self.region, self.roster[i]))
    for i in range (len(self.roster)):
      self.rank_Profiles.append(self.watcher.league.by_summoner(self.region, self.profiles[i]['id']))
  
#GET MATCH------------------------------------------------------------------------------------------------------
  def get_Matches(self, match_Quant):
  # Returns a list of the last x matches for each summoner in the team.
    # match_List = []
    print(self.roster)
    for i in range(len(self.roster)):
      self.match_Profiles.append(self.watcher.match.matchlist_by_puuid(self.region, self.profiles[i]['puuid'], None, match_Quant))
      
    # self.match_Profiles = match_List
    
#Get Match Data--------------------------------------------------------------------------------------------------
  def get_Match_Data(self, match):
  # Returns the details for the match list specified for each summoner on the team
    return self.watcher.match.by_id(self.region, match)
    
  # def set_Match_Quant(quant):
  #   self.match_Quant = quant
    
  # def set_Queue_Type(type):
  #   self.queue_Type = type
    
  # def set_Start_Time(time):
  #   self.start_Time = time