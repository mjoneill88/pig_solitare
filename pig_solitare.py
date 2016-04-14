# Pig Solitare

import random

class Pig:
    def __init__(self):
        self.points = 0
    def change_points(self, number_points):
        self.points += number_points
    def choose_after_roll(self, turn_score):
        return 0

class RandomPig(Pig):
    def __init__(self):
        self.points = 0
    def change_points(self, number_points):
        self.points += number_points
    def choose_after_roll(self, turn_score):
        random_number=random.randint(0,1)




class SmartPig(Pig):
    pass

player_1 = Pig()

def roll_die():
    return random.randint(1,6)


def game_function(player):
    turn_score = 0
    choice=1
    turn_over=0
    for _ in range(7):
        while choice and not turn_over:
            dice_roll = roll_die()
            print("DICE ROLL", dice_roll)
            if dice_roll == 1:
                turn_score = 0
                turn_over = 1
            turn_score += dice_roll
            choice = player.choose_after_roll(turn_score)
        player.change_points(turn_score)


    # for _ in range(7):
    #     dice_roll = roll_die()
    #     if dice_roll == 1:
    #         turn_score = 0
    #         continue
    #     turn_score += dice_roll
    #     choice=player.choose_after_roll(turn_score)
    #     while choice:
    #         dice_roll = roll_die()




game_function(player_1)
print(player_1.points)
