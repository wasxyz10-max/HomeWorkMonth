
class Person:
    def __init__(self, name, birth_date, occupation):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я родился {self.birth_date},  работаю {self.occupation}") 
            


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, group_name):
        super().__init__(name, birth_date, occupation)
        self.group_name = group_name
    def introduce(self):
            print(f"Привет, меня зовут {self.name},я одноклассник {self.group_name} я родился {self.birth_date},  работаю {self.occupation}") 
 

class Friend(Person):
    def __init__(self, name, birth_date, occupation, hobby):
        super().__init__(name, birth_date, occupation)
        self.hobby = hobby
    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я друг {self.hobby} я родился {self.birth_date},  работаю {self.occupation}") 



fred = Friend("Амантур", "Бектура", "01.01.1990", "программистом")
classmate = Classmate("Эдик", "Ивана", "02.02.1991", "программистом")
bektyr = Friend("Бектур", "Адилета", "03.03.1992", "программистом")
bekjan = Classmate("Бекжан", "Асылбека", "04.04.1993", "программистом")

fred.introduce()
classmate.introduce()

object_list = [fred, classmate, bektyr, bekjan]

for obj in object_list:
    obj.introduce()