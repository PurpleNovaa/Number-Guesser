### Imports ###

import random
import time
from time import sleep
import csv
import subprocess

### Variables ###

gd = { # Game Difficulties
    # FORMAT - NAME: GUESSES, MAX NUMBER, TIME
    'quick': [3, 10, 120],
    'easy': [15, 60, 300],
    'normal': [10, 100, 180],
    'hard': [8, 125, 120],
    'extreme': [5, 150, 60]
}

gm = { # Gamemodes, to add a new gamemode you must edit the code yourself.
    'timed',
    'normal'
}

### Welcome ###

##   # #   # ##   ## #####  ##### #####   ###### #   # ##### ##### ##### ##### #####
# #  # #   # # # # # #    # #     #   #   #      #   # #     #     #     #     #   #
#  # # #   # #  #  # #####  ##### #####   #   ## #   # ##### ##### ##### ##### #####
#   ## #   # #     # #    # #     #  #    #    # #   # #         #     # #     #  #
#    # ##### #     # #####  ##### #   #   ###### ##### ##### ##### ##### ##### #   #

print("##   # #   # ##   ## #####  ##### #####   ###### #   # ##### ##### ##### ##### #####\n# #  # #   # # # # # #    # #     #   #   #      #   # #     #     #     #     #   #\n#  # # #   # #  #  # #####  ##### #####   #   ## #   # ##### ##### ##### ##### #####\n#   ## #   # #     # #    # #     #  #    #    # #   # #         #     # #     #  #\n#    # ##### #     # #####  ##### #   #   ###### ##### ##### ##### ##### ##### #   #")
# Prints the ASCII art above

### Last Record ###

lst_rcd = 'ng5best.csv' # Last Record

print("Last Record: \n"+open(lst_rcd).read())

open(lst_rcd).close()

### Functions ###

def start_timer(time_left):
    for x in range(time_left, 0, -1):
        time_left = x - 1
        print(time_left)
        sleep(1)
        return time_left

def timed_gamemode(mode, max_num, guesses, time_left, answer, start_time):
        if guesses != 1:
            print("Guess a number from 1 to "+str(max_num)+", you have "+str(guesses)+" guesses and "+str(time_left)+" seconds left. Type 'quit' to end the game")
        else:
            print("Guess a number from 1 to "+str(max_num)+", you have 1 guess and "+str(time_left)+" seconds left. Type 'quit' to end the game")
        guess = input("   ")
        # Checks if the guess is a number or string
        if guess.lower() == "quit":
            is_running = False
            quit()
        try:
            guess = int(guess)
            if guess < 1 or guess > max_num:
                print("Outside of boundaries.")

            elif guess != answer:
                guesses = guesses - 1
                if guess < answer:
                    print("Higher, time remaining: "+str(time_left))
                elif guess > answer:
                    print("Lower, time remaining: "+str(time_left))

            elif guess == answer:
                end_time = time.time()
                time_lapsed = end_time - start_time
                time_lapsed = str(round(time_lapsed, 2))
                print("Correct! The answer was "+str(answer)+", you won with "+time_left+" second left, your time was "+time_lapsed+"s! Enter your username to save your score.")
                username = input("")
                with open(lst_rcd, 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile, dialect='unix')
                    msg = [username, time_lapsed, mode.upper()]
                    writer.writerow(msg)

            if guesses == 0:
                print("Gameover! You have ran out of guesses, the correct answer was "+str(answer)+".")
            if time_left == 0:
                print("Gameover! You have ran out of time, the correct answer was "+str(answer)+".")
        except:
            print("Please enter 'quit' or a number.")

def begin_ng(mode, difficulty):
    # Variables
    diff_split = str(gd[difficulty]).replace("[", "").replace("]", "").split(",") # Removes the [] from the difficulty table and splits it up into 3 parts.
    guesses = int(diff_split[0]) # Tables start with 0
    max_num = int(diff_split[1])
    time_left = int(diff_split[2])
    answer = random.randrange(1, max_num)
    start_time = time.time()
    
    # Start Game

    if mode == 'normal':
        is_running = True
        while is_running == True:
            sleep(0.25)
            if guesses != 1:
                print("Guess a number from 1 to "+str(max_num)+", you have "+str(guesses)+" guesses. Type 'quit' to end the game")
            else:
                print("Guess a number from 1 to "+str(max_num)+", you have 1 guess. Type 'quit' to end the game")
            guess = input("   ")
            # Checks if the guess is a number or string
            if guess.lower() == "quit":
                is_running = False
                quit()
            try:
                guess = int(guess)
                if guess < 1 or guess > max_num:
                    print("Outside of boundaries.")

                elif guess != answer:
                    guesses = guesses - 1
                    if guess < answer:
                        print("Higher")
                    elif guess > answer:
                        print("Lower")

                elif guess == answer:
                    end_time = time.time()
                    time_lapsed = end_time - start_time
                    time_lapsed = str(round(time_lapsed, 2))
                    print("Correct! The answer was "+str(answer)+", your time was "+time_lapsed+"s! Enter your username to save your score.")
                    username = input("")
                    with open(lst_rcd, 'w', newline='') as csvfile:
                        writer = csv.writer(csvfile, dialect='unix')
                        msg = [username, time_lapsed, mode.upper()]
                        writer.writerow(msg)
                    break

                if guesses == 0:
                    print("Gameover! You have ran out of guesses, the correct answer was "+str(answer)+".")
                    break
            except:
                print("Please enter 'quit' or a number.")
    if mode == 'timed': # This is WIP and it won't work.
        is_running = True
        while is_running == True:
            time_left = start_timer(time_left)
            timed_gamemode(mode, max_num, guesses, time_left, answer, start_time)



def difficulty_select(mode):
    is_running = True
    while is_running == True:
        print("Select a difficulty to start the game. DIFFICULTIES: QUICK, EASY, NORMAL, HARD, EXTREME")

        diff_sel = input("   ").lower()

        if diff_sel in gd:
            begin_ng(mode, diff_sel)
        else:
            print("Error")
            continue


def mode_select():
    is_running = True
    while is_running == True:
        print("Select a mode. MODES: NORMAL")

        mode_sel = input("   ").lower()

        if mode_sel in gm:
            difficulty_select(mode_sel)
        else:
            print("Error")
            continue

def start_game():
    is_running = True
    while is_running == True:
        print("Type 'start' to begin, type 'quit' to end the program")

        open_ng = input("  ")

        if open_ng == 'start':
            mode_select()
        elif open_ng == 'quit':
            quit()
        else:
            print("Error")
            continue

### GAME DO NOT TOUCH (please) ### 

start_game()




