print("Enter two numbers to add.")
print("Enter 'q' to quit.")

while True:
    first_number = input("First number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        result = int(first_number) + int(second_number)
        print(f"The result is {result}")
    except ValueError:
        print("Please enter valid numbers.")