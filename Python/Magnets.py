def solve():
	many = int(input())
	group = 1
	polar1 = 0
	polar2 = 0
	i = 0

	for _ in range(many):
		magnets = list(map(int, input()))
		if i == 0:
			polar1 = magnets[1]
		else:
			polar2 = magnets[0]
			if polar2 == polar1:
				group += 1
			polar1 = magnets[1]
			i = 0
		i += 1

	print(group)

solve()






