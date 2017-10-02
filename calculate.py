import math
from decimal import *

def FunctionF(number):
    return Decimal(-3* number).exp()
def FunctionN(number):
    return Decimal(-3* number).exp() - Decimal(number)
def DerivativeN(number):
    return Decimal(-3)* Decimal(-3* number).exp() - Decimal(1)

limit = 1000

def NewtonMethod(startingPoint, precision):
    getcontext().prec = precision
    precision = 10**(-1 * precision)

    nextNumber = Decimal(startingPoint)
    iteration = 1
    while abs(FunctionN(nextNumber)) > Decimal(precision):
        if iteration > limit:
            print ("Too much operations")
            return
        nextNumber = nextNumber - FunctionN(nextNumber)/DerivativeN(nextNumber)
        print ("{0}         | {1} | {2}".format(iteration, nextNumber, FunctionN(nextNumber)))
        iteration += 1
    print ("Found. {0}".format(nextNumber))

def FixedPointIterationMethod(startingPoint, precision):
    getcontext().prec = precision
    precision = 10**(-1 * precision)

    previousNumber = Decimal(startingPoint)
    nextNumber = FunctionF(previousNumber)
    iteration = 1
    while abs(previousNumber - nextNumber) > Decimal(precision):
        if iteration > limit:
            print ("Too much operations")
            return
        previousNumber = nextNumber
        nextNumber = FunctionF(previousNumber)
        print ("{0}         | {1}".format(iteration, nextNumber))
        iteration += 1
    print ("Found. {0}".format(nextNumber))

def Main():
    print ("Program to calculate e^(-3x) - x = 0 ")

    startingPoint = int(input ("Pease input start point. "))
    precision = int(input ("Pease input precision. "))
    while True:
        method = input("Choose method. 1 - Fixed point iteration, 2 - Newton. ")
        print("Iteration | Aproximation")
        if method == "1":
            FixedPointIterationMethod(startingPoint, precision)
            break
        elif method == "2":
            NewtonMethod(startingPoint, precision)
            break
        else:
            print("Wrong input.")

Main()
