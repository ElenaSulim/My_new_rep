from dataclasses import dataclass

@dataclass
class Human:
    name: str
    surname: str
    age: int

human = Human(name='Elena', surname='Sulim', age= 24)
print(human.name, human.surname, human.age)
