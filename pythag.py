from math import sqrt
from banner import banner

banner("Pythagorean Calculator", "by Trendel")

print("we will help you find the missing side of a right triangle.")
print("The lengths of the two lags are 'a' and 'b', and the length of the hypotenuse is 'c'.")

print("")

print("Please enter the length of each side, or leave it blank if yo u don't know.")

a = (input("a: "))
a = float(a)

b = (input("b: "))	
b = float(b)

c = (input("c: "))
c = float(c)

if a != "":
    a = float(a)
elif b != "":
    b = float(b)
elif c != "":
    c = float(c)
c = sqrt(a**2 + b**2)

b = sqrt(c**2 + a**2)
a = sqrt(b**2 + c**2)


print("The length of the hypotenuse is", c )
print("The length of the hypotenuse is",a)






