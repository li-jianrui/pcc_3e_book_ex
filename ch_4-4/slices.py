numbers = list(range(3, 34, 3))

print("The first three items in the list are:")
for num in numbers[:3]:
    print(num)

print("Three items from the middle of the list are:")
for num in numbers[4:7]:
    print(num)

print("The last three items in the list are:")
for num in numbers[-3:]:
    print(num)