def solve():
	nums = int(input())
	strings = [x for x in str(input())]

	a = 0
	d = 0

	for x in strings:
		if x == "A":
			a += 1
		elif x == "D":
			d += 1

	if a > d:
		print("Anton")
	elif a < d:
		print("Danik")
	else:
		print("Friendship")

solve()
