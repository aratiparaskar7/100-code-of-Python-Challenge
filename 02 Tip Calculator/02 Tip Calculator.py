#Tip Calculator

print("Welcome to the Tip Calculator!")
# Taking I/P from user
bill=float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? (10,12 or 15)  "))
N_of_person = int(input("How many people to split the bill? "))
#performing operation
Amount_per_person = ( bill + tip/100 * bill  )/N_of_person
#printing Results
print(f"Each person should pay :{Amount_per_person} ")