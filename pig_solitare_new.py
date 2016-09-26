#Ideas:
#simulate different pigs with different
#probabilities of rolling again

import random

class Base_Pig:
    def __init__(self):
        self.score = 0

    def roll_again(self):
        random_number = random.randint(1,2)
        if random_number == 1:
            return True
        else:
            return False

class Five_Pig:
    def __init__(self):
        self.score = 0
        self.roll_count =4

    def roll_again(self):

        if self.roll_count > 0:
            self.roll_count -= 1
            return True
        else:
            return False





def roll_dice():
    dice_roll = random.randint(1,6)
    return dice_roll

def play_game(pig):
    turn_over = False
    dice_score = roll_dice()
    if dice_score == 1:
        turn_over = True
    else:
        pig.score += dice_score
        decide_to_roll_again = pig.roll_again()
        while not turn_over and decide_to_roll_again:
            dice_score = roll_dice()
            if dice_score == 1:
                turn_over = True
                pig.score = 0
            else:
                pig.score += dice_score
                decide_to_roll_again = pig.roll_again()

pig_player = Five_Pig()

play_game(pig_player)

print(pig_player.score)
