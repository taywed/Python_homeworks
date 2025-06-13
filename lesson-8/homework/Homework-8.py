#
try:
    x = float(input("Enter numerator: "))
    y = float(input("Enter denominator: "))
    print("Result =", x / y)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

#
s = input("Enter an integer: ")
try:
    n = int(s)
    print("You entered integer:", n)
except ValueError:
    print("Error: That is not a valid integer.")

# 
fname = input("Enter filename to open: ")
try:
    f = open(fname, 'r')
    print(f.read())
    f.close()
except FileNotFoundError:
    print("Error: File not found:", fname)

# 
a, b = input("Enter two numbers separated by space: ").split()
try:
    a = float(a); b = float(b)
    print("Sum =", a + b)
except ValueError:
    print("Error: Both inputs must be numbers.")

#
fname = input("Enter filename to open for writing: ")
try:
    f = open(fname, 'w')
    f.write("Test\n")
    f.close()
except PermissionError:
    print("Error: No permission to write to", fname)

# 
lst = [10, 20, 30]
idx = int(input("Enter index to access (0–2): "))
try:
    print("Element:", lst[idx])
except IndexError:
    print("Error: Index out of range.")

# 
try:
    x = input("Enter a number (Ctrl+C to cancel): ")
    print("You entered:", x)
except KeyboardInterrupt:
    print("\nInput cancelled by user.")

#
try:
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    result = x // y
    print("Integer division result:", result)
except ArithmeticError as e:
    print("Arithmetic error:", e)

# 
fname = input("Enter text filename: ")
try:
    with open(fname, encoding='utf-8') as f:
        print(f.read())
except UnicodeDecodeError:
    print("Error: Cannot decode file contents as UTF-8.")

#
lst = [1, 2, 3]
try:
    print(lst.nonexistent_method())
except AttributeError:
    print("Error: That attribute does not exist on list.")

# 2

filename = "sample.txt"

#
with open(filename, 'r') as f:
    all_text = f.read()
print("Entire file contents:\n", all_text)

#
n = int(input("How many first lines to read? "))
with open(filename, 'r') as f:
    for i in range(n):
        line = f.readline()
        if not line:
            break
        print(line, end='')

# 
append_text = input("\nEnter text to append: ")
with open(filename, 'a') as f:
    f.write(append_text + "\n")
print("After append:")
with open(filename, 'r') as f:
    print(f.read())

#
n = int(input("How many last lines to read? "))
with open(filename, 'r') as f:
    lines = f.readlines()
print("".join(lines[-n:]))

# 
with open(filename, 'r') as f:
    lines_list = f.readlines()
print("Lines list:", lines_list)

#
text_var = ""
with open(filename, 'r') as f:
    for line in f:
        text_var += line
print("Aggregated text:", text_var)

#
with open(filename, 'r') as f:
    arr = [line.rstrip('\n') for line in f]
print("Array of lines:", arr)

#
with open(filename, 'r') as f:
    words = f.read().split()
longest = max(words, key=len)
print("Longest word:", longest)

#
with open(filename, 'r') as f:
    count = sum(1 for _ in f)
print("Number of lines:", count)

# 
from collections import Counter
with open(filename, 'r') as f:
    freq = Counter(f.read().split())
print("Word frequencies:", freq)

#
import os
size = os.path.getsize(filename)
print("File size (bytes):", size)

# 
lst = ['apple', 'banana', 'cherry']
with open("fruits.txt", 'w') as f:
    for item in lst:
        f.write(item + "\n")

# 
with open(filename, 'r') as fr, open("copy.txt", 'w') as fw:
    fw.write(fr.read())

# 
with open("file1.txt", 'r') as f1, open("file2.txt", 'r') as f2:
    for l1, l2 in zip(f1, f2):
        print(l1.rstrip('\n') + " | " + l2.rstrip('\n'))

# 
import random
with open(filename, 'r') as f:
    lines = f.readlines()
print("Random line:", random.choice(lines).rstrip('\n'))

# 
f = open(filename, 'r')
print("Is closed before closing?", f.closed)
f.close()
print("Is closed after closing?", f.closed)

# 
with open(filename, 'r') as f:
    data = f.read().replace('\n', '')
print("Without newlines:", data)

# 
with open(filename, 'r') as f:
    text = f.read().replace(',', ' ')
    words = text.split()
print("Word count:", len(words))

# 
with open(filename, 'r') as f:
    chars = list(f.read())
print("Characters list:", chars)

# 
import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", 'w') as f:
        f.write(letter + "\n")

# 
N = int(input("Letters per line: "))
alphabet = string.ascii_uppercase
with open("alphabet_lines.txt", 'w') as f:
    for i in range(0, len(alphabet), N):
        f.write(alphabet[i:i+N] + "\n")
