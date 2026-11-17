class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}, Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

user_1 = User("John", "Doe", "john.doe@example.com")
user_1.describe_user()
user_1.greet_user()

user_2 = User("Jane", "Smith", "jane.smith@example.com")
user_2.describe_user()
user_2.greet_user()

user_3 = User("Alice", "Johnson", "alice.johnson@example.com")
user_3.describe_user()
user_3.greet_user()

