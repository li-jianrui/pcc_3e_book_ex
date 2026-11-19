from pathlib import Path
import json

favorite_number_file = Path(__file__).with_name('favorite_number.json')

if favorite_number_file.exists():
    contents = favorite_number_file.read_text()
    favorite_number = json.loads(contents)
    print(f"Your favorite number is {favorite_number}.")
else:
    favorite_number = input("What is your favorite number? ")
    contents = json.dumps(favorite_number)
    favorite_number_file.write_text(contents)