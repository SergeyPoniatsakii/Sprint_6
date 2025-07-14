import allure
import pytest
from data.faq_data import answers
from pages.main_page import MainPage


class TestFAQAnswers():
    @allure.title("Проверка ответов FAQ")
    @allure.description("Тестирование ответов в открывающихся секциях")
    @pytest.mark.parametrize( "faq_number, expected_answer", answers)

    def test_faq_answer(self, driver, faq_number, expected_answer):
        main_page = MainPage(driver)
        main_page.cookie_ok()
        main_page.faq_click(faq_number)
        assert main_page.faq_answer_get(faq_number) == expected_answer