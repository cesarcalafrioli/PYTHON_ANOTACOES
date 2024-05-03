my_numbers = (1, 1, 2, 3, 5, 8, 13, 21)

print("Last element:")
print(my_numbers[-1])

print("Second element via negative index:")
print(my_numbers[-3])

print("Obtaining many elements using slice:")
print(my_numbers[2:5])

print("Everything up to the index in the position 3:")
print(my_numbers[:3])

print("Everything from the index position 3 until the last element")
print(my_numbers[3:])

print("List everything:")
print(my_numbers[::])

print("Elements in the position one and seven jumping by two:")
print(my_numbers[1:7:2])

# Instead of manually iterate the tuple, string or list inside a for loop and exclude elements by hand, use
# built-in sintax for slices, as examples below.
interval = slice(1, 7, 2)
print("Same thing above, but using built-in function slice:")
print(my_numbers[interval])

interval = slice(None, 3)
print("Example 2:")
print(my_numbers[interval] == my_numbers[:3])
