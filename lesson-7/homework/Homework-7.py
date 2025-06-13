def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# 1
n = int(input())
print(is_prime(n))

def digit_sum(k):
    s = 0
    while k > 0:
        s += k % 10
        k //= 10
    return s

# 2
k = int(input())
print(digit_sum(k))

# 3
N = int(input())
p = 2
first = True
while p <= N:
    if not first:
        print(" ", end="")
    print(p, end="")
    first = False
    p *= 2
print()
