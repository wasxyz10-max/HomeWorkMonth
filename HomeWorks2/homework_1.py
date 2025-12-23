
class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education
        
    def introduce(self):
        print(f"Меня зовут {self.name}, я родился {self.birth_date}, моя профессия {self.occupation}, наличие высшего образования: {self.higher_education}")




if __name__ == "__main__":


    king_arthur = Person(name="Артур", birth_date="Неизвестно", occupation="Король Англии", higher_education=False)
    napoleon_bonaparte = Person(name="Наполеон бонапарт", birth_date="15.08.1769", occupation="Император франции", higher_education=True)
    prometei_gigant = Person(name="Прометей", birth_date="650 годами до нашей эры", occupation="Титан", higher_education=False)

    print(king_arthur.name,king_arthur.birth_date, king_arthur.occupation, king_arthur.higher_education, )
    print(napoleon_bonaparte.name, napoleon_bonaparte.birth_date, napoleon_bonaparte.occupation, napoleon_bonaparte.higher_education)
    print(prometei_gigant.name, prometei_gigant.birth_date, prometei_gigant.occupation, prometei_gigant.higher_education)

    king_arthur.introduce()
    napoleon_bonaparte.introduce()
    prometei_gigant.introduce()

    king_arthur.higher_education = True
    king_arthur.introduce()
    napoleon_bonaparte.higher_education = False
    napoleon_bonaparte.introduce()

    king_arthur.introduce()
    king_arthur.introduce()
    king_arthur.introduce()