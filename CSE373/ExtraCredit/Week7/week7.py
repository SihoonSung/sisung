import sys

while True:
    line = sys.stdin.readline()
    if not line:
        break

    m, n = map(int, line.split())

    grid = []
    for _ in range(m):
        grid.append(list(map(int, sys.stdin.readline().split())))

    dp = [[0]*n for _ in range(m)]
    parent = [[-1]*n for _ in range(m)]

    for r in range(m):
        dp[r][n-1] = grid[r][n-1]

    for c in range(n-2, -1, -1):
        for r in range(m):
            next_rows = [
                (r-1) % m,
                r,
                (r+1) % m
            ]
            next_rows.sort() 

            best_row = next_rows[0]
            best_cost = dp[best_row][c+1]

            for nr in next_rows:
                if dp[nr][c+1] < best_cost:
                    best_cost = dp[nr][c+1]
                    best_row = nr

            dp[r][c] = grid[r][c] + best_cost
            parent[r][c] = best_row

    start = 0
    for r in range(1, m):
        if dp[r][0] < dp[start][0]:
            start = r

    path = [start]
    cur = start
    for c in range(n-1):
        cur = parent[cur][c]
        path.append(cur)

    print(" ".join(str(r+1) for r in path))
    print(dp[start][0])