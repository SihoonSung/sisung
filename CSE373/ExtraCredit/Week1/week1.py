import sys

def collatz(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    return length

for line in sys.stdin:
    i, j = map(int, line.split())
    
    start = min(i, j)
    end = max(i, j)
    max_len = 0

    for num in range(start, end + 1):
        cur = collatz(num)
        if cur > max_len:
            max_len = cur

    print(i, j, max_len)