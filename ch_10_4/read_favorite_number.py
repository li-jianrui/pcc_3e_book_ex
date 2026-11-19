from pathlib import Path
import json

favorite_number_file = Path(__file__).with_name('favorite_number.json')

try:
    contents = favorite_number_file.read_text()
except FileNotFoundError:
    print(f"File {favorite_number_file} not found.")
else:
    favorite_number = json.loads(contents)
    print(f"Your favorite number is {favorite_number}.")