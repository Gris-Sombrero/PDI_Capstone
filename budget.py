""" A simple budget tracker for manual entries written in Python"""

print ("Welcome to wasting less money!")
initial_funds = 1000

use_decision = input("Will you be adding or subtracting funds?")

if use_decision == "adding":
    more_funds = float(input("How much money are you bringing to the table?"))
    initial_funds = initial_funds + more_funds
    print (f"Congratulations! Your account now has {initial_funds} in it!")
elif use_decision == "Too much":
    print ("I hate seeing you so hopeless")
else:
    print ("You chose subtract :(")
    less_funds = float(input("Geez, how much did you spend this time?"))
    initial_funds = initial_funds - less_funds
    print (f"Make better decisions, you now only have {initial_funds} in your account")


