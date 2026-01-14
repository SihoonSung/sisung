import sys

def solve_case(weights):
    n = len(weights)
    total = sum(weights)

    k1 = n // 2
    k2 = n - k1  
    max_sum = total
    dp = [set() for _ in range(k2 + 1)]
    dp[0].add(0)
    for w in weights:
        for c in range(k2, 0, -1):
            for s in dp[c-1]:
                dp[c].add(s + w)
    best = None
    for c in (k1, k2):
        for s in dp[c]:
            if best is None or abs(total - 2*s) < abs(total - 2*best):
                best = s
    team1 = best
    team2 = total - best

    return min(team1, team2), max(team1, team2)


t = int(sys.stdin.readline().strip())
sys.stdin.readline() 

for case in range(t):
    n = int(sys.stdin.readline().strip())
    weights = []
    for _ in range(n):
        weights.append(int(sys.stdin.readline().strip()))
    a, b = solve_case(weights)
    print(a, b)

    if case != t - 1:
        print()
        