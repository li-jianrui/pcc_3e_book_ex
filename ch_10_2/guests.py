from pathlib import Path

file_path = Path(__file__).with_name('guest_book.txt')

names = ""
name = input("Please enter your name, enter 'q' to quit: ")
while name != 'q':
    names += name + "\n"
    name = input("Please enter your name, enter 'q' to quit: ")

file_path.write_text(names)