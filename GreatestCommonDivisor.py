# Put your code here
small = int(input("Enter the smaller number: "))
large = int(input("Enter the larger number: "))

for i in range(1, small + 1):
    if (small % i == 0) and (large % i == 0):
        gcd = i

print("\nThe greatest common divisor is {}".format(gcd))
