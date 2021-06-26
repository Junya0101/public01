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
for i in range(10):
    print(fibo(i))
