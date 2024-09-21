import random
print("Get Ready to Rock!\nWelcome to the ultimate Rock-Paper-Scissors showdown!")
user_input=int(input('choose type 1 for ROCK/ 2 for PAPER/ 3 for SCISSOR \n'))
computer_input=random.randint(0,2)
print(f"computer_input is{computer_input}")
if user_input=="0" and computer_input=="2":
    print("YOU WON.....")
elif user_input=="2" and computer_input=="1":
    print("YOU WIN....")
elif user_input=="1" and computer_input=="0":
    print("YOU WON....")
elif computer_input>user_input:
    print("YOU LOST....")
elif user_input>computer_input:
    print("YOU WIN...")
elif computer_input==user_input:
    print("game draw")
else :
    print("incorrect choose")
    









