# Take inputs
num = [int(input("Enter an odd number: ")) for _ in range(4)]

# Pick only odd numbers (corrected condition)
odd = [i for i in num if i % 2 != 0]
print("Odd numbers:", odd)

# Fruit list in uppercase using list comprehension
fruit = ["banana", "apple", "mango"]
print("Original fruit list:", fruit)
fruit_upper = [item.upper() for item in fruit]
print("Uppercase fruit list:", fruit_upper)
