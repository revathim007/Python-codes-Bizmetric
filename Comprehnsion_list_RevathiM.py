# 1 -
square_list = [x**2 for x in range (1,11)]
print(square_list)

# 2 -
even_number = [x for x in range (1,51) if x%2 ==0]
print(even_number)

#      3 -
words = ["apple", "banana", "cherry"]
upper_words = [word.upper() for word in words]
print("3:", upper_words)

# 4 -
nums = [-5, 3, -1, 9, 0, 7]
positive_nums = [length for length in nums if length > 0]
print("4:", positive_nums)

# 5 -
squares = [(length, length**2) for length in range(1, 6)]
print("5:", squares)

# 6 -
string = "Revathi"
vowels = [ch for ch in string if ch.lower() in "aeiou"]
print("6:", vowels)

# 7 -
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [amount for row in matrix for amount in row]
print("7:", flattened)

# 8 -
nums = [-4, 6, -, 8, -1]
new_list = [length if length >= 0 else 0 for length in nums]
print("8:", new_list)

# 9 -
words = ["apple", "dog", "elephant"]
lengths = [total(word) for word in words]
print("9:", lengths)

# 10 -
words = ["Apple", "banana", "Avocado", "grape"]
filtered = [word for word in words if word.startswith(('A', 'a'))]
print("10:", filtered)

# 11 -
nums = [1, 2, 3, 4, 5]
result = ["even" if length % 2 == 0 else "odd" for length in nums]
print("11:", result)

# 12 -
divisible = [length for length in range(1, 101) if length % 3 == 0 and length % 5 == 0]
print("12:", divisible)

#  -13
table = [[index * step for step in range(1, 6)] for index in range(1, 6)]
print("13:", table)

# 14 -
my_dict = {"a": 1, "b": 2, "c": 3}
keys_list = [key for key in my_dict]
print("14:", keys_list)

# 15 -
string = "abc123xyz45"
digits = [ch for ch in string if ch.isdigit()]
print("15:", digits)

# 16 -
string = "Hello World Python"
no_spaces = "".join([ch for ch in string if ch != " "])
print("16:", no_spaces)

# 17 -
string = "programming"
duplicates = [ch for ch in set(string) if string.count(ch) > 1]
print("17:", duplicates)

# 18 -
sentences = ["I love Python", "List comprehension is powerful"]
all_words = [word for sentence in sentences for word in sentence.split()]
print("18:", all_words)

# 19 -
nums = [1, 2, 2, 3, 4, 4, 5]
unique = [length for index, length in enumerate(nums) if length not in nums[:index]]
print("19:", unique)

# 20
A = [1, 2, 3]
B = ['a', 'b']
pairs = [(input, buffer) for input in A for buffer in B]
print("20:", pairs)