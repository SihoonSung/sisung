import sys

for line in sys.stdin:
    data = list(map(int, line.split()))
    n = data[0]
    nums = data[1:]

    if n == 1:
        print("Jolly")
        continue

    differences = []
    for i in range(n - 1):
        diff = abs(nums[i] - nums[i + 1])
        differences.append(diff)
    needed = set(range(1, n))

    if set(differences) == needed:
        print("Jolly")
    else:
        print("Not jolly")