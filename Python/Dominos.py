def solve():
	inputs = list(map(int, input().split()))

	dom_area = 2*1
	box_area = inputs[0] * inputs[1]

	print(int(box_area / dom_area))

solve()