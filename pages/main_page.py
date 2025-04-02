from pages.base_page import BasePage
from src import data
from src.data import BASE_URL
from pages.main_page_locators import MainPageLocators as mpl
import allure


MAIN_PAGE_URL = BASE_URL

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_main_page(self):
        self.open_page(MAIN_PAGE_URL)

    def wait_visibility_cookie(self):
        cookie_locator = mpl.COOKIE_BUTTON
        self.wait_visibility_of_element_located(cookie_locator)

    @allure.step('Окно Cookie закрыто')
    def close_cookie_window(self):
        self.click_on_element(mpl.COOKIE_BUTTON)

    @allure.step('Скролл до секции с вопросами')
    def scroll_faq_section(self, test_faq_sections):
        questions_locator = mpl.FAQ_QUESTIONS.get(test_faq_sections)
        self.scroll_to_element(questions_locator)

    def wait_visibility_faq_questions(self, test_faq_sections):
        questions_locator = mpl.FAQ_QUESTIONS.get(test_faq_sections)
        self.wait_visibility_of_element_located(questions_locator)

    def wait_clickable_faq_questions(self, test_faq_sections):
        questions_locator = mpl.FAQ_QUESTIONS.get(test_faq_sections)
        self.wait_element_to_be_clickable(questions_locator)

    @allure.step('Получен текст вопроса')
    def get_questions_text(self, test_faq_sections):
        questions_locator = mpl.FAQ_QUESTIONS.get(test_faq_sections)
        return self.get_element_text(questions_locator)

    @allure.step('Клик на вопрос')
    def click_on_faq_questions(self, test_faq_sections):
        questions_locator = mpl.FAQ_QUESTIONS.get(test_faq_sections)
        self.click_on_element(questions_locator)

    def wait_visibility_faq_answer(self, test_faq_sections):
        answer_locator = mpl.FAQ_ANSWERS.get(test_faq_sections)
        self.wait_visibility_of_element_located(answer_locator)

    @allure.step('Получен текст ответа')
    def get_answer_text(self, test_faq_sections):
        answer_locator = mpl.FAQ_ANSWERS.get(test_faq_sections)
        return self.get_element_text(answer_locator)

    @allure.step('Клик по кнопке "Заказать" в шапке страницы')
    def click_on_order_button_header(self):
        self.wait_visibility_of_element_located(mpl.ORDER_BUTTON_IN_HEADER)
        self.wait_element_to_be_clickable(mpl.ORDER_BUTTON_IN_HEADER)
        self.click_on_element(mpl.ORDER_BUTTON_IN_HEADER)

    @allure.step('Клик по лого "Самокат"')
    def click_on_logo_scooter(self):
        self.wait_visibility_of_element_located(mpl.LOGO_SCOOTER_LINK)
        self.wait_element_to_be_clickable(mpl.LOGO_SCOOTER_LINK)
        self.click_on_element(mpl.LOGO_SCOOTER_LINK)

    @allure.step('Клик по лого "Яндекс"')
    def click_on_logo_yandex(self):
        self.wait_visibility_of_element_located(mpl.LOGO_YANDEX_LINK)
        self.wait_element_to_be_clickable(mpl.LOGO_YANDEX_LINK)
        self.click_on_element(mpl.LOGO_YANDEX_LINK)
        self.switch_to_next_tab()
        self.wait_url_to_be(data.DZEN_URL)

    @allure.step('Получен текущий URL')
    def get_url_page(self):
        return self.get_current_url()