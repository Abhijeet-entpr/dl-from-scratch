squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

x = [x**2 for x in range(10)]

print(x)

evens = []
for x in range(20):
    if x % 2 == 0:
        evens.append(x)

even_filter = [x for x in range(21) if x % 2 == 0]

print(even_filter)

labels = []
for x in range(5):
    if x % 2 == 0:
        labels.append("even")
    else:
        labels.append("odd")

label_comp = ["even" if x % 2 == 0 else "odd" for x in range(8)]

print(label_comp)

words = ["python", "is", "fun", "code", "iterators"]
long_upper = []
for w in words:
    if len(w) > 3:
        long_upper.append(w.upper())

long_upper_comp = [x.upper() for x in words if len(x) > 3]

print(long_upper)
print(long_upper_comp)

matrix = [[1, 2], [3, 4], [5, 6]]
flat = []
for row in matrix:
    for item in row:
        flat.append(item)

print([item for row in matrix for item in row])


words = ["apple", "banana", "pear", "apple", "fig"]
unique_lengths = set()
for w in words:
    unique_lengths.add(len(w))

print({len(item) for item in words})


cubes = {}
for x in range(1, 6):
    cubes[x] = x**3

print({x: x**3 for x in range(1, 6)})

scores = {"Alice": 85, "Bob": 62, "Charlie": 91, "Diana": 58}
passing = {}
for name, score in scores.items():
    if score >= 70:
        passing[name] = score

{key: val for key, val in scores.items() if val >= 70}


######## Batch Generator

def batch_generator(data, n):
    for i in range(0, len(data), n):
        yield data[i : i + n]

items = list(range(23))
for batch in batch_generator(items, 5):
    print(batch)


##### Compare sys.getsizeof: list comprehension vs generator over 1M items


import sys

# 1. List Comprehension (uses square brackets)
list_comp = [x for x in range(1_000_000)]

# 2. Generator Expression (uses parentheses)
gen_exp = (x for x in range(1_000_000))   

print("List size:", sys.getsizeof(list_comp), "bytes")
print("Generator size:", sys.getsizeof(gen_exp), "bytes")