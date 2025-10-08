from espn_api.hockey import League
from datetime import datetime
import time

year = datetime.now().year + 1
league_id = int(input("league ID: "))
my_team = input("Team Name: ")
league = League(league_id=league_id, year=year)
current_matchup = league.box_scores()

for box in current_matchup:
    if box.home_team.team_name == my_team:
        team = "Home"
        score = box
    elif box.away_team.team_name == my_team:
        team = "Away"
        score = box

if team == "Home":
    print(score.home_score)
    print(datetime.now())
if team == "Away":
    print(score.away_score)
    print(datetime.now())

while True:
    time.sleep(60)
    if current_matchup != league.box_scores():
        current_matchup = league.box_scores()
        for box in current_matchup:
            if box.home_team.team_name == my_team:
                team = "Home"
                score = box
            elif box.away_team.team_name == my_team:
                team = "Away"
                score = box
        if team == "Home":
            print(score.home_score)
            print(datetime.now())
        if team == "Away":
            print(score.away_score)
            print(datetime.now())




