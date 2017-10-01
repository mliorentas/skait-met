import math

def NewtonMethod():
    print ("Not implemented.")


def FixedPointIterationMethod(startingPoint, precision):
    previousNumber = startingPoint
    nextNumber = math.exp(-3 * startingPoint)
    while abs(previousNumber - nextNumber) > precision:
        nextNumber = math.exp(-3 * nextNumber)
        print (nextNumber)
    print ("Found. {0}".format(nextNumber))

print ("Hello to hell.")
# intervalStart = input ("Please input start of interval. ")
# intervalEnd = input ("Please input end of interval. ")
# startingPoint = input ("Pease input start point. ")
# precision = input ("Pease input precision. ")
startingPoint = 0.4
precision = 0.001

while True:
    # method = input("Choose method. 1 - fixed point iteration, 2 - Newton. ")
    method = "1"
    if method == "1":
        FixedPointIterationMethod(startingPoint, precision)
        break
    elif method == "2":

        break
    else:
        print("Wrong input.")
