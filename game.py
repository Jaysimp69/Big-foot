from re import X
import time
# day = input('what day is it john?: ')

# if day == 'thursday' :
#     print('Damn we have warrior task and battle drills')
#     eod= input(' What time is it at?: ')
#     if eod ==  '1750' :
#         print('thats later than wednesday')
#     else:
#         print(' Wtf, thats too damn early.')
# else: 
#     print("I still ahve time to go to the gym")

attempts = 0
x = 'password'

    #increment the number of attempts
def ask_for_password():
    password = input('Please enter your password.\n')
    pass_attempts(password)
    #return password

def pass_attempts(password):
    global attempts
    while password != x and attempts < 4:
        attempts = attempts + 1
        total_attempts = 5
        remaining_attempts = total_attempts - attempts
        print(f'Incorrect password. You have {remaining_attempts} attempts left.')
        password = ask_for_password()

# #ask the user to input their password
password = ask_for_password()

        
if password == x:
    print("you're in.")
else:
    print("you have been locked out of your account, bitch\nCreate a new password. Enter a new one:")
    x = input()
    ask_for_password()




# attempts = 0
# total_attempts = 5
# password = ''
# while password != 'password':
#     print('Enter your password:')
#     password =input()
#     attempts = attempts + 1
#     remaining_attempts = total_attempts - attempts
#     if password != 'password':
#         print(f'Incorrect password... {remaining_attempts}, attempts left') #Number of attempts left
#         while attempts < 5:
            
#             # int(print('Incorrect password', attempts ,' attempts left')) #Number of attempts left



# print('Thank you!')

# name = input('Now i have your info fool')
# print('thank you')

# x = 2
# while x < 1000:
#     print(x)
#     x = x ** 2
#     time.sleep(1)

# print('I am out of the loop')