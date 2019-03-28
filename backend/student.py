# sample class
class Student:
    def __init__(self, first: str, last: str, scholarship: int):
        self.scholarship = scholarship
        self.last = last
        self.first = first

    @property
    def email(self):
        return f'{self.first[0].lower()}.{self.last.lower()}@innopolis.ru'

    @property
    def full_name(self):
        return f'{self.first} {self.last}'

    @property
    def is_in_36k_club(self):
        return self.scholarship == 36000
