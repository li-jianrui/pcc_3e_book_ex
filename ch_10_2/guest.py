from pathlib import Path

guest = input("Please enter your name: ")
print(f"Hello, {guest}!")

file_path = Path(__file__).with_name('guest.txt')
file_path.write_text(guest)