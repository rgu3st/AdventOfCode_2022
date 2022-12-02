from enum import Enum

LOSE = 0
TIE = 3
WIN = 6
CHOOSE_LOSE = 'lose'
CHOOSE_TIE = 'tie'
CHOOSE_WIN = 'win'
SHAPE_SCORES = {"rock":1, "paper":2, "scissors":3}
ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

def decode_choice(choice):
    if choice in ['A', 'X']:
        return ROCK
    if choice in ['B', 'Y']:
        return PAPER
    if choice in ['C', 'Z']:
        return SCISSORS
    else:
        return "Not Found"

def decode_part2(choice):
    if ROCK == choice:
        return CHOOSE_LOSE
    elif PAPER == choice:
        return CHOOSE_TIE
    else:
        return CHOOSE_WIN

def get_win_score(opponent_choice:str, my_choice:str)->int:
    #print("Checking: ", opponent_choice, " and ", my_choice)
    if opponent_choice == my_choice:
        return TIE
    elif opponent_choice == ROCK and my_choice == PAPER:
        return WIN
    elif opponent_choice == ROCK and my_choice == SCISSORS:
        return LOSE
    elif opponent_choice == PAPER and my_choice == ROCK:
        return LOSE
    elif opponent_choice == PAPER and my_choice == SCISSORS:
        return WIN
    elif opponent_choice == SCISSORS and my_choice == ROCK:
        return WIN
    elif opponent_choice == SCISSORS and my_choice == PAPER:
        return LOSE

def get_win_choice(opponent_choice:str)->str:
    if opponent_choice == ROCK:
        return PAPER
    elif opponent_choice == PAPER:
        return SCISSORS
    else:
        return ROCK

def get_lose_choice(opponent_choice:str)->str:
    if opponent_choice == ROCK:
        return SCISSORS
    elif opponent_choice == PAPER:
        return ROCK
    else:
        return PAPER

def get_tie_choice(opponent_choice:str)->str:
    return opponent_choice

def calculate_score(opponent_choice:str, my_choice:str):
    score = get_win_score(opponent_choice, my_choice)
    score += SHAPE_SCORES[my_choice]
    return score

''' This calculates what result we want, based on my_choice, wether to win, lose, or draw'''
def calculate_score_part2(opponent_choice:str, win_choice:str):
    my_choice = ''
    print(f"Win choice: {win_choice}")
    if CHOOSE_WIN == win_choice:
        my_choice = get_win_choice(opponent_choice)
        print(f"Need to win, using {my_choice} vs. {opponent_choice}")
    elif CHOOSE_TIE == win_choice:
        my_choice = get_tie_choice(opponent_choice)
        print(f"Need to tie, using {my_choice} vs. {opponent_choice}")
    else:
        my_choice = get_lose_choice(opponent_choice)
        print(f"Need to lose, using {my_choice} vs. {opponent_choice}")
    score = get_win_score(opponent_choice, my_choice)
    score += SHAPE_SCORES[my_choice]
    return score

def run():
    print("Running day 2.")

    inputData = []

    with open("./Data/input_day2.txt", 'r') as fileData:
        inputData = fileData.readlines()

    total_score_part1 = 0
    total_score_part2 = 0
    # Quick test: update soonest:
    #inputData = ["A Y", "B X", "C Z"]

    for line in inputData:
        #print(line)
        opponent_choice = decode_choice(line[0])
        my_choice = decode_choice(line[2])
        this_score = calculate_score(opponent_choice, my_choice)
        total_score_part1 += this_score
        #print(f"score {this_score} for: {opponent_choice}, {my_choice}")
        my_choice = decode_part2(my_choice)
        this_score2 = calculate_score_part2(opponent_choice, my_choice)
        #print(this_score2)
        total_score_part2 += this_score2

    print(f"Total score: {total_score_part1}")
    print(f"Total score, part2: {total_score_part2}")