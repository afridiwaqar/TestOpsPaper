# user_management.py

class UserAlreadyExistsError(Exception):
    pass

class UserNotFoundError(Exception):
    pass

class InvalidPasswordError(Exception):
    pass

class UserManagement:
    def __init__(self):
        self.users = {}

    def register_user(self, username, email, password):
        if username in self.users:
            raise UserAlreadyExistsError("Username already exists")
        self.users[username] = {
            'email': email,
            'password': password
        }
        return "Registration successful"

    def login_user(self, username, password):
        if username not in self.users:
            raise UserNotFoundError("User not found")
        if self.users[username]['password'] != password:
            raise InvalidPasswordError("Invalid password")
        return f"Welcome {username}!"

    def get_user_info(self, username):
        if username not in self.users:
            raise UserNotFoundError("User not found")
        return self.users[username]

# Example usage
if __name__ == "__main__":
    um = UserManagement()
    try:
        print(um.register_user('testuser', 'testuser@example.com', 'password'))
        print(um.login_user('testuser', 'password'))
        print(um.get_user_info('testuser'))
    except Exception as e:
        print(e)

