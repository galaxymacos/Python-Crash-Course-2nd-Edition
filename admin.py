from user import *


class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    def __init__(self, first_name, last_name, age, sex, *privileges):
        super().__init__(first_name, last_name, age, sex)
        self.privileges = Privileges(privileges)


admin = Admin("Xun", "Ruan", 17, "Male", ["can add post", "can delete post"])
admin.privileges.show_privileges()