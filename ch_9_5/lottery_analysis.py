from random import choices

combination = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "B", "C", "D", "E"]

my_ticket = choices(combination, k=4)

winning_combination = choices(combination, k=4,)
trail_num = 0

while my_ticket != winning_combination:
    trail_num += 1
    my_ticket = choices(combination, k=4)

print(f"It took {trail_num} tries to win the lottery with the ticket {" ".join(my_ticket)}")