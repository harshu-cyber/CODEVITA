def move_direction(facing, turn):
    # facing: 0=north,1=east,2=south,3=west
    if turn == "straight":
        return facing
    if turn == "left":
        return (facing + 1) % 4
    if turn == "right":
        return (facing + 3) % 4
    if turn == "back":
        return (facing + 2) % 4

def simulate(instructions, replace_idx=None, new_turn=None, start=(0,0)):
    x, y = start
    facing = 0  # north
    for idx, (turn, dist) in enumerate(instructions):
        if replace_idx == idx:  # substitute wrong turn
            turn = new_turn
        facing = move_direction(facing, turn)
        if facing == 0:  # north
            y += dist
        elif facing == 1:  # east
            x += dist
        elif facing == 2:  # south
            y -= dist
        else:  # west
            x -= dist
    return (x, y)

def solve():
    N = int(input().strip())
    instructions = []
    for _ in range(N):
        t, d = input().split()
        instructions.append((t, int(d)))
    x0, y0 = map(int, input().split())
    xt, yt = map(int, input().split())

    turns = ["left", "right", "straight", "back"]

    for i in range(N):
        wrong_turn, dist = instructions[i]
        for new_turn in turns:
            if new_turn == wrong_turn:
                continue
            final_pos = simulate(instructions, replace_idx=i, new_turn=new_turn, start=(x0,y0))
            if final_pos == (xt, yt):
                print("Yes")
                print(f"{wrong_turn} {dist}")
                print(f"{new_turn} {dist}")
                return
    print("No")
