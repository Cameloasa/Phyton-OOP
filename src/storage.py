#1 Vad gör följande kod?
class SafeStorage:
    __data = None
    def get(self):
        return self.__data
    def put(self, data):
        self.__data = data

safe = SafeStorage()
safe.put("Anakonda")
x = safe.get()
safe.put("Boaorm")
y = safe.get()
print(x, y)

class SafeStorage:
    def __init__(self):
        self.__data = None  # Privat instansattribut

    def get(self):
        if self.__data is None:
            raise ValueError("Ingen data lagrad!")  # Förhindrar åtkomst till None
        return self.__data

    def put(self, data):
        if not isinstance(data, str):  # Säkerställer att endast strängar kan lagras
            raise TypeError("Endast strängar är tillåtna!")
        self.__data = data

safe = SafeStorage()
safe.put("Anakonda")
x = safe.get()

safe.put("Boaorm")
y = safe.get()

print(x, y)