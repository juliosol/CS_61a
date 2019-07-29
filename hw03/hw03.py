HW_SOURCE_FILE = 'hw03.py'

#############
# Questions #
#############

from operator import add, mul, sub

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'has_seven',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if k % 10 == 7:
        return True
    elif k < 10 and k != 7:
        return False
    else:
        return has_seven(k//10)

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    def ping_helper(counter, i):
        if counter == n:
            return 1
        if counter % 7 == 0 or has_seven(counter):
            return 1 - ping_helper(counter + 1, 1)
        else:
            return 1 + ping_helper(counter + 1, 1)

    return ping_helper(1,1)


def accumulate(combiner, base, n, term):
    """Return the result of combining the first n terms in a sequence and base.
    The terms to be combined are term(1), term(2), ..., term(n).  combiner is a
    two-argument, associative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    """
    total, k = base, 1
    while k <= n:
        total, k = combiner(total, term(k)), k + 1
    return total

def filtered_accumulate(combiner, base, pred, n, term):
    """Return the result of combining the terms in a sequence of N terms
    that satisfy the predicate pred. combiner is a two-argument function.
    If v1, v2, ..., vk are the values in term(1), term(2), ..., term(N)
    that satisfy pred, then the result is
         base combiner v1 combiner v2 ... combiner vk
    (treating combiner as if it were a binary operator, like +). The
    implementation uses accumulate.

    >>> filtered_accumulate(add, 0, lambda x: True, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> filtered_accumulate(add, 11, lambda x: False, 5, identity) # 11
    11
    >>> filtered_accumulate(add, 0, odd, 5, identity)   # 0 + 1 + 3 + 5
    9
    >>> filtered_accumulate(mul, 1, greater_than_5, 5, square)  # 1 * 9 * 16 * 25
    3600
    >>> # Do not use while/for loops or recursion
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'filtered_accumulate',
    ...       ['While', 'For', 'Recursion'])
    True
    """
    def combine_if(x, y):
        "*** YOUR CODE HERE ***"
        if pred(y):
            return combiner(x,y)
        else:
            return x

    return accumulate(combine_if, base, n, term)


def odd(x):
    return x % 2 == 1

def greater_than_5(x):
    return x > 5

# Q4. 
def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    def counter_helper(last_digit, number):
        if number < 10 and number + last_digit == 10:
            return 1
        elif number < 10 and number + last_digit != 10:
            return 0
        elif number > 10:
            return counter_helper(last_digit, number % 10) + counter_helper(last_digit, number // 10)

    def helper(digit):
        if digit < 10:
            return 0
        else:
            return counter_helper(digit % 10, digit // 10) + helper(digit//10)

    return helper(n)


def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    
    def max_exponent(quantity, exponent):
        if 2 ** exponent == quantity:
            return exponent
        elif 2 ** exponent > quantity:
            return exponent - 1
        else:
            return max_exponent(quantity, exponent + 1)

    def help_breaker(quantity, exponent):
        if exponent == 0:
            return 1
        elif quantity == 0:
            return 1
        elif quantity < 0:
            return 0
        else:
            return help_breaker(quantity, exponent - 1) + help_breaker(quantity-2 **exponent,exponent) 

    return help_breaker(amount, max_exponent(amount, 1))
    

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120

    >>> fact = lambda n: 1 if n == 1 else mul(n, fact(sub(n, 1)))
    >>> fact(5)
    120
    """
    return lambda n: (lambda f, v: f(f,v))(lambda f, v: 1 if v == 1 else mul(v, f(f, sub(v,1))),n)

print(make_anonymous_factorial()(5))