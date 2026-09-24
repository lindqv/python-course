class User:
    def __init__(self, username: str):
        self.username = username

class AdminUser(User):
    def __init__(self, username: str):
        super().__init__(username)
        self.is_admin = True

admin  = AdminUser("admin")

print(isinstance(admin, AdminUser))
print(isinstance(admin, User))
print(isinstance(admin, str))

# AdminUser is also considered an instance of User since AdminUser inherits from User.
# Or in other words, AdminUser is a subclass of User.