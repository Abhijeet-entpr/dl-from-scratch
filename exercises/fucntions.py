from functools import wraps
import time
# Mutable-Default Bug & Its Fix

# def append_bug(item, target=[]):
#     target.append(item)
#     return target

# print(append_bug(1))  # Returns [1]
# print(append_bug(3)) 
# print(append_bug(4)) 
# print(append_bug(5)) 

# def append_fixed(item, target=None):
#     if target is None:
#         target=[]
#     target.append(item)
#     return target


# print(append_fixed(1))  # Returns [1]
# print(append_fixed(3)) 
# print(append_fixed(4)) 
# print(append_fixed(5)) 


# Function Taking *args and **kwargs
# pos = [1, 2, 3]
# keyargs = {'a': 4, 'b': 5, 'c': 6}
# def print_pos_and_key_args(*args, **kwargs):
#     a = 0;
#     for arg in args:
#         a += arg;
#     print("Positional arguments:", a)
#     print("Keyword arguments:", kwargs)

# print_pos_and_key_args(*pos, **keyargs)


# def make_couter(start = 0):
#     count = start
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#     print(count)
#     return counter

# make_couter()
# make_couter()
# make_couter()

# Step 1: c = make_couter(0)
# ----------------------------------------------------------------------
# [Heap Memory]
# Cell Object ---> holds value: 0

# [make_couter Execution]
# 1. Initializes Cell Object to 0.
# 2. Creates 'counter' function object.
# 3. Attaches 'counter' function to the Cell Object.
# 4. Returns 'counter' function object and assigns it to 'c'.
# ----------------------------------------------------------------------

# Step 2: First call: c()
# ----------------------------------------------------------------------
# 1. 'c()' runs inside its closure.
# 2. 'nonlocal count' tells Python: "Look at the attached Cell Object."
# 3. Updates value in Cell Object from 0 -> 1.
# 4. Returns 1.
# ----------------------------------------------------------------------

# Step 3: Second call: c()
# ----------------------------------------------------------------------
# 1. 'c()' runs again.
# 2. Accesses the SAME attached Cell Object (now holding 1).
# 3. Updates value in Cell Object from 1 -> 2.
# 4. Returns 2.
# ----------------------------------------------------------------------

# c = make_couter(10)

# # 1. 'c' has an attribute '__closure__' containing tuple of cells
# print(c.__closure__)
# # Output: (<cell at 0x...: int object at 0x...>,)

# # 2. Inspect the actual value stored inside the cell
# print(c.__closure__[0].cell_contents)
# # Output: 10

# # Call the counter
# c()

# # 3. Check the cell contents again!
# print(c.__closure__[0].cell_contents)
# # Output: 11


def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {elapsed_time:.6f} seconds")
        return result
    return wrapper

@time_it
def func_test():
    total = 0
    for i in range(1000000):
        total += i
    return total

result = func_test()