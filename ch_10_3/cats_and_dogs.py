from pathlib import Path
cats_file_path = Path(__file__).with_name('cats.txt')
dogs_file_path = Path(__file__).with_name('dogs.txt')

try:
    cats = cats_file_path.read_text()
except FileNotFoundError:
    print(f"File {cats_file_path} not found.")
else:
    print(f"File {cats_file_path} read successfully.")
    print(cats)
try:
    dogs = dogs_file_path.read_text()
except FileNotFoundError:
    print(f"File {dogs_file_path} not found.")
else:
    print(f"File {dogs_file_path} read successfully.")
    print(dogs)
