alien_color = "green"
alien_colors = ["green", "yellow", "red"]

print(f"The alien is {alien_color}.")
if alien_color in alien_colors:
    print("You just earned 5 points!")

alien_color = "black"
print(f"\nThe alien is {alien_color}.")
if alien_color in alien_colors:
    print("You just earned 5 points!")