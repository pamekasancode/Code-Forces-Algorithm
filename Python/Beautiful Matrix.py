def solve():
    matrix = [input().split() for _ in range(5)]
    matrix = [list(map(int, x)) for x in matrix]
    midle_point = 2

    for x in range(len(matrix)):
        i = 0
        for y in matrix[x]:
            if y == 1:
                col = x
                row = i
                break
            i += 1

    moves = 0
    while True:
        while True:
            if row > midle_point:
                row -= 1
                moves += 1
            elif row < midle_point:
                row += 1
                moves += 1
            else:
                break

        if col > midle_point:
            col -= 1
            moves += 1
        elif col < midle_point:
            col += 1
            moves += 1
        else:
            break
    print(moves)
    
solve()
