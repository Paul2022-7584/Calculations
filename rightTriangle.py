# Put your code here:
FirstSide = int(input("Enter the first side: "))
SecondSide = int(input("Enter the second side: "))
ThirdSide = int(input("Enter the third side: "))

if ((FirstSide**2 == SecondSide**2 + ThirdSide**2) or
(FirstSide**2 + SecondSide**2 == ThirdSide**2) or
(FirstSide**2 + ThirdSide**2 == SecondSide**2)):
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
