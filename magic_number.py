#!/usr/bin/python

#Magic number problem: it's a prime number and its position in the list equals its value. The positions in the list start at zero

#num1 represents the number to test primality - 1
def is_prime(num, num1):
    print "pasamos %d" % num
    raw_input("Press enter to continue")
    if num < 2:
        answer = 0 #no prime
    if (num % num1 == 0):
        answer = 0 #no prime
    elif (num % num1 != 0 and num1 != 2):
        isprime(num, num1 - 1)
    else:
        answer = 1 #is prime
    return answer


def isprime1(n):
    if n == 2 or n == 3: return True
    elif n == 1 or n % 2 == 0 or n % 3 == 0: return False 
    divisor = n - 1
    while (divisor > 0):
        if n % divisor == 0:
            return False
        divisor = divisor - 1
    return True

#prime numbers we gotta calculate only factors up to its square root 
#also keep in mind that only odd numbers (except 2) are primes
#also the fact that for primes > 4 the prime%6 must be 1 or 5.
def isprime(n):
    sqrt_n = int(n**0.5 + 0.5)
    if n == 2 or n == 3: return True
    elif n < 2 or n % 2 == 0 or n % 3 == 0: return False
    divisor = 5
    increment = 2
    while divisor <= sqrt_n:
        if n % divisor == 0:
            return False
        divisor += increment
        increment = 6 - increment # toggle: 2-> 4 -> 2 ...
    return True

def sequential():
    f = open('numbers.txt', 'r')
    i=0
    for line in f:
        num_line = int(line)
        print num_line, " versus ", i
        if ((num_line == i) and isprime(i)):
            print "The number is %d" % i
            f.close()
            exit(1)
        i = i + 1
    print "Something went bad!"
    f.close()

print isprime(2147483647)
#sequential()
