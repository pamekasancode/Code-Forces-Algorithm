def solve():
	problem = int(input())
	i = 0
	for _ in range(problem):
		condition = list(map(int, input().split()))
		if sum(condition) >= 2:
			i += 1
		
	print(i)

solve()