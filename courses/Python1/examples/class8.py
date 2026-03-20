class Employee:

    def __init__(self, first_name, surname, salary):
        self._first_name = first_name
        self._surname = surname
        self._salary = salary

    def __str__(self):
        return "Full name: {name} {surname}   Salary: {salary}".format(name=self._first_name,
                                                                       surname=self._surname,
                                                                       salary=self._salary)


employee1 = Employee("Eda", "Wasserfall", 10000)
employee2 = Employee("Přemysl", "Hájek", 25001)

print(employee1)
print(employee2)
