k = int(input())
s = input()

start = 0
d = {}
maxstring = 0
dlinastroki = 0
for end in range(len(s)):
    d[s[end]] = d.get(s[end], 0) + 1
    maxstring = max(maxstring, d[s[end]])
    v = (end + 1 - start - maxstring <= k)
    if not v:
        d[s[start]] -= 1
        start += 1
    dlinastroki = end + 1 - start

print(dlinastroki)
