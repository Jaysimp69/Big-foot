import random
guessesused = 0
def play_a_game():
    name = input('what is your name?')   
    ans = print(input('Well welcome back, '+ name +', Do you want to play a game?'))
    if ans == "yes":
        while True:
            Number1 = int (input ("Enter you first number"))
            Number2 = int (input ("Enter you second number"))
    if ans == "no":
         sore_loser()
            

def sore_loser():
    print('why not?')


game= play_a_game()



