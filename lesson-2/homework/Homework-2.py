name = input("Enter your name: ")
birth_year = int(input("Enter your year of birth (e.g. 1990): "))
current_year = int(input("Enter the current year (e.g. 2025): "))
age = current_year - birth_year
print(name + ", you are " + str(age) + " years old.\n")





txt = 'LMaasleitbtui'
cars = []
current = ''
for ch in txt:
    if ch.isupper():
        if current != '':
            cars.append(current)
        current = ch
    else:
        current += ch
if current:
    cars.append(current)
print("Extracted car names from txt1:", cars, "\n")




txt = 'MsaatmiazD'
cars = []
current = ''
for ch in txt:
    if ch.isupper():
        if current != '':
            cars.append(current)
        current = ch
    else:
        current += ch
if current:
    cars.append(current)
print("Extracted car names from txt2:", cars, "\n")



txt = "I'am John. I am from London"
area = ''
marker = "from "
pos = txt.find(marker)
if pos != -1:
    area = txt[pos + len(marker):]
print("Residence area:", area, "\n")


s = input("Enter a string to reverse: ")
rev = ''
for ch in s:
    rev = ch + rev
print("Reversed string:", rev, "\n")


s = input("Enter a string: ")
count = 0
for ch in s.lower():
    if ch in 'aeiou':
        count += 1
print("Number of vowels:", count, "\n")


lst = input("Enter a list of numbers separated by spaces: ").split()
max_val = None
for x in lst:
    num = float(x)
    if max_val is None or num > max_val:
        max_val = num
print("Maximum value:", max_val, "\n")


word = input("Enter a word: ").lower()
is_pal = True
for i in range(len(word)//2):
    if word[i] != word[-1-i]:
        is_pal = False
        break
if is_pal:
    print("'" + word + "' is a palindrome.\n")
else:
    print("'" + word + "' is not a palindrome.\n")


email = input("Enter your email address: ")
domain = ''
if '@' in email:
    domain = email[email.find('@')+1:]
print("Email domain:", domain, "\n")


length = int(input("Enter desired password length: "))
seed = int(input("Enter a numeric seed for password generation: "))
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
password = ''
for _ in range(length):
    seed = (seed * 9301 + 49297) % 233280
    idx = seed % len(chars)
    password += chars[idx]
print("Generated password:", password)
