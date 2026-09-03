class Vec2:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vec2(self.x * other, self.y * other)
        else:
            return Vec2(self.x * other.x, self.y * other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y 

    def __repr__(self):
        return  f"Vec2({self.x}, {self.y})"

    def __len__(self):
        return 2  # A Vec2 always has 2 dimensions (x and y)

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vec2 index out of range (use 0 for x, 1 for y)")
    def __rmul__(self, other):
        return self.__mul__(other)

i = Vec2(2, 7)
j = Vec2(3, 9)

assert i + j == Vec2(5, 16), f"Add Expected (5, 16) giving {i+j}"

assert i - j == Vec2(-1, -2), f"Sub Expected (-1, -2) giving {i-j}"    

assert i*j == Vec2(6, 63), f"Mul Expected (6, 63) giving {i*j}"

assert i*5 == Vec2(10, 35), f"lmul Expected (-1, -2) giving {i*5}"

print("All 4 assertions passed")


# Create test vectors
v1 = Vec2(3, 4)
v2 = Vec2(1, 2)

# 1. Addition (__add__)
v_add = v1 + v2
assert v_add.x == 4 and v_add.y == 6, f"Expected Vec2(4, 6), got {v_add}"

# 2. Subtraction (__sub__)
v_sub = v1 - v2
assert v_sub.x == 2 and v_sub.y == 2, f"Expected Vec2(2, 2), got {v_sub}"

# 3. Scalar Multiplication (__mul__)
v_mul_scalar = v1 * 3
assert (
    v_mul_scalar.x == 9 and v_mul_scalar.y == 12
), f"Expected Vec2(9, 12), got {v_mul_scalar}"

# 4. Vector Multiplication (__mul__)
v_mul_vec = v1 * v2
assert (
    v_mul_vec.x == 3 and v_mul_vec.y == 8
), f"Expected Vec2(3, 8), got {v_mul_vec}"

# 5. Reverse Scalar Multiplication (__rmul__)
v_rmul = 2 * v1
assert (
    v_rmul.x == 6 and v_rmul.y == 8
), f"Expected Vec2(6, 8), got {v_rmul}"

# 6. Equality True (__eq__)
assert v1 == Vec2(3, 4), "Expected v1 == Vec2(3, 4) to be True"

# 7. Equality False (__eq__)
assert (v1 == v2) == False, "Expected v1 == v2 to be False"

# 8. Representation (__repr__)
assert repr(v1) == "Vec2(3, 4)", f"Expected 'Vec2(3, 4)', got {repr(v1)}"

# 9. Length / Dimension Count (__len__)
assert len(v1) == 2, f"Expected length 2, got {len(v1)}"

# 10. Indexing (__getitem__)
assert v1[0] == 3 and v1[1] == 4, f"Expected v1[0]=3 and v1[1]=4, got {v1[0]}, {v1[1]}"

print("All 10 assertions passed successfully! 🚀")
