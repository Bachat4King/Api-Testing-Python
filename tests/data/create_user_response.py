class CreateUserResponse:
    def __init__(self, id=None, token=None):
        self.id = id
        self.token = token

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def token(self):
        return self.token

    def set_token(self, token):
        self.token = token
