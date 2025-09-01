import math

def distance(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def orientation(o, a, b):
    # cross product
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def fruit_bowl(points):
    points = sorted(points) 
    

    lower = []
    for p in points:
        while len(lower) >= 2 and orientation(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
   
    perimeter = 0
    for i in range(len(lower)-1):
        perimeter += distance(lower[i], lower[i+1])
    
    return round(perimeter)


N = int(input().strip())
points = [tuple(map(int, input().split())) for _ in range(N)]

print(fruit_bowl(points))
