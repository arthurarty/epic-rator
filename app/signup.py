"""
module signup
"""
class Users:
    
    def __init__(self, users=list()):
        self.users = users
        
        
    def register_user(self, username, password, role):
        """
        method registers new user
        """
        user = {
            'username': username,
            'password': password,
            'role': role
        }
        self.users.append(user)
        return self.users

if __name__ == '__main__':
    new_user = Users()
    print (new_user.register_user('bill', 'exchange', 'BootCamper')) 
