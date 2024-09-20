from http.client import IncompleteRead

print("Hey there....! \n Welcome to the code Pizza delivery")
size=input("What size pizza do you want ? Small,Medium,Large :")
pepperoni=input("Do you want pepperoni on your pizza ? Yes / No :")
extra_cheese=input("Do you want extra cheese ? Yes/No :")
print( f"you have ordered {size} pizza")
bill=0
if size=="small":
    bill=200
elif size=="medium":
    bill=400
if size=="Large":
        bill=600
if pepperoni=="yes":
    bill+=20
if extra_cheese=="yes":
    bill+=50
print(f"Your final bill is {bill}")










