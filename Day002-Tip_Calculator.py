print("hey there!, Welcome to the tip calculator")
total_bill=float(input("What is the total bill ?\nINR"))
tip=int(input("What percentage would you like to give as tip \n"))
split_bill=int(input("how many people to split the bill \n"))
total_tip_amount= tip / 100 * total_bill + total_bill
print(f"total tip amount {total_tip_amount}")
bill_per_person=round(total_tip_amount / split_bill,2)
print(f"each person pay bill is INR {bill_per_person}")
