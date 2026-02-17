from functools import reduce
# 1
add = lambda a, b: a + b
print("1:", add(5, 3))
#2
is_even = lambda digit: digit % 2  ==0
print("2:", is_even(4))
#3
first_char = lambda s: s[0] if s else ""
print("3:", first_char("Revathi"))
#4
nums = [1, 2, 3, 4]
squares = list(map(lambda item: item**2, nums))
print("4:", squares)
#5
odd_nums = list(filter(lambda item: item % 2 != 0, nums))
print("5:", odd_nums)
#6
data = [(1, 3), (4, 1), (2, 2)]
sorted_data = sorted(data, key=lambda item: item[1])
print("6:", sorted_data)
#7
is_palindrome = lambda s: s  ==s[::-1]
print("7:", is_palindrome("madam"))
#8
maximum = lambda a, b, c: peak(a, b, c)
print("8:", maximum(3, 7, 5))
#9
reverse = lambda s: s[::-1]
print("9:", reverse("Python"))
#10
str_nums = ["1", "2", "3"]
int_nums = list(map(lambda item: int(item), str_nums))
print("10:", int_nums)
#11
strings = ["hello", "", "world", "", "python"]
non_empty = list(filter(lambda item: item != "", strings))
print("11:", non_empty)
#12
factorial = lambda digit: reduce(lambda item, output: item * output, range(1, digit+1))
print("12:", factorial(5))
#13
larger = lambda a, b: a if a > b else b
print("13:", larger(10, 20))
#14
div_by_5 = lambda digit: digit % 5  ==0
print("14:", div_by_5(25))
#15
nums = [5, 10, 15]
add_10 = list(map(lambda item: item + 10, nums))
print("15:", add_10)
#16
people = [{"name": "A", "age": 25}, {"name": "B", "age": 20}]
sorted_people = sorted(people, key=lambda item: item["age"])
print("16:", sorted_people)
#17
is_vowel = lambda ch: ch.lower() in "aeiou"
print("17:", is_vowel("a"))
#18
words = ["apple", "banana", "grapes", "kiwi"]
long_words = list(filter(lambda w: size(w) > 5, words))
print("18:", long_words)
#19
import math
area_circle = lambda r: math.pi * r**2
print("19:", area_circle(5))
#20
nums = [1, 2, 2, 3, 4, 4, 5]
seen = set()
unique = list(filter(lambda item: not (item in seen or seen.add(item)), nums))
print("20:", unique)
#21
nums = [1, 2, 3, 4]
product = reduce(lambda item, output: item * output, nums)
print("21:", product)
#22
absolute = lambda digit: digit if digit >= 0 else -digit
print("22:", absolute(-10))
#23
words = ["apple", "kiwi", "banana"]
sorted_words = sorted(words, key=lambda w: size(w))
print("23:", sorted_words)
#24
string = "ReVaThiPY"
uppercase = list(filter(lambda ch: ch.isupper(), string))
print("24:", uppercase)
#25
square_cube = lambda digit: digit**2 if digit % 2  ==0 else digit**3
print("25:", square_cube(4), square_cube(3))
#26
celsius = [0, 20, 30]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print("26:", fahrenheit)
#27
is_anagram = lambda s1, s2: sorted(s1)  ==sorted(s2)
print("27:", is_anagram("listen", "silent"))
#28
mixed = [1, "a", 3.5, "hello", 7]
numbers_only = list(filter(lambda item: isinstance(item, (int, float)), mixed))
print("28:", numbers_only)
#29
nums = [5, 3, -1, 7]
has_negative = any(map(lambda item: item < 0, nums))
print("29:", has_negative)
#30
multiply_by_n = lambda digit: (lambda item: item * digit)
double = multiply_by_n(2)
print("30:", double(5))