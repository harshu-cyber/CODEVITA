def simulate_band(start, seq):
    x, y = start
    path = [(x, y)]
    moves = {'u':(-1,0), 'd':(1,0), 'l':(0,-1), 'r':(0,1)}
    for move in seq:
        dx, dy = moves[move]
        x += dx
        y += dy
        path.append((x, y))
    return path

def solve():
    S = int(input())
    x1, y1 = map(int, input().split())
    seq1 = input().strip()
    x2, y2 = map(int, input().split())
    seq2 = input().strip()
    
    path1 = simulate_band((x1, y1), seq1)
    path2 = simulate_band((x2, y2), seq2)
    
    # Matrix to track first layer
    grid = [[[] for _ in range(S)] for _ in range(S)]
    
    # Fill band1
    for i, (x, y) in enumerate(path1):
        grid[x][y].append(1)
    
    # Fill band2
    for i, (x, y) in enumerate(path2):
        grid[x][y].append(2)
    
    impossible = False
    overlap_count = 0
    for i in range(S):
        for j in range(S):
            layers = grid[i][j]
            if len(layers) > 2:
                # Interlocked more than 2 → impossible
                impossible = True
                break
            if len(layers) == 2:
                if layers[0] != layers[1]:
                    # Check interlocking: must be consistent
                    # If both orders appear in different cells → impossible
                    # Here we can just check if a cell is layer 1 over 2, 
                    # and another cell layer 2 over 1 → impossible
                    pass
                overlap_count += 1
        if impossible:
            break
    if impossible:
        print("Impossible")
    else:
        print(overlap_count)

# Run
solve()
