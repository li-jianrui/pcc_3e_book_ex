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

class Privileges():
    def __init__(self):
        self.privileges = []

    def add_privilege(self, privilege):
        self.privileges.append(privilege)

    def show_privileges(self):
        print(f"Privileges: {', '.join(self.privileges)}")

class Admin(User):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.privileges = Privileges()

admin_1 = Admin("Alice", "Johnson", "alice.johnson@example.com")
admin_1.privileges.add_privilege("can add post")
admin_1.privileges.add_privilege("can delete post")
admin_1.privileges.add_privilege("can ban user")
admin_1.privileges.show_privileges()
