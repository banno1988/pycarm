n = int(input())
k = int(input())
parta = int(input())
mesto = int(input())

mestopete = (parta - 1) * 2 + mesto
variantpete = mestopete % k
if variantpete == 0:
    variantpete = k
skolvar = n // k
ostatok = n % k

if ostatok >= variantpete:
    skolvar += 1
#print(skolvar,'skolvar')
if ((mestopete + k))% 2 == 0:
    a = 2
else:
    a = 1
if ((mestopete - k)) % 2 == 0:
    b = 2
else:
    b = 1
#print(((mestopete + k) +1)//2)
#print(((mestopete - k) +1)//2)
if skolvar == 1:
    print(-1)
if skolvar == 2:
    if mestopete + k <= n:
        print(((mestopete + k) +1)// 2, a)
    else:
        print(((mestopete - k) +1)// 2, b)
if skolvar >= 3:
    if mestopete + k <= n:
        if ((mestopete + k) +1)// 2 - parta <= parta - ((mestopete - k) +1)// 2:
            print(((mestopete + k) +1)// 2, a)
        elif ((mestopete + k) +1)// 2 - parta > parta - ((mestopete - k) +1)// 2:
            print(((mestopete - k) +1) // 2, b)
    else:
        print(((mestopete - k) + 1) // 2, b)
