import math
B = 10
def e_th_root(e, n):
    len = math.floor(math.log(n, B)) + 1
    k = math.floor((len - 1) / e)
    m = B ** k
    digit = 1
    while digit < B and (m + B ** k)  ** e  <= n:
        m += B ** k
        digit += 1

    print(f"n={n}  len = {len}  k={k} m={m}")

    for i in range(k - 1, -1, -1):
        digit = 0
        while digit < B and (m + B ** i) ** e <= n:
            m += B ** i
            digit += 1
    print( f"m={m}")
    return m

e_th_root(2, 200)
e_th_root(2, 500)
e_th_root(2, 1500)
e_th_root(2, 78)
e_th_root(2, 9)
e_th_root(2, 26000)
e_th_root(2, 50000)

print("cube roots")
e_th_root(3, 30)
e_th_root(3, 27)
e_th_root(3, 130)
e_th_root(3, 10)
e_th_root(3, 8000)
e_th_root(3, 10000)