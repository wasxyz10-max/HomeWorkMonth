
class Person:

    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education


    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я родился {self.birth_date},  работаю {self.__occupation}, наличие высшего образования: {self.__higher_education}") 
            


class Classmate(Person):
    def __init__(self, name, group_name, birth_date, occupation, higher_education):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name


    def introduce(self): 
        if self.higher_education:
            print(f"Привет, меня зовут {self.name}, учился в группе {self.group_name}, я родился {self.birth_date},  работаю {self.occupation} у меня есть высшее образование")
        elif not self.higher_education: 
            print(f"Привет, меня зовут {self.name}, учился в группе {self.group_name}, я родился {self.birth_date},  работаю {self.occupation} у меня нет высшего образования")
 

class Friend(Person):
    def __init__(self, name, hobby, birth_date, occupation, higher_education):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    
    def introduce(self): 
        if self.higher_education:
            print(f"Привет, меня зовут {self.name}, мое хобби {self.hobby} я родился {self.birth_date},  работаю {self.occupation} у меня есть высшее образование")
        elif not self.higher_education: 
            print(f"Привет, меня зовут {self.name}, мое хобби {self.hobby} я родился {self.birth_date},  работаю {self.occupation} у меня нет высшего образования")


fred = Friend("Амантур", "футбол", "01.01.1990", "студент", True)
classmate = Classmate("Эдик", "V23", "02.02.1991", "программистом", False)
     

fred.introduce()
classmate.introduce()
fred.introduce()
classmate.introduce()