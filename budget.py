""" A simple budget tracker for manual entries written in Python"""
"""Apply for loop values here as a dictionary of deductions: key = label, value = amount, loop for the dictionary and tie it to each input value"""

""" What is an easy way to turn an expense into a question? I want to be able to make some of these variable i.e. ElectricBill = float(input("What was your electric bill this month?")) Feeds my dictionary amount for ElectricBill which then combines with other key values to create my object MonthlyExpenses. Can I  have that combination of fixed and variable items wwithin a dictionary, or should I create a string of elif statements and broaden my initial UseDecision statement?   """

MonthlyExpenses = items(Mortgage 3034.88: , HOAPayment : 73, CarPayment : 1670.22, Audible : 15.99, BabySittingFee : 300, ChurchDonation : 103.29, TogoDonation : 60, ChatGPT : 20, Netflix : 15.49, WSJ : 4, NYT : 4, Adobe : 19.99, DisneyPlus : 24.99, KindleUnlimited : 11.99, Internet : 105.91, Spotify : 16.99, AllstateInsurance : 200.10 CellPhone : )

MonthlyIncomeStream = items(PayCheck : 9300, Disability : 4202)

VariableExpenses = items(ElectricBill : , Sanitation : , WaterBill : ,)

print ("Welcome to wasting less money!")
InitialFunds = float(input("How much money is in your combined accounts?"))
MonthlyIncome = float(input("What is your monthly base income?"))#move this to a dict

CurrentFunds = InitialFunds + MonthlyIncome
while True:
    
    UseDecision = input("Will you be adding or subtracting funds?")
    
    if UseDecision == "adding":
        MoreFunds = float(input("What amount of $$ were added?"))
        CurrentFunds += MoreFunds
        print (f"Congratulations! Your account now has ${CurrentFunds} in it!")
    elif UseDecision == "subtracting": 
        LessFunds = float(input("What amount of $$ were spent?"))
        CurrentFunds -= LessFunds
        print (f"Congratulations! Your account now has ${CurrentFunds} in it!")
    else:
        break
