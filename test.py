def print_numbers(n,k):
	def inner(n,s):
		if n == 0:
			if s % k  == 0 and s > k:
				print(s)
		else:
			inner(n//10, s)
			inner(n//10, s*10 + n % 10)
	inner(n,0)

#print(print_numbers(97531, 5))
#print(print_numbers(97531, 7))
print(print_numbers(97531, 2))