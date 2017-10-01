import math
from decimal import *

def FunctionF(number):
    return Decimal(-3* number).exp()
def FunctionN(number):
    return Decimal(-3* number).exp() - number
def DerivativeN(number):
    return Decimal(-3)* Decimal(-3* number).exp() - Decimal(1)

limit = 100

def NewtonMethod(startingPoint, precision):
    getcontext().prec = 50
    nextNumber = Decimal(startingPoint)
    iteration = 1
    # for x in range (1, 50):
    while abs(FunctionN(nextNumber)) > Decimal(precision):
        if iteration > limit:
            print ("Too much operations")
            return
        nextNumber = nextNumber - FunctionN(nextNumber)/DerivativeN(nextNumber)
        print (nextNumber)
        iteration += 1
    print ("Found. {0}".format(nextNumber))

def FixedPointIterationMethod(startingPoint, precision):
    getcontext().prec = 50
    previousNumber = Decimal(startingPoint)
    nextNumber = FunctionF(previousNumber)
    iteration = 1
    # for x in range (1, 50):
    while abs(previousNumber - nextNumber) > Decimal(precision):
        if iteration > limit:
            print ("Too much operations")
            return
        previousNumber = nextNumber
        nextNumber = FunctionF(previousNumber)
        print (nextNumber)
        iteration += 1
    print ("Found. {0}".format(nextNumber))


print ("Program to calculate e^(-3x) - x = 0 ")
startingPoint = 0
precision = 0.0000001

# startingPoint = input ("Pease input start point. ")
# precision = input ("Pease input precision. ")

while True:
    # method = input("Choose method. 1 - fixed point iteration, 2 - Newton. ")
    method = "2"
    if method == "1":
        FixedPointIterationMethod(startingPoint, precision)
        break
    elif method == "2":
        NewtonMethod(startingPoint, precision)
        break
    else:
        print("Wrong input.")
