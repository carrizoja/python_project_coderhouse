class Person:
    def __init__(self, name, lastname, date, gender):
        self.name = name
        self.lastname = lastname
        self.date = date
        self.gender = gender

    def __str__(self):
        return self.name + ' ' + self.lastname + ' ' + self.date + ' ' + self.gender

    def say_hi(self):
      return print(f'Hello! My name is {self.name} {self.lastname} and my date is {self.date}. I am {self.gender}')







