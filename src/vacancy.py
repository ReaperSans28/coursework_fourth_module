class Vacancy:
    """
    Класс для работы с вакансиями.
    """

    def __init__(self, name, url, salary, description):
        self.name = name
        self.url = url
        self.salary = self.validate_salary(salary)
        self.description = description

    @staticmethod
    def validate_salary(salary):
        if salary is None or salary <= 0:
            return "Зарплата не указана"
        return salary

    def __lt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary < other.salary
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary > other.salary
        else:
            return NotImplemented

    def __repr__(self):
        return f"Vacancy(name='{self.name}', url='{self.url}', salary='{self.salary}', description='{self.description}')"
