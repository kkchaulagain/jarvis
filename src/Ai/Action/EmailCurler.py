class EmailCurler:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def get_emails(self):
        return self.email, self.password