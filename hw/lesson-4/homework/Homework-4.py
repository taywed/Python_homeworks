sample_dict = { 'a': 3, 'b': 1, 'c': 2 }
asc_items = sorted(sample_dict.items(), key=lambda item: item[1])
asc_dict = {k: v for k, v in asc_items}
print("1a) Ascending by value:", asc_dict)
desc_items = sorted(sample_dict.items(), key=lambda item: item[1], reverse=True)
desc_dict = {k: v for k, v in desc_items}
print("1b) Descending by value:", desc_dict, "\n")

#
d = {0: 10, 1: 20}
d[2] = 30
print("2) After adding key:", d, "\n")

#
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
concatenated = {}
for dct in (dic1, dic2, dic3):
    for k, v in dct.items():
        concatenated[k] = v
print("3) Concatenated dict:", concatenated, "\n")

#1 ton
n = int(input("Enter n for squares dict (e.g. 5): "))
squares = {}
for x in range(1, n + 1):
    squares[x] = x * x
print("4) Squares dict 1 to", n, ":", squares, "\n")

#1 to 15
squares_15 = {}
for x in range(1, 16):
    squares_15[x] = x * x
print("5) Squares dict 1 to 15:", squares_15, "\n")

#
my_set = {1, 2, 3, 4}
print("Set created:", my_set)

#
print("Iterating over set:")
for elem in my_set:
    print(elem)
print()

#
my_set.add(5)
my_set.update([6, 7])
print("After adding members:", my_set)

#
if 2 in my_set:
    my_set.remove(2)
print("After removing 2:", my_set)

#
my_set.discard(10)
print("After discarding 10 (no error if absent):", my_set)
