import allure
import pytest
from pages.main_page import MainPage
from src import data


class TestFAQ:

    @allure.title('Проверка вопросов в секции "Вопросы о важном"')
    @pytest.mark.parametrize('number, expected_question', data.data_questions_faq)
    def test_check_text_on_questions_faq(self, driver, number, expected_question):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.wait_visibility_cookie()
        main_page.close_cookie_window()
        main_page.scroll_faq_section(number)
        main_page.wait_visibility_faq_questions(number)
        main_page.wait_clickable_faq_questions(number)
        actual_question = main_page.get_questions_text(number)

        assert actual_question == expected_question, f"Ожидалось: {expected_question}, получено: {actual_question}"


    @allure.title('Проверка ответов в секции "Вопросы о важном"')
    @pytest.mark.parametrize('number, expected_answer', data.data_answers_faq)
    def test_check_text_on_answer_faq(self, driver, number, expected_answer):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.wait_visibility_cookie()
        main_page.close_cookie_window()
        main_page.scroll_faq_section(number)
        main_page.wait_visibility_faq_questions(number)
        main_page.wait_clickable_faq_questions(number)
        main_page.click_on_faq_questions(number)
        main_page.wait_visibility_faq_answer(number)
        actual_answer = main_page.get_answer_text(number)

        assert actual_answer == expected_answer, f"Ожидалось: {expected_answer}, получено: {actual_answer}"