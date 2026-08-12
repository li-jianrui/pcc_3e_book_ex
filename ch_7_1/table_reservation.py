num_ppl = input("How many people are in your dinner group? ")
if int(num_ppl) > 8:
    print("You'll have to wait for a table.")
elif int(num_ppl) > 0:
    print("Your table is ready.")
else:
    print("Please enter a valid number of people.")