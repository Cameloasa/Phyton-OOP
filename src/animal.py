#2a Vad gör följande kod? Fixa eventuella fel.

#Variant 1
print("#Variant 1")
class Animal:
    def make_noise(self):
        print("Detta djur har vi inget ljud för.")

class Dog(Animal):
    def make_noise(self):
        print("Voff!") #indentering

class Cat(Animal):
    def make_noise(self): #self not shelf
        super().make_noise()
        print("Mjau!")

class Rooster(Animal):
    def make_noise(self):
        print("Kuckeliku!")

def sound_off(animal):
    animal.make_noise()

c = Cat()
d = Dog()
h = Rooster() #definera class Först innan vi instanțierea objekten

for animal in [c,d,h]:
    print(sound_off(animal))

#Variant2
print("#Variant 2")
class Animal:
    def make_noise(self):
        print("Detta djur har vi inget ljud för.")

class Dog(Animal):
    def make_noise(self):
        super().make_noise()
        print("Voff!")

class Cat(Animal):
    def make_noise(self):
        super().make_noise()
        print("Mjau!")

class Rooster(Animal):
    def make_noise(self):
        super().make_noise()
        print("Kuckeliku!")

def sound_off(animal):
    animal.make_noise()

c = Cat()
d = Dog()
h = Rooster()

for animal in [c, d, h]:
    sound_off(animal)

#Variant 3
print("#Variant 3")
class Animal:
    sound = "Detta djur har vi inget ljud för"  # statik variabel

    def make_noise(self):
        print(self.sound)

class Dog(Animal):
    sound = "Voff!"

class Cat(Animal):
    sound = "Mjau!"

class Rooster(Animal):
    sound = "Kuckeliku!"

def sound_off(animal):
    animal.make_noise()

c = Cat()
d = Dog()
h = Rooster()

for animal in [c, d, h]:
    sound_off(animal)

# Variant 4
print("#Variant 4")

class Animal:
    sound = None  #

    def make_noise(self):
        if self.sound:
            print(self.sound)
        else:
            sound_off(self)  #

class Dog(Animal):
    sound = "Voff!"

class Cat(Animal):
    sound = "Mjau!"

class Rooster(Animal):
    sound = "Kuckeliku!"

class Guldfisk(Animal):
    pass

def sound_off(animal):
    print("Detta djur har vi inget ljud för.")

c = Cat()
d = Dog()
h = Rooster()
i = Guldfisk()
x = Animal()

for animal in [c, d, h, i, x]:
    animal.make_noise()




