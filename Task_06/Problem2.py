from datetime import datetime
class Person:
    def __init__(self, name, country, birthDate):
        self.name = name
        self.country = country
        self.birthDate = birthDate
    
    def calculate_Age(self):
        today = datetime.now()
        birthDate = datetime.strptime(self.birthDate, "%Y-%m-%d")
        Age = today.year - birthDate.year
        return Age

    def print_Data(self):
        return f"""
        Name: {self.name}
        Country: {self.country}
        Date of Birth: {self.birthDate}
        Age: {self.calculate_Age()} """

Person_one = Person("Ferdi Odilia", "France", "1962-07-12")

print("Person_one:",Person_one.print_Data())
    
