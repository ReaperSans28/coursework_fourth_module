from src.hhapi import HeadHunterAPI
from src.vacancy import Vacancy
from src.working_with_files import WorkingWithData


def user_interaction() -> None:
    hh_api = HeadHunterAPI()

    search_query = input("Введите поисковый запрос для вакансий: ")

    vacancies_data = hh_api.get_vacancies({"text": search_query})

    vacancy_objects = []

    for vacancy in vacancies_data:
        vacancy_obj = Vacancy(vacancy)
        vacancy_objects.append(vacancy_obj.to_dict())

    data_handler = WorkingWithData()

    for vacancy in vacancy_objects:
        data_handler.add_to_json(vacancy)

    saved_vacancies = data_handler.read_json()
    print("Сохраненные вакансии:", saved_vacancies)


if __name__ == "__main__":
    user_interaction()
