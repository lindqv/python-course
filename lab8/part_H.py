class User:
    def __init__(self, username: str, email: str):
        if len(username) == 0:
            raise ValueError("Username cannot be empty")
        self.username = username
        self.email = email

    def get_email(self):
        return self.email

    def get_username(self):
        return self.username


class AdminUser(User):
    def __init__(self, username: str, email: str, admin_rights = True):
        super().__init__(username, email)
        self.admin_rights = admin_rights

    def has_admin_rights(self):
        return self.admin_rights

    def get_username(self):
        if self.has_admin_rights():
            return "admin_" + self.username
        else:
            return super().get_username()

class PremiumUser(User):
    def __init__(self, username: str, email: str, membership_months: int):
        super().__init__(username, email)
        self.membership_months = membership_months

    def get_membership_months(self):
        return self.membership_months

    def get_username(self):
        return "premium_" + self.username

anna = AdminUser("anna", "anna@example.com")
anthony = AdminUser("anthony", "anthony@example.com")
alina = PremiumUser("alina", "alina@example.com", 12)
alex = User("alex", "alex@example.com")

print(anna.has_admin_rights())
print(anthony.has_admin_rights())
setattr(anthony, "admin_rights", False)
print(anna.has_admin_rights())
print(anthony.has_admin_rights())

print(alina.get_username())
print(alex.get_username())
print(anna.get_username())
print(anthony.get_username())

print(alina.get_email())
print(alex.get_email())
print(anna.get_email())
print(anthony.get_email())

# AdminUser and PremiumUser have an "is-a" relationship with User, since they both are Users. Like so:
# 1. AdminUser is a User
# 2. PremiumUser is a User