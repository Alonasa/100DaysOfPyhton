'''
  That module count tips
'''

print("Welcome to the tip calculator!")
bill_amount = float(input("What was the total bill? "))
amount_people = int(input("How many people to split the bill? "))
tip_percent = int(input("What percentage tip would you like to give? "))
to_pay = (bill_amount + bill_amount * (tip_percent/100))/amount_people
print(f"Each person should pay: ${to_pay}")
