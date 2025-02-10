from src.country import Country
from src.user import User

print("User")
my_user = User("romanian", "Cami", "1234")
print(my_user)
print(my_user.get_password())
print(my_user.password)
my_user.is_correct_login("Cami","1234")

print("************")
print("Countries")
se = Country("Sverige", 10.5)
no = Country("Norge", 5.5)
se.print_info()
no.print_info()