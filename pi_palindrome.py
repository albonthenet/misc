#!/usr/bin/python

#amazon problem for jobs website
#This is a simple dirty non error checking non efficient program to solve:


# The problem says:
#find the 1st 10 digits palindrome in the digits of Pi
import math
from sympy.mpmath import mp

mp.dps = 100000  # number of digits

def ispalindrom(strin):
    #print "La palabra tiene longitud:", len(strin)
    str_inv = strin[::-1]
    if strin == str_inv:
        return True
    else:
        return False

print "Calculating %d decimal numbers of pi (%f...)" % (mp.dps, math.pi)
#Convert decimals to string and trim the integer part
pi_str = str(mp.pi)
pi_str = pi_str[2:]
print pi_str

limit = 0
while limit < 300:
    limit = limit + mp.dps
    if limit < mp.dps:
        i = 0
    else:
        i = limit + 1
    for i in xrange(limit):
        print pi_str[i:(i+10)]
        if ispalindrom(pi_str[i:(i+10)]):
            print "The number %s is a palindrom, starting at the position %d of pi decimals" % (pi_str[i:(i+10)], i)
            exit()
print "Something went bad!!"

