import time

def fibo(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)

def fibo2(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    x1 = 1
    x2 = 1
    tmp = 0
    for i in range(1, n):
        tmp = x1 + x2
        x1 = x2
        x2 = tmp
    return x2

t0 = time.time()

n = 100

# print(fibo(n))
print(fibo2(n))

print(time.time() - t0, "秒かかった")