from math import exp
from decimal import *

def FunctionF(number):
    return exp(-3* number)
def FunctionN(number):
    return exp(-3* number) - number
def DerivativeN(number):
    return (-3)* exp(-3* number) - 1

limit = 1000

def NewtonMethod(startingPoint, precision):
    digitsAfterPoint = precision
    precision = 10**(-1 * precision)

    nextNumber = startingPoint
    iteration = 1
    while abs(FunctionN(nextNumber)) > precision:
        if iteration > limit:
            print ("Too much operations")
            return
        nextNumber = nextNumber - FunctionN(nextNumber)/DerivativeN(nextNumber)
        print ("{0}         | {1} | {2}".format(iteration, round(nextNumber,digitsAfterPoint), FunctionN(nextNumber)))
        iteration += 1
    print ("Found. {0}".format(round(nextNumber,digitsAfterPoint)))

def FixedPointIterationMethod(startingPoint, precision):
    digitsAfterPoint = precision
    precision = 10**(-1 * precision)

    previousNumber = startingPoint
    nextNumber = FunctionF(previousNumber)
    iteration = 1
    while abs(previousNumber - nextNumber) > precision:
        if iteration > limit:
            print ("Too much operations")
            return
        previousNumber = nextNumber
        nextNumber = FunctionF(previousNumber)
        print ("{0}         | {1} | {2}".format(iteration, round(nextNumber,digitsAfterPoint), previousNumber - nextNumber))
        iteration += 1
    print ("Found. {0}".format(round(nextNumber,digitsAfterPoint)))

def Main():
    print ("Program to calculate e^(-3x) - x = 0 ")

    startingPoint = int(input ("Pease input start point. "))
    precision = int(input ("Pease input precision. "))
    while True:
        method = input("Choose method. 1 - Fixed point iteration, 2 - Newton. ")
        print("Iteration | Aproximation | q")
        if method == "1":
            FixedPointIterationMethod(startingPoint, precision)
            break
        elif method == "2":
            NewtonMethod(startingPoint, precision)
            break
        else:
            print("Wrong input.")

Main()
