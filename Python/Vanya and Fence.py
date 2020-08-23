def solve():
	inputs = list(map(int, input().split()))
	friends = inputs[0]
	h_fence = inputs[1]
	i = 0

	person_h = list(map(int, input().split()))
	for x in person_h:
		if x <= h_fence:
			i += 1
		else:
			i += 2

	print(i)	
solve()	
