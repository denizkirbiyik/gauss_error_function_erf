import decimal
import math

up_lim = int(input("What value of the Gauss Error Function would you like to compute? : "))
inf1 = int(input("What number should be substituted for infinity in the limit? : "))
iterate = input("How many iterations of the algorithm for pi do you want to compute? : ")
decimal.getcontext().prec = 1 + (int(input("How much precision of digits would you like to compute for each calculation? : ")))
dtr = int(input("The reciprocal of what number should be the length of dt? : "))

dt = decimal.Decimal(1/dtr)

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
 

def exp(x, inf):
    e = ((1+(decimal.Decimal(x)/decimal.Decimal(inf)))**inf);
    return e

def func(t):
    tout = 1/exp(t**2, inf1)
    return tout

def integration(upper, dif, difr):
    log = 0
    for i in range(0, (upper-1)*difr):
        log += func(i*dif)
    return log*dif
integral = integration(up_lim, dt, dtr)
print(integral*2/decimal.Decimal(pi).sqrt())
