def solve():
	nums = str(input())
	seq = [int(x) for x in nums if x == "4" or x == "7"]
	if len(seq) == 7 or len(seq) == 4:
		print("YES")
	else:
		print("NO")

solve()
