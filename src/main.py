from src.user import User

my_user = User("romanian", "Cami", "1234")

print(my_user)

print(my_user.get_password())
print(my_user.password)

my_user.is_correct_login("Cami","1234")
