from typing import Any

import pytest

from src.hhapi import HeadHunterAPI
from src.vacancy import Vacancy


@pytest.fixture
def hh_data() -> Any:
    return HeadHunterAPI()


@pytest.fixture
def vacancies() -> Any:
    return Vacancy("Ну да")


def test_head_hunter_api(hh_data) -> None:
    assert hh_data is not None


def test_vacancy_init(vacancies) -> None:
    assert vacancies.name == "Таролог в Футбольный клуб «Сокол»"
    assert vacancies.url == "https://api.hh.ru/areas/88"
    assert vacancies.salary == 300000
    assert vacancies.description == "Ну да"
