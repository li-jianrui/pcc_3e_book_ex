ticket_price = ""
while ticket_price != "quit":
    ticket_price = input("Please enter the age of the ticket holder (or 'quit' to exit): ")
    if ticket_price != "quit":
        age = int(ticket_price)
        if 0 <= age < 3:
            print("The ticket is free.")
        elif 3 <= age < 12:
            print("The ticket price is $10.")
        elif age >= 12:
            print("The ticket price is $15.")
        else:
            print("Please enter a valid age.")