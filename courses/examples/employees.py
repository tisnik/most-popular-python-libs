class Person:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname


class Employee(Person):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self._salary = None

    def set_salary(self, salary):
        if salary <= 0:
            raise ValueError("improper salary")
        if salary > 100000:
            raise ValueError("improper salary: too much")
        self._salary = salary

    def get_salary(self):
        return self._salary

    def display(self):
        print(f"Employee {self._name} {self._surname} with salary {self._salary} CZK")

    def __str__(self):
        return f"Employee {self._name} {self._surname} with salary {self._salary} CZK"


class Contractor(Employee):

    def __init__(self, name, surname, from_date, to_date):
        super().__init__(name, surname)
        self._from_date = from_date
        self._to_date = to_date

    def display(self):
        print(f"Contractor {self._name} {self._surname} with salary {self._salary} CZK")

    def __str__(self):
        return f"Contractor {self._name} {self._surname} with salary {self._salary} CZK: start/end {self._from_date}/{self._to_date}"

class Intern(Employee):

    def __init__(self, name, surname, from_date, to_date, age):
        super().__init__(name, surname)
        self._from_date = from_date
        self._to_date = to_date
        self._age = age

    def display(self):
        print(f"Intern {self._name} {self._surname} with salary {self._salary} CZK")

    def __str__(self):
        return f"Intern {self._name} {self._surname} with salary {self._salary} CZK: start/end {self._from_date}/{self._to_date}"



e = Contractor("Pepa", "Novak", "2025-06-20", "2025-09-01")
e.set_salary(10000)
print(e)

e2 = Employee("Ivan", "Necas")
e2.set_salary(20000)
print(e2)
