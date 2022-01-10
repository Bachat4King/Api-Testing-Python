class CreateUser:
    def __init__(self, email=None, password=None):
        self.email = email
        self.password = password

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def set_email(self, email):
        self.email = email

    def set_password(self, password):
        self.password = password