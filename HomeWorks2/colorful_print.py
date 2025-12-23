

from blessed import Terminal
from homework_1 import Person

term = Terminal()


fruits = [
    ('Яблоко', 'red', '🍎'),
    ('Банан', 'yellow', '🍌'),
    ('Апельсин', 'orange', '🍊'),
    ('Клубника', 'brightred', '🍓'),  
    ('Виноград', 'magenta', '🍇'),
]

for name, color_name, emoji in fruits:
    color = getattr(term, color_name)
    print(f'{emoji} {color}{name}{term.normal}')


person1 = Person('Иван', '01.01.2000', 'Программист', True)    
person2 = Person('Анна', '15.05.1995', 'Учитель', False)

person1.introduce()
person2.introduce()