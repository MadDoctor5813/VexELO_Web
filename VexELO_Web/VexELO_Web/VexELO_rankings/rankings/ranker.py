import math

K_FACTOR = 32


def predict_match(red_elo1, red_elo2, blue_elo1, blue_elo2):
    red_elo = calc_alliance_elo(red_elo1, red_elo2)
    blue_elo = calc_alliance_elo(blue_elo1, blue_elo2)
    #transform elos according to the elo formula
    red_elo = math.pow(10, red_elo / 400)
    blue_elo = math.pow(10, blue_elo / 400)
    #get expected results
    red_expected = red_elo / (red_elo + blue_elo)
    blue_expected = blue_elo / (red_elo + blue_elo)
    return red_expected, blue_expected
    
def rank_match(match, team_dict):
    red_expected, blue_expected = predict_match(match.redTeam1.elo, match.redTeam2.elo, match.blueTeam1.elo, match.blueTeam2.elo)
    red_actual = 0
    blue_actual = 0
    if match.redScore > match.blueScore:
        #red wins
        red_actual = 1
        blue_actual = 0
    elif match.redScore < match.blueScore:
        #blue wins
        red_actual = 0
        blue_actual = 1
    else:
        #we have a tie
        red_actual = 0.5
        blue_actual = 0.5
    margin_adjust = calc_margin_adjust(match.redScore, match.blueScore)
    red_change = margin_adjust * K_FACTOR * (red_actual - red_expected)
    blue_change = margin_adjust * K_FACTOR * (blue_actual - blue_expected)
    apply_elo(team_dict, match.redTeam1, match.redTeam2, red_change)
    apply_elo(team_dict, match.blueTeam1, match.blueTeam2, blue_change)

def calc_margin_adjust(red_score, blue_score):
    margin = math.fabs(red_score - blue_score)
    if margin == 0:
        return 1
    else:
        return math.log(margin, 10) + 1

def calc_alliance_elo(team_elo1, team_elo2):
    return (team_elo1 + team_elo2) / 2

def apply_elo(team_dict, team1, team2, change):
    contrib1 = team1.elo / (team1.elo + team2.elo)
    contrib2 = team2.elo / (team1.elo + team2.elo)
    team1.elo += (change * contrib1)
    team2.elo += (change * contrib2)