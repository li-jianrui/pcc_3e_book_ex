class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}, Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def print_login_attempts(self):
        print(f"Login attempts: {self.login_attempts}")

user_1 = User("John", "Doe", "john.doe@example.com")
user_1.describe_user()
user_1.greet_user()

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.print_login_attempts()
user_1.reset_login_attempts()
user_1.print_login_attempts()
