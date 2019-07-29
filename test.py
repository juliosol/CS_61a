def make_direction(secret):
	def guess_compare(guess):
		if guess < secret:
			return 1
		elif guess > secret:
			return -1
		return 0
	return guess_compare

def naive_search(low, high, direction):
	guess, count = (low + high)//2, 1
	print(guess)
	sign = direction(guess)
	while sign != 0:
		guess = guess + sign
		count = count + 1
		sign = direction(guess)
		print(guess)
	return count

def binary_search(low, high, direction):
	guess = (low + high)//2
	print(guess)
	sign = direction(guess)
	if sign == 0:
		return 1
	elif sign < 0:
		return 1 + binary_search(low, guess, direction)
	else:
		return 1 + binary_search(guess, high, direction)

def sum_some(n,p):
	total = 0
	while n > 0:
		if p(n%10):
			total += (n % 10)
		n = n // 10
	return total

even = lambda d: d%2 == 0
big = lambda d: d > 5

def sum_largest(n,k):
	if k == 0 or n == 0:
		return 0
	a = sum_largest(n//10, k)
	b = sum_largest(n, k-1)
	return max(a,b)

def cascade(n):
	if n < 10:
		print(n)
	else:
		print(n)
		cascade(n // 10)
		print(n)

def inv_cascade(n):
	def grow(n):
		if n < 10:
			return None
		else:
			grow(n//10)
			print(n//10)
	
	def shrink(n):
		if n < 10:
			return None
		else:
			print(n//10)
			shrink(n//10)

	grow(n)
	print(n)
	shrink(n)

def inverse_cascade(n):
	grow(n)
	print(n)
	shrink(n)

def f_then_g(f,g,n):
	if n:
		f(n)
		g(n)

grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)

def count_partitions(n,m):
	if n == 0:
		return 1
	elif n < 0:
		return 0
	elif m == 0:
		return 0
	else:
		return count_partitions(n-m, m) + count_partitions(n,m-1)

def is_prime(n):
	def prime_helper(index):
		if index == n:
			return True
		elif n % index == 0 or n == 1:
			return False
		else:
			return prime_helper(index + 1)
	return prime_helper(2)

def make_func_repeater(f,x):
	def repeat(n):
		if n == 0:
			return x
		else:
			return f(repeat(n-1))
	return repeat

def pascal(row, column):
	if column == 0:
		return 1
	elif column == row:
		return 1
	return pascal(row-1, column) + pascal(row-1, column - 1)
