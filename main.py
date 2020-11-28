import random

player_score = 0
computer_score = 0
match_round_number = 1

main_arr = ['r', 'p', 's'] # Rock-Paper-Scissor

def computer_turn():
    return random.choice(main_arr)

def player_turn():
    pt = input("Enter r for rock or p for paper or s for scissor: ")
    while True:
        if pt not in main_arr:
            print("Enter a valid character please")
            pt = input("Enter r for rock or p for paper or s for scissor: ")
        else:
            break
    return pt

def check_token(pt, ct):
    global player_score, computer_score
    def simple():
        print("Player token:", pt)
        print("Computer token:", ct)
    if pt == ct:
        simple()
        print("Draw..")
    else:
        if pt == 'r' and ct == 's':
            simple()
            player_score += 1
            print("Player gains a point..")
        elif pt == 'p' and ct == 'r':
            simple()
            player_score += 1
            print("Player gains a point..")
        elif pt == 's' and ct == 'p':
            simple()
            player_score += 1
            print("Player gains a point..")
        elif ct == 'r' and pt == 's':
            simple()
            computer_score += 1
            print("Computer gains a point..")
        elif ct == 'p' and pt == 'r':
            simple()
            computer_score += 1
            print("Computer gains a point..")
        elif ct == 's' and pt == 'p':
            simple()
            computer_score += 1
            print("Computer gains a point..")

def main():
    global match_round_number
    print("Round no: ", match_round_number)
    pt = player_turn()
    ct = computer_turn()
    check_token(pt, ct)
    print("Player Score: ", player_score)
    print("Computer Score: ", computer_score)
    match_round_number += 1


if __name__ == "__main__":
    print("Welcome to the Rock-Paper-Scissor game")
    print("Total rounds 10")
    for i in range(10):
        main()
    if player_score > computer_score:
        print("Player wins the match...")
    elif computer_score > player_score:
        print("Computer wins the match...")
    else:
        print("Match Draw...")
