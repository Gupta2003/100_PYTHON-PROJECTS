print("Welcome to the trip calculator : \n")
amount = int(input("What was the total bill ? \n"))
tip = int(input("How much percentage of tip would you like to give? 10, 12, or 15? \n"))
if(tip == 10 ):
    tip = (amount*10)/100
elif(tip == 12):
    tip = (amount*12)/100
elif(tip == 15):
    tip = (amount*15)/100
else:
    print("Please enter a valid percent")
final_amount = tip + amount
people = int(input("How many people to split the bill?\n"))
final_bill = final_amount/people
print("Each person should pay : ", final_bill)