import sys

while True:
    a = sys.stdin.readline()
    if not a:
        break
    a = a.strip()

    b = sys.stdin.readline()
    if not b:
        break
    b = b.strip()

    result = ""

    for ch in "abcdefghijklmnopqrstuvwxyz":
        count_a = 0
        for x in a:
            if x == ch:
                count_a += 1

        count_b = 0
        for x in b:
            if x == ch:
                count_b += 1

        small = count_a if count_a < count_b else count_b
        result += ch * small

    print(result)