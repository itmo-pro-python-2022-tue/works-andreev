class Staff:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        if 40_000 <= salary <= 70_000:
            self.__salary = salary
        else:
            self.__salary = None

    def __str__(self):
        return f'Staff({self.name}, {self.position}, {self.__salary})'

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if 40_000 <= new_salary <= 70_000:
            self.__salary = new_salary


barista = Staff('Прядкин Олег Александрович', 'Бариста', 50_000)
print(barista)

print(barista.salary)

# way_too_large_salary = barista.salary * 10
# barista.salary = way_too_large_salary
barista.salary += 10_000
print(barista)
