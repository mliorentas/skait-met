def iter_primes():
     # an iterator of all numbers between 2 and +infinity
     numbers = itertools.count(2)

     # generate primes forever
     while True:
         # get the first number from the iterator (always a prime)
         prime = numbers.next()
         yield prime

         # this code iteratively builds up a chain of
         # filters...slightly tricky, but ponder it a bit
         numbers = itertools.ifilter(prime.__rmod__, numbers)

for p in iter_primes():
    if p > 1000:
        break
    print p
method = input("Choose method. 1 - fixed point iteration, 2 - Newton")
if method == 1

elif mothod == 2
if x == 'a':
    # Do the thing
elif x == 'b':
    # Do the other thing
if x in 'bc':
    # Fall-through by not using elif, but now the default case includes case 'a'!
elif x in 'xyz':
    # Do yet another thing
else:
    # Do the default
