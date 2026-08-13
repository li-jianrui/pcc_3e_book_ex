sandwich_orders = ['tuna', 'ham', 'pastrami', 'turkey', 'pastrami', 'veggie', 'pastrami']
finished_sandwiches = []
print("The deli has run out of pastrami.")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    if current_sandwich == 'pastrami':
        continue
    else:
        print(f"I made your {current_sandwich} sandwich.")
        finished_sandwiches.append(current_sandwich)
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
