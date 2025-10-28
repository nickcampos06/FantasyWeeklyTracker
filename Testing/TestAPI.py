from espn_api.hockey import League
from datetime import datetime
import time

# ---INITIALIZE--- #
# Get League info from user
year = datetime.now().year + 1
league_id = int(input("league ID: "))
my_team = input("Team Name: ")
# Generate League
league = League(league_id=league_id, year=year)
# Keep Track of the current week we are playing
current_week = league.current_week
# Find the full list of box scores in the league
current_matchup = league.box_scores()
# Find out which matchup belongs to the user
for box in current_matchup:
    if box.home_team.team_name == my_team:
        team = "Home"
        score = box
    elif box.away_team.team_name == my_team:
        team = "Away"
        score = box
# Print the score for the user
if team == "Home":
    print(score.home_score)
    print(datetime.now())
if team == "Away":
    print(score.away_score)
    print(datetime.now())

# ---LOOP--- #
# Every 60 seconds we check to see if the current matchup has changed (at the end of the week), and update the score
while True:
    time.sleep(60)
    # If a change is detected, we update the full list of matchups and find which one is the user's once again
    if current_week != league.current_week:
        current_matchup = league.box_scores()
        current_week = league.current_week
        for box in current_matchup:
            if box.home_team.team_name == my_team:
                team = "Home"
                score = box
            elif box.away_team.team_name == my_team:
                team = "Away"
                score = box
    # We print the current score
    if team == "Home":
        print(score.home_score)
        print(datetime.now())
    if team == "Away":
        print(score.away_score)
        print(datetime.now())

# For debugging purposes, I also print the date, so we can see when the week resets precisely
# and ensure the code accounts for it.


