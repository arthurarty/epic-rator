
class SignIn:
    User = [{"username":"kica", "password":"12345","role":"bootcamp"}]
    

    def signin(self, username, password):
        for k in self.User:
            if k["username"] == username and k["password"] == password:
                return k
        return None


