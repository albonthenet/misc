#!/usr/bin/python

#amazon problem for jobs website
#find the 1st 10 digits palindrome in the digits of Pi
import math
from sympy.mpmath import mp



mp.dps = 100  # number of digits
#print(mp.pi)   # print pi to a thousand places

print "Calculating %d decimal numbers of pi (%d)" % (mp.dps, math.pi)

#Convert decimals to string
pi_str = str(mp.pi)


print pi_str[2]

'''
n=0
for n to limit
leer n .. n+4
	if substr(n..n+4) == substr(n+4..n)
		print n..n+4 is the number
	else
		n++
'''
