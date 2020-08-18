def solve():
	len_wrds = int(input())
	new_wrds = []
	
	for x in range(len_wrds):
		wrds = str(input())
		if len(wrds) > 10:
			new_wrds.append(wrds[0] + str(len(wrds)-2) + wrds[-1])
		else:
			new_wrds.append(wrds)

	for x in new_wrds:
		print(x)

solve()
