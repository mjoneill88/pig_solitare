
import random


class Eight_Rolls_Pig:
    def __init__(self):
        self.score = 0
        self.roll_count =7
    def roll_again(self):
        if self.roll_count > 0:
            self.roll_count -= 1
            return True
        else:
            return False

class Seven_Rolls_Pig:
    def __init__(self):
        self.score = 0
        self.roll_count =6
    def roll_again(self):
        if self.roll_count > 0:
            self.roll_count -= 1
            return True
        else:
            return False

class Six_Rolls_Pig:
    def __init__(self):
        self.score = 0
        self.roll_count =5
    def roll_again(self):
        if self.roll_count > 0:
            self.roll_count -= 1
            return True
        else:
            return False

class Five_Rolls_Pig:
    def __init__(self):
        self.score = 0
        self.roll_count =4
    def roll_again(self):
        if self.roll_count > 0:
            self.roll_count -= 1
            return True
        else:
            return False

class Four_Rolls_Pig:
    def __init__(self):
        self.score = 0
        self.roll_count =3
    def roll_again(self):
        if self.roll_count > 0:
            self.roll_count -= 1
            return True
        else:
            return False

class Fifty_Percent_Pig:
    def __init__(self):
        self.score = 0
    def roll_again(self):
        random_number = random.randint(1,2)
        if random_number == 1:
            return True
        else:
            return False
            

class Seventy_Percent_Pig:
    def __init__(self):
        self.score = 0
    def roll_again(self):
        random_number = random.randint(1,10)
        if random_number <= 7:
            return True
        else:
            return False

class Eighty_Percent_Pig:
     def __init__(self):
         self.score = 0
     def roll_again(self):
         random_number = random.randint(1,10)
         if random_number <= 8:
             return True
         else:
             return False


class Ninety_Percent_Pig:
     def __init__(self):
         self.score = 0
     def roll_again(self):
         random_number = random.randint(1,10)
         if random_number <= 9:
             return True
         else:
             return False

class Messing_With_Stuff_Pig:
     def __init__(self):
         self.score = 0
     def roll_again(self):
         if self.score < 20:
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

def simulate_trials(trials):
    trial_results = []
    while trials > 0:
        pig_player = Eight_Rolls_Pig()
        play_game(pig_player)
        trial_results.append(pig_player.score)
        pig_player.score = 0
        trials -= 1
    return trial_results


def main():
    trial_results = simulate_trials(10000)
    #print(trial_results)
    print('Number of Trials:', len(trial_results))
    print(sum(trial_results)/len(trial_results))

main()
