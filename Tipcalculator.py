print("Welcome to the tip to the calculator!")
bill=int(input("What was the total bill?$"))
tip=int(input("How much tip like to give?10,12, or 15"))
split=int(input("How many people to split the bill?"))

tip_as_percent=tip/100
total_tip_amount=bill*tip_as_percent
total_bill=bill+total_tip_amount
bill_per_person=total_bill/split

print(f"Each person should pay:${bill_per_person}")