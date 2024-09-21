import random
print("Welcome to the ultimate coin flip showdown! Heads or Tails, let's see where luck takes you today!")
user_input=input('choose "HEADS" or "Tails"').lower()
heads_and_tails=random.randint(0,1)
if heads_and_tails==0:
    print("Heads")
    if user_input=="heads":
        print("Congratulations \n Heads up, you're the champion!")
else:
    print("Tails")
    if user_input=="tails":
        print("Congratulations \n Tails of success! You won!")

