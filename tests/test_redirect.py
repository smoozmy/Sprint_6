import allure
from pages.main_page import MainPage
from src import data


class TestRedirectPages:

    @allure.title('Проверка перехода после клика по лого "Яндекс"')
    def test_redirect_dzen_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.wait_visibility_cookie()
        main_page.close_cookie_window()
        main_page.click_on_logo_yandex()
        current_url = main_page.get_url_page()

        assert data.DZEN_URL in current_url


    @allure.title('Проверка перехода после клика по лого "Самокат"')
    def test_redirect_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.wait_visibility_cookie()
        main_page.close_cookie_window()
        main_page.click_on_order_button_header()
        main_page.click_on_logo_scooter()
        current_url = main_page.get_url_page()

        assert data.BASE_URL in current_url

