n_str ,k_str = input().split()
n = int(n_str)
k = int(k_str)

def combination(n ,k):
    if k == 0 or n ==k:
        return 1
    elif k > n:
        return 0
    else:
        return combination(n - 1 ,k -1) +combination(n - 1 ,k)
c = combination(n ,k)
print(c)
