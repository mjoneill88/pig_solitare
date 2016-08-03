# Pig Solitare

import random

class Pig:
    def __init__(self):
        self.turn_points = 0
        self.total_points = 0
        self.keep_rolling = True

    def choose_after_roll(self, turn_points):
        self.keep_rolling = False
        return self.keep_rolling

class RandomPig(Pig):
    def choose_after_roll(self, turn_points):
        random_number=random.randint(0,1)
        if random_number == 1:
            self.keep_rolling = True
            return self.keep_rolling
        else:
            self.keep_rolling = False
            return self.keep_rolling

class SmartPig(Pig):
    def choose_after_roll(self, turn_points):
        pass






player_1 = RandomPig()

def roll_die():
    return random.randint(1,6)




def game_function(player):
    for _ in range(7):
        player.turn_points = 0
        player.keep_rolling = True
        while player.keep_rolling:
            dice_roll = roll_die()
            if dice_roll == 1:
                player.turn_points = 0
                player.keep_rolling = False
            else:
                player.turn_points += dice_roll
                player.keep_rolling = player.choose_after_roll(player.turn_points)
            player.total_points += player.turn_points


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
print(player_1.__dict__)
