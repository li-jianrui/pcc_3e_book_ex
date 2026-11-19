from pathlib import Path
import json

favorite_number_file = Path(__file__).with_name('favorite_number.json')

favorite_number = input("What is your favorite number? ")

contents = json.dumps(favorite_number)

favorite_number_file.write_text(contents)