def count_matches(n,m):
	counter = 0
	while n >= 10 and m >=10:
		if n % 10 == m % 10:
			counter += 1
		n = n // 10
		m = m // 10
	if n < 10 or m < 10:
		if n == m % 10 or m == n % 10:
			counter += 1
	return counter

print(count_matches(101, 10))
