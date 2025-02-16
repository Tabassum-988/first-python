# Numeric Data Types
# Integer
X = 10
print(X)

# Float
Y = 12.7
print(Y)

# Complex
Z = 10 + 20j
print(Z)

# String
Letter = ["A", "B", "C"]
print(Letter)

# Tuple (Immutable Sequence)
Country = ("Canada", "Japan", "Finland")
print(Country)

# Sequence Types
# List (Mutable, like an array)
my_list = [10, 20.5, "Tabassum", "Japan"]
print(my_list[2])  # Accessing the third element

# Tuple (Immutable)
id_numbers = ("234", "543", "228")
print(id_numbers)

# Range
number = range(1, 10)
print(*number)  # Unpacking the range

odd_number = range(1, 10, 2)
print(*odd_number)

even_number = range(2, 20, 2)
print(*even_number)

num = range(5)  # Equivalent to range(0,5)
print(*num)

# Boolean (Only True/False)
isStudent = True
print(isStudent)

# None (Represents absence of a value)
taka = None
print(taka)

# Mapping (Dictionary: Key-Value Pairs)
# Ordered (indexed)
person = {
    "Name": "Tabassum Sultana",  # Removed extra space in key
    "Age": 24,
    "isStudent": True,
}
print(person)
print(person["Age"])  # Fixed key case sensitivity

# Set (Unordered, Unique, Mutable)
position = {1, 2, 3, 4}
print(position)

# FrozenSet (Unordered, Unique, Immutable)
position2 = frozenset([4, 5, 6, 7])
print(position2)
