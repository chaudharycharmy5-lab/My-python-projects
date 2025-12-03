print("Welcome to the tip calculator.")
bill=float(input("What was the total amount?Rs."))
tip=int(input("How much tip would you like to give? 10, 12 or 15?"))
people=int(input("How many people to split the bill?"))
Total_bill=bill+(bill*tip/100)
pay=Total_bill/people
print(f"Each person should pay Rs.{pay}")