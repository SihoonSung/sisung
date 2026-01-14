import sys

t = int(sys.stdin.readline().strip())

for case in range(1, t + 1):
    sys.stdin.readline() 

    n = int(sys.stdin.readline().strip())

    jobs = []
    for i in range(1, n + 1):
        T, S = map(int, sys.stdin.readline().split())
        jobs.append((T, S, i)) 

    jobs.sort(key=lambda x: (x[0] / x[1], x[2]))
    order = [str(job[2]) for job in jobs]
    print(" ".join(order))

    if case != t:
        print()
