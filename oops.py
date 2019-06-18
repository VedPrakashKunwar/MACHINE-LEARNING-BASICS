############################ import data #################################
import pandas as pd
play = pd.read_table("D:/Study/Dataquest/Data sets/nba_players_2013.csv", sep=',')
# we want only first four column only 
nba = play.iloc[:, 0:4].copy().values.tolist()

# Initialize a player using the first row of our data set
first_player = Player(nba.loc[0])

# creating the team class
import math

class Player():
    # The special __init__ function runs whenever a class is instantiated
    # The init function can take arguments, but self is always the first one
    # Self is just a reference to the instance of the class
    # It's automatically passed in when you instantiate an instance of the class
    def __init__(self, data_row):
        self.player_name = data_row[0]
        self.position = data_row[1]
        self.age = int(data_row[2])
        self.team = data_row[3]

class Team():
    def __init__(self, team_name):
        self.team_name = team_name
        self.roster = []
        for row in nba:
            if row[3] == self.team_name:
                self.roster.append(Player(row))
    
    def num_players(self):
        count = 0
        for player in self.roster:
            count += 1
        return count
    
    def average_age(self):
        return math.fsum([player.age for player in self.roster]) / self.num_players()
    
    @classmethod
    def older_team(self, team1, team2):
        if team1.average_age() > team2.average_age():
            return team1
        else:
            return team2

old_team = Team.older_team(Team("New York Knicks"), Team("Miami Heat"))
spurs = Team("San Antonio Spurs")
spurs_num_players = spurs.num_players()
spurs_avg_age = spurs.average_age()