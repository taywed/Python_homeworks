#1
txt = input("Enter a string: ")
vowels = "aeiouAEIOU"
out = ""
count = 0
length = len(txt)
for i, ch in enumerate(txt):
    out += ch
    count += 1
    if count == 3 and i < length - 2:
        out += "_"
        count = 0
print("Modified string:", out, "\n")


#2
n = int(input("Enter n for squares (0 ≤ i < n): "))
i = 0
while i < n:
    print(i * i)
    i += 1
print()


#1
print("1–10 natural numbers:")
i = 1
while i <= 10:
    print(i)
    i += 1
print()

#2
print("Number pattern:")
for row in range(1, 6):
    for num in range(1, row + 1):
        print(num, end=" ")
    print()
print()

# 3
m = int(input("Enter number to sum to: "))
total = 0
i = 1
while i <= m:
    total += i
    i += 1
print("Sum is:", total, "\n")

#4
t = int(input("Enter number for multiplication table: "))
i = 1
while i <= 10:
    print(t * i)
    i += 1
print()

#5
numbers = [12, 75, 150, 180, 145, 525, 50]
print("Filtered output:")
for x in numbers:
    if x > 50 and x % 10 != 0:
        print(x)
print()

#6
num = input("Enter a number to count digits: ")
print("Number of digits:", len(num), "\n")

#
print("Reverse number pattern:")
for start in range(5, 0, -1):
    for num in range(start, 0, -1):
        print(num, end=" ")
    print()
print()

# 8
list1 = [10, 20, 30, 40, 50]
print("List in reverse:")
for i in range(len(list1) - 1, -1, -1):
    print(list1[i])
print()

#9
print("Negative one to ten:")
for x in range(-10, 0):
    print(x)
print()

# 10
for x in range(5):
    print(x)
print("Done!\n")

#11
print("Primes between 25 and 50:")
for num in range(25, 51):
    is_prime = True
    if num < 2:
        is_prime = False
    else:
        div = 2
        while div * div <= num:
            if num % div == 0:
                is_prime = False
                break
            div += 1
    if is_prime:
        print(num)
print()

#12
print("Fibonacci sequence (10 terms):")
a, b = 0, 1
count = 0
while count < 10:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
print("\n")

#13
f = int(input("Enter number to factorial: "))
fact = 1
i = 1
while i <= f:
    fact *= i
    i += 1
print(f"{f}! =", fact, "\n")


#4
lst1 = input("Enter list1 elements separated by spaces: ").split()
lst2 = input("Enter list2 elements separated by spaces: ").split()

for idx in range(len(lst1)):
    lst1[idx] = int(lst1[idx])
for idx in range(len(lst2)):
    lst2[idx] = int(lst2[idx])

result = []
for x in lst1:
    if x not in lst2:
        result.append(x)
for x in lst2:
    if x not in lst1:
        result.append(x)

print("Uncommon elements:", result)


txt = input("Enter string:")
out = ""
for i, ch in enumerate(txt):
    out += ch
    if (i + 1) % 3 == 0 and i != len(txt) - 1:
        out += "_"
print(out)




