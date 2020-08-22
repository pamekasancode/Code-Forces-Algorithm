def solve():
	wrds = str(input())

	up = 0
	low = 0
	for x in wrds:
		if x.isupper():
			up += 1
		elif x.islower():
			low += 1

	if up > low:
		print(wrds.upper())
	else:
		print(wrds.lower())

solve()
