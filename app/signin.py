from datetime import datetime
class SignIn:
    User = [{"username":"kica", "password":"12345","role":"bootcamp"}]
    

    def signin(self, username, password):
        for k in self.User:
            if k["username"] == username and k["password"] == password:
                k.update({"login_time":str(datetime.now())})
                return k
        return None
a = SignIn()
print(a.signin("kica","12345"))

