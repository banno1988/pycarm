k = int(input())
s = input()
n = 0
t = 0
p = 0
o = 1
for i in s:
    t += 1
    l = s[t:]
    # print(l)
    for j in range(len(l)):
        print('p',p,'o',o)
        if l[j] != i and o == 1 and p < k:
            p += 1
        elif (j + 1) != len(l) and l[j] != i and p == k:
            break
        elif l[j] == i and o >= 1:
            o += 1
        elif l[j] != i and o > 1 and p < k:
            p += 1

    #print('p', p, 'o', o)
    # print(p)
    if o + p > n:
        n = p + o
    p = 0
    o = 1
print(n)
