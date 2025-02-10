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
# Skapa objekt för Sverige, Norge, Island och Danmark
se = Country("Sverige", 10.5, 447425)
no = Country("Norge", 5.5, 385207)
island = Country("Island", 0.38, 103000)
danmark = Country("Danmark", 6.0, 42924)

# Lägg till språk
se.add_language("Svenska")
no.add_language("Norska")
no.add_language("Svenska")
island.add_language("Isländska")
danmark.add_language("Danska")

# Testa print_info-metoden
se.print_info()
no.print_info()
island.print_info()
danmark.print_info()
