import sys

t = int(sys.stdin.readline())

for _ in range(t):
    parts = sys.stdin.readline().split()
    r = int(parts[0])   
    streets = []

    for i in range(1, r + 1):
        streets.append(int(parts[i]))

    streets.sort()
    median = streets[r // 2]

    total_distance = 0
    for s in streets:
        if s >= median:
            total_distance += s - median
        else:
            total_distance += median - s

    print(total_distance)