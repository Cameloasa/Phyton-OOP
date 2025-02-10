class Country:
    def __init__(self, name, pop, area=None,):
        self.__name = name
        self.__population = pop
        self.__area = area
        self.__languages = []


    def print_info(self):
        info = f"I {self.__name} bor det {self.__population} miljoner invånare."
        if self.__area is not None:
            info += f" Landets area är {self.__area} km²."
        print(info)

        if self.__languages:
            print("Officiella språk:", ", ".join(self.__languages))


    def add_language(self, language):
        self.__languages.append(language)