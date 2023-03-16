k = int(input())
t = k
s = input()
n = len(s)
max_beauty = 1
sets1 = set(s)
for a in sets1:
    #print(a)
    for l in range(n):
        r = l
        while r < n:
            #print(r,k)
            if s[r] == a:
                r += 1
            else:
                k -= 1
                r += 1
            if k < 0:
                r-=1
                break
        k = t
        cur_beauty = r - l

        #print('#',max_beauty, cur_beauty)
        max_beauty = max(max_beauty, cur_beauty)
print(max_beauty)
