# intreverse(n) that takes as input a positive integer n and returns the integer
# obtained by reversing the digits in n

def intreverse(n):
    i = 0
    m = 0
    while (n != 0):
        d = n%10
        (m, n) = (m*10 + d, n//10)
        i = i + 1
    return m

# matched(s) that takes as input a string s and checks if the brackets "(" and
# ")" in s are matched: that is, every "(" has a matching ")" after it and every
# ")" has a matching "(" before it.  Your function should ignore all other
# symbols that appear in s.  Your function should return True if s has matched
# brackets and False if it does not.

def matched(s):
    flag = 0
    for i in s:
        if (i == '('):
            flag = flag + 1
        elif ((i == ')') and (flag > 0)):
            flag = flag - 1
    return (not(flag%2))

# sumprimes(l) that takes as input a list of integers and retuns the sum of all
# the prime numbers in l.

def isprime(n):
    if (n > 0):
        if (n == 1):
            return False
        for i in range(2,n):
            if (not(n % i)):
                return False
        return True
    else:
        return False

def sumprimes(l):
    sum = 0
    for i in l:
        if (isprime (i)):
            sum = sum + i
    return sum
