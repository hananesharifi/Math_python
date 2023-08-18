def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        result = fib(n - 1, memo) + fib(n - 2, memo)
        memo[n] = result
        return result
n = eval(input())
list1 = []
for i in range(1 ,n):
    f = fib(i)
    list1.append(f)
for i in range(1 , n + 1):
    if i in list1:
        print('+',end='')
    else:
        print('-',end='')
if n == 0:
    print('-',end='')