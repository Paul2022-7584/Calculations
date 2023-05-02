# Put your code here
wage = float(input("Please enter the wage: "))
regularHours = int(input("Please enter the regular hours: "))
overTimeHours = int(input("Please enter the overtime hours: "))
overTime = (overTimeHours * 1.5 * wage)

weeklyPay = (wage * regularHours + overTime)

print("The total weekly pay is " + str(weeklyPay))

