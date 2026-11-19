from pathlib import Path
import json

username_file = Path(__file__).with_name('me.json')

user = {}

if username_file.exists():
    contents = username_file.read_text()
    user = json.loads(contents)
    print(f"Welcome back, {user['user_name']}!")
    print(f"Your mail address is {user['mail_address']}.")
else:
    user_name = input("What is your user name? ")
    mail_address = input("What is your mail address? ")

    user['user_name'] = user_name
    user['mail_address'] = mail_address

    contents = json.dumps(user)
    username_file.write_text(contents)