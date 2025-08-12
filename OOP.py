class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I am {self.name}, protector of {self.city}!")
    
    def use_power(self):
        print(f"{self.name} uses {self.power}!")
        print(f"{self.name} saves the day in {self.city}!")

class FlyingHero(Superhero):
    def __init__(self, name, power, city, altitude):
        super().__init__(name, power, city)
        self.altitude = altitude

    def use_power(self):  # Polymorphism
        print(f"{self.name} soars at {self.altitude} meters using {self.power}!")

hero1 = Superhero("Bolt", "Speed", "Nairobi")
hero2 = FlyingHero("SkyWing", "Flight", "Murang'a", 3000)

hero1.introduce()
hero1.use_power()

hero2.introduce()
hero2.use_power()