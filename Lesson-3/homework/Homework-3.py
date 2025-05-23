fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("1) Third fruit:", fruits[2], "\n")


# 2
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated = list1 + list2
print("2) Concatenated list:", concatenated, "\n")

#3
numbers = [10, 20, 30, 40, 50]
first = numbers[0]
middle = numbers[len(numbers)//2]
last = numbers[-1]
extracted = [first, middle, last]
print("3) First, middle, last:", extracted, "\n")




#4
movies_list = ["Inception", "The Matrix", "Interstellar", "The Godfather", "Pulp Fiction"]
movies_tuple = tuple(movies_list)
print("4) Movies tuple:", movies_tuple, "\n")

#5
cities = ["New York", "London", "Paris", "Tokyo", "Sydney"]
has_paris = "Paris" in cities
print("5) Is 'Paris' in cities?:", has_paris, "\n")

# 6
nums = [7, 8, 9]
duplicated = nums * 2
print("6) Duplicated list:", duplicated, "\n")



# 7
swap_list = [100, 200, 300, 400]
swap_list[0], swap_list[-1] = swap_list[-1], swap_list[0]
print("7) After swap first and last:", swap_list, "\n")

# 8
t = tuple(range(1, 11))  # (1,2,...,10)
slice_3_to_7 = t[3:8]     # indices 3,4,5,6,7
print("8) Slice from index 3 to 7:", slice_3_to_7, "\n")

# 9
colors = ["red", "blue", "green", "blue", "yellow", "blue"]
count_blue = colors.count("blue")
print("9) 'blue' appears:", count_blue, "times\n")

# 10
animals = ("cat", "dog", "lion", "tiger")
index_lion = animals.index("lion")
print("10) Index of 'lion':", index_lion, "\n")

# 11
t1 = (1, 2, 3)
t2 = (4, 5, 6)
merged = t1 + t2
print("11) Merged tuple:", merged, "\n")

# 12
sample_list = [10, 20, 30]
sample_tuple = (40, 50, 60, 70)
print("12) Length of list:", len(sample_list))
print("    Length of tuple:", len(sample_tuple), "\n")

# 13
nums_tuple = (5, 10, 15, 20, 25)
nums_list = list(nums_tuple)
print("13) Converted list:", nums_list, "\n")

#14
values = (3, 1, 4, 1, 5, 9, 2)
print("14) Max value:", max(values))
print("    Min value:", min(values), "\n")

#15
words = ("hello", "world", "python", "code")
reversed_words = words[::-1]
print("15) Reversed tuple:", reversed_words)
