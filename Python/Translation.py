def solve():
	wrds1 = str(input())
	wrds2 = str(input())

	if wrds1[::-1] == wrds2:
		print("YES")
	elif wrds1 == wrds2[::-1]:
		print("YES")
	else:
		print("NO")

solve()
