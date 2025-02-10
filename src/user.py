
class User:

    def __init__(self, lang, username,password):
        self.preferred_language = lang
        self.username = username
        self.__password = password

    def __str__(self):
        #Returnerar klassen innehåll
        return (f"User: {self.preferred_language}, {self.username}"
                f" {self.__password}")

    #Alternativ use @property
    @property
    def password(self):
        print("Use property decorator")
        return self.__password

    def get_password(self):
        return self.__password



    def is_correct_login(self,username, password):
        if username == self.username and password == self.__password:
            return True
        else:
            return False