from src.hhapi import HeadHunterAPI
from src.vacancy import Vacancy


def salary_key(vacancy):
    return (
        vacancy.salary
        if isinstance(vacancy.salary, (int, float)) and vacancy.salary > 0
        else -1
    )


def user_interaction() -> None:
    """
    Функция для вызова всего.
    """
    hh_api = HeadHunterAPI()

    search_query = input("Введите поисковый запрос для вакансий: ")

    vacancies_data = hh_api.get_vacancies({"text": search_query, "area": 1})
    vacancies = []

    for item in vacancies_data:
        vacancies.append(
            Vacancy(
                name=item.get("name"),
                url=item.get("alternate_url"),
                salary=item.get("salary", {}).get("from"),
                description=item.get("snippet", {}).get("requirement", ""),
            )
        )

    if not vacancies:
        print("Вакансии не найдены.")
        return

    try:
        n = int(input("Введите количество вакансий, которые хотите увидеть (N): "))
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")
        return

    sorted_vacancies = sorted(vacancies, key=salary_key, reverse=True)

    print(f"\nТоп {n} вакансий по зарплате:")
    for vacancy in sorted_vacancies[:n]:
        print(vacancy)

    keyword = input("\nВведите ключевое слово для поиска в описании вакансий: ")

    keyword_vacancies = []

    for vacancy in vacancies:
        if keyword.lower() in vacancy.description.lower():
            keyword_vacancies.append(vacancy)

    print("\nВакансии с ключевым словом '{}' в описании:".format(keyword))
    for vacancy in keyword_vacancies:
        print(vacancy)


if __name__ == "__main__":
    user_interaction()
