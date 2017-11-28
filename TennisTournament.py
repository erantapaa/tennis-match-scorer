import csv
import pickle

all_players = []
all_tournaments = []


# ------------------------------ Initial Inputs ------------------------------
def save_players():
    with open("player_objects.txt") as fp:
        pickle.dump(all_players, fp)

def load_players():
    with open("player_objects,txt") as fp:
        all_players = pickle.load(fp)
        print(len(fp))

# Fills all_players
def read_players():
    # read male players into malePlayerList
    with open("MALE PLAYERS.csv", "r") as malePlayersFile:
        malePlayersFileReader = csv.reader(malePlayersFile)
        for row in malePlayersFileReader:
            if len(row) != 0:
                all_players.append(Player(str(*row),"male"))
    # read female players into malePlayerList
    with open("FEMALE PLAYERS.csv", "r") as femalePlayersFile:
        femalePlayersFileReader = csv.reader(femalePlayersFile)
        femalePlayerList = []
        for row in femalePlayersFileReader:
            if len(row) != 0:
                all_players.append(Player(str(*row), "female"))


# Fills all_tournaments
def read_tournaments():
    t_file = list(csv.reader(open("PRIZE MONEY.csv")))
    for i in range(len(t_file)):
        for j in range(len(t_file[i])):  # j is columns, i is rows
            if i > 0:
                current_input = t_file[i][j]
                if j == 0:  # first row is tournament names
                    if len(current_input) > 2:  # i > 0 skips first line (headers) len... skips empty
                        this_tournament = Tournament(current_input,[])
                        all_tournaments.append(this_tournament)
                if  j == 2:
                    this_tournament.add_prize(current_input)






def get_difficulty(t_name):
    print("finding difficulty " + t_name)
    if t_name == "TAC1":
        return 2.7
    if t_name == "TAE21":
        return 2.3
    if t_name == 'TAW11':
        return 3.1
    if t_name == "TBS2":
        return 3.25


# ---------------------------------- Classes ----------------------------------

class Player:
    def __init__(self,name,gender):
        # print("new player")
        self.name = name
        self.gender = gender
        self.points = 0
        self.difficulty = get_difficulty(name)

    def get_name(self):
        return self.name

    def add_points(self, p):
        self.points += p


class Tournament:
    '''
    new_game is used to advance and eliminate players
    '''
    def __init__(self, name, prizemoney):
        self.prizemoney = prizemoney
        # prizemoney first place index is 0
        self.name = name
        self.current_round_players = all_players
        self.next_round_players = []
        self.not_in_round = []
        self.current_round = 1
        self.finished = False
        self.difficulty = 1
        print(*self.prizemoney, sep='\n')
        print("New tournament: " + self.name)

    def new_game(self, p1, p2, s1, s2):
        if p1 not in self.not_in_round and p2 not in self.not_in_round:
            if s1 > s2:  # p1 wins
                self.next_round_players.append(p1)
                # TODO adds points for winning player
            if s2 > s1:  # p2 wins
                self.next_round_players.append(p2)
            self.not_in_round.append(p1)
            self.not_in_round.append(p2)
        else:
            print("ERR: A selected player is not in the round")

    def next_round(self):
        if len(self.next_round_players) is 1:  # Tournament is over
            print("End of tournament")
        else:
            self.current_round += 1
            self.current_round_players = self.next_round_players
            self.next_round_players = []

    def end_tourn(self):
        self.finished = True

    def add_prize(self, prize): # used to populate prizemoney
        self.prizemoney.append(prize)
        print(self.name + " prize money added: " + prize)

# ---------------------------------- Sorting ----------------------------------


# test this
def sort_by_points(p_list):
    string_list = []
    for i in range(len(p_list)):
        list.append(p_list[i].get_points + " " + p_list[i].get_name)
    return sorted(string_list)

# --------------------------------- Running ------------------------------------

read_players()
read_tournaments()
