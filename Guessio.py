import random
import sys
import time




# attempts = 0
#Do you like games?
def play_a_game(input):
    name = input('what should I call you?\n')   
    ans = input('Well welcome back, '+ name +', Do you want to play a game?\n')
    while ans == "yes":
        pick_a_number()
    while ans == "no":
         sore_loser()

#Start with a choice
def pick_a_number():
    while True:
        number1 = int(input("Enter your first number:\n"))

        number2 = int(input("Enter your second number:\n"))
        
        #now compare the largest values
        if (number2<number1) and (number1>number2):
            least = number2
            largest = number1
        elif (number1<number2) and (number2>number1):
            least = number1
            largest = number2
        #start guesses
        
        guess= int(input(f'Im thinking of a number between {least} and {largest} ...What is it?\n'))
        n= random.randint(least,largest)
        while n != guess:
            def just_right(y):
                if y < n:
                    print ("Your number is too low. Guess again:\n")
                    # y= int(input("guess again:\n"))
                    # return 
                elif y > n:
                    print ("Your number is too high. Guess again:\n")
                    # guess = int(input("guess again:\n"))
                    # y= int(input("guess again:\n"))
                    # return
                # else:
                #     print ("You guessed it!")
                #     ans= input("Do you want to play again?\n")
                #     if ans == 'yes':
                #         return pick_a_number()
                #     if ans == 'no':
                #         print('Bye')
            def guess_attempts(y,t):
                # global attempts
                attempts = 0
                while y != t and attempts < 5:
                    attempts = attempts + 1
                    total_attempts = 5
                    remaining_attempts = total_attempts - attempts
                    if remaining_attempts == 0:
                        print("GAME OVER")
                        time.sleep(.5)
                        again = input("Do you want to play again?\n")
                        if again == 'yes':
                                play_a_game()
                        else: 
                            sys.exit
                    print(f'Wrong Answer. You have {remaining_attempts} attempts left.')
                    just_right(y)
                    y= int(input())
                    # if remaining_attempts == 0:
                    #     print("GAME OVER")
                    #     time.sleep(.5)
                    #     again = input("Do you want to play again?")
                    #     if again == "yes":
                    #         play_a_game
                    #     else: 
                    #         sys.exit
                            
                    
            guess_attempts(guess,n)
                  
            if n == "guess":
                print ("You guessed it!")
                ans= input("Do you want to play again?\n")
                if ans == 'yes':
                    pick_a_number()
                if ans == 'no':
                    print('Bye')
            # def just_right():
            #     if guess < n:
            #         print ("your number is too low\n")
            #         # guess = int(input("guess again:\n"))
            #         guess_attempts(guess,n)
            #     elif guess > n:
            #         print ("you number is too high\n")
            #         # guess = int(input("guess again:\n"))
            #         guess_attempts(guess,n)
            #     else:
            #         print ("You guessed it!")
            #         ans= input("Do you want to play again?\n")
            #         if ans == 'yes':
            #             return pick_a_number()
            #         if ans == 'no':
            #             print('Bye')
                # def guess_attempts(game):
                #     global attempts
                #     while game != n and attempts < 5:
                #         attempts = attempts + 1
                #         total_attempts = 6
                #         remaining_attempts = total_attempts - attempts
                #         # print(f'Incorrect password. You have {remaining_attempts} attempts left.')
                #         guess = int(input("guess again:\n"))
                         
        
                



#try this game
def sore_loser():
    print('ok, Ill ask you again in 5 seconds')
    time.sleep(5)
    print('Do you want to play now?')
    time.sleep(.5)
    print('Sike, Lets Play')
    time.sleep(1)
    pick_a_number()
        


# def repeat():
    

#random is the name of the game
game = play_a_game(input)




