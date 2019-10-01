# Eratosthenes

# Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
# Initially, let p equal 2, the smallest prime number.
# Enumerate the multiples of p by counting in increments of p from 2p to n, and mark them in the list (these will be 2p, 3p, 4p, ...; the p itself should not be marked).
# Find the first number greater than p in the list that is not marked. If there was no such number, stop. Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.
# When the algorithm terminates, the numbers remaining not marked in the list are all the primes below n.

import sys
import math

def remove_multiples(arr, n, x):
  for y in range(2*x, n, x):
    # print(p)
    if y in arr:
      arr.remove(y)
  # print(arr)
  return arr


def eratosthenes(n):
  numbers = [m for m in range(2, n)]
  # print(numbers)
  # numbers = remove_multiples(numbers, n, 2)
  # print(numbers)
  # numbers = remove_multiples(numbers, n, 3)
  # print(numbers)
  for x in numbers:
    if x < math.sqrt(n):
      # print(x)
      numbers = remove_multiples(numbers, n, x)
      # print(numbers)   
  return numbers 

def prime(n):
  intn = int(n)
  primes = eratosthenes(intn)
  # print(primes)
  for x in primes:
    if x < math.sqrt(intn):
      if intn % x == 0:
        print('not a prime')
        return 0
  print('prime!')
  return 1

prime(sys.argv[1])
