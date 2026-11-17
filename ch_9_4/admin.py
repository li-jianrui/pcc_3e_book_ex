from user import User

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


