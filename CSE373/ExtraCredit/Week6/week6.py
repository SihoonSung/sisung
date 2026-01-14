import sys

elephants = []
idx = 1
for line in sys.stdin:
    w, iq = map(int, line.split())
    elephants.append((w, iq, idx))
    idx += 1

elephants.sort(key=lambda x: (x[0], -x[1]))

n = len(elephants)

dp = [1] * n        
parent = [-1] * n   

for i in range(n):
    for j in range(i):
        if elephants[j][0] < elephants[i][0] and elephants[j][1] > elephants[i][1]:
            if dp[j] + 1 >= dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j

max_len = max(dp)
end = dp.index(max_len)

sequence = []
while end != -1:
    sequence.append(elephants[end][2])  
    end = parent[end]
sequence.reverse()

print(max_len)
for x in sequence:
    print(x)