HW_SOURCE_FILE = 'hw04.py'

###############
#  Questions  #
###############

def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    "*** YOUR CODE HERE ***"
    strt1, ave1 = street(a), avenue(a)
    strt2, ave2 = street(b), avenue(b)
    return abs(strt1 - strt2) + abs(ave1 - ave2)

def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    "*** YOUR CODE HERE ***"
    out = []
    for elt in s:
    	if round(elt ** (0.5)) - elt ** (0.5) == 0:
    		out = out + [round(elt ** (0.5))]
    return out
    #return [int(sqrt(i)) for i in s if round(i ** (0.5)) - i ** (0.5) == 0]

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
    	return n
    else:
    	return g(n-1) + 2 * g(n-2) + 3 * g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 1 or n ==2 or n == 3:
    	return n
    else:
    	i = 3
    	curr, prev_val, prev_prev_val = 3, 2, 1
    	total = 0
    	while i < n:
    		total = curr  + 2 * prev_val + 3 * prev_prev_val
    		curr, prev_val, prev_prev_val = total, curr, prev_val
    		i += 1

    	return total

    return total

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
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"

    def max_exponent(amount, n):
    	if 2 ** n >= amount:
    		return n
    	else:
    		return max_exponent(amount, n+1)
    	#n = 0
    	#while 2 ** (n+1) <= amount:
    	#	n += 1
    	#return n

    def change_counter(amount, max_exp):
    	if amount < 0 or max_exp < 0:
    		return 0
    	elif amount == 0 or amount == 1 or max_exp == 0:
    		return 1
    	else:
    		return change_counter(amount - 2 ** max_exp, max_exp) + change_counter(amount, max_exp - 1)
    
    return change_counter(amount, max_exponent(amount,0))

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"

    def remaining(start,end):
    	return 6 - start - end

    def helper(n, start, end):
    	if n == 1:
    		print_move(start, end)
    	else:
    		move_stack(n-1, start, remaining(start, end))
    		print_move(start, end)
    		move_stack(n-1, remaining(start,end), end)
    return helper(n, start, end)


###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return lambda n: (lambda f,v: f(f, v))(lambda f, v: 1 if v == 1 else mul(v, f(f, sub(v,1))), n)