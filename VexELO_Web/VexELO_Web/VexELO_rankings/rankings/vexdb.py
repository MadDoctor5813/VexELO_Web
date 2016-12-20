import requests
import json
from VexELO_rankings.models import Match, Team

class JsonMatch:

    redTeam1 = ""
    redTeam2 = ""
    blueTeam1 = ""
    blueTeam2 = ""

    redScore = 0
    blueScore = 0

    def __init__(self, redTeam1, redTeam2, blueTeam1, blueTeam2, redScore, blueScore):
        self.redTeam1 = redTeam1
        self.redTeam2 = redTeam2
        self.blueTeam1 = blueTeam1
        self.blueTeam2 = blueTeam2
        self.redScore = redScore
        self.blueScore = blueScore

class VexDbApi:

    MATCHES_URL = r'https://api.vexdb.io/v1/get_matches'

    def get_all_matches(self):
        matches = list()
        #get the number of current starstruck matches
        nodata_response = requests.get(self.MATCHES_URL, {'season':'current', 'nodata':True}).json()
        num_matches = nodata_response['size']
        #get all the matches
        count = 0
        while count < num_matches:
            data_response = requests.get(self.MATCHES_URL, {'season':'current', 'limit_start':count}).json()
            for team_json in data_response['result']:
                #exclude VEX university matches
                if "VEXU" not in team_json['sku']: 
                    matches.append(self.parse_match_json(team_json))
            count += data_response['size']
        return matches
        
    def parse_match_json(self, json):
        redTeams = [json['red1'], json['red2'], json['red3']]
        blueTeams = [json['blue1'], json['blue2'], json['blue3']]
        redTeams = [x for x in redTeams if x != json['redsit']]
        blueTeams = [x for x in blueTeams if x != json['bluesit']]
        return JsonMatch(redTeams[0], redTeams[1], blueTeams[0], blueTeams[1], json['redscore'], json['bluescore'])
