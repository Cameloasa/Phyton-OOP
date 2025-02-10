class Country:
    def __init__(self, name, pop):
        self.__name = name
        self.__population = pop


    def print_info(self):
        info = f"I {self.__name} bor det {self.__population} miljoner invånare."
        print(info)