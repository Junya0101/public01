import time

a = 200

def fibo(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)

a = a + a * 100
print(a)

print(a * 3)

print("ばーか")

t0 = time.time()

# print(fibo(30))
# print(fibo(33))
print(fibo(34))
# print(fibo(40))

print(time.time() - t0, "秒かかった")