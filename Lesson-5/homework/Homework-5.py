#1
def is_leap(year):
    """Determines whether a given year is a leap year."""
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = int(input("Enter a year to check for leap year: "))
print(f"{year} is", "a leap year." if is_leap(year) else "not a leap year.")
print()

# 2
n = int(input("Enter a positive integer n (1–100): "))
if n % 2 == 1:
    print("Weird")
else:
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:  # n > 20
        print("Not Weird")
print()

#3

a = int(input("Enter integer a: "))
b = int(input("Enter integer b: "))

# 4
if a % 2 == 0:
    start = a
else:
    start = a + 1
evens_with_if = list(range(start, b + 1, 2))
print("Even numbers between a and b (using if-else):", evens_with_if)

#5
start2 = a + (a % 2)
evens_no_if = list(range(start2, b + 1, 2))
print("Even numbers between a and b (no if-else):", evens_no_if)
