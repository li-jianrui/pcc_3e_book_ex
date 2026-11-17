from random import choices

combination = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "B", "C", "D", "E"]

winning_combination = choices(combination, k=4)

print(f"The winning combination is {" ".join(winning_combination)}")
