import math
import decimal

arg = int(input("What value of the Gauss Error Function would you like to compute? : "))
iterate = input("How many iterations of the algorithm do you want to compute? : ")
inf1 = int(input("What number should be substituted for infinity in the limit? : "))
decimal.getcontext().prec = 1 + (int(input("How much precision of digits would you like to compute for each calculation? : ")))

pi = 0

for i in range(int(iterate)):
    s1 = decimal.Decimal(
        decimal.Decimal(math.factorial(6 * i) * ((545140134 * i) + 13591409))
        / decimal.Decimal(
            (
                math.factorial(3 * i)
                * (math.factorial(i) ** 3)
                * ((-262537412640768000) ** i)
            )
        )
    )
    pi = pi + (s1)
pi = 1 / decimal.Decimal(pi)
pi = pi * (426880 * (decimal.Decimal(10005).sqrt()))

def sgn(x):
    if(x>0):
        y = 1
    elif(x<0):
        y = -1
    else:
        y = 0
    return y

def exp(x, inf):
    e = ((1+(decimal.Decimal(x)/decimal.Decimal(inf)))**inf);
    return e

a = 8*(pi-3)/(3*pi*(4-pi))

f = -(arg**2)*(4/pi+a*(arg**2))/(1+a*(arg**2))

p1 = sgn(arg)

p2 = decimal.Decimal(1-exp(f, inf1)).sqrt()

final = p1*p2

print(final)