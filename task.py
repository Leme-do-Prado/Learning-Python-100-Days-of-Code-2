
print("Hello! Let's calculate your suggested tip and bill splits. \n"
      + "Im going to ask you some questions now.")
tipPercentage = float(input("1. What's your desired tip percentage?\n"))/100
totalAmount = float(input("2. What's the total bill amount? \n$"))
peopleAmount = int(input("3. How many people you're in? \n"))


splitBill = (totalAmount * (1 + tipPercentage)) / peopleAmount
splitBill = round(splitBill, 2)

print("Your suggested tip is " + str(totalAmount * tipPercentage))
print("The suggested splits are of " + str(splitBill) + " pounds each.")
print("(or " + str((totalAmount * tipPercentage)/peopleAmount) + ", for just the tips.)")



