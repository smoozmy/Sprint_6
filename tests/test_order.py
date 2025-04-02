import allure
import pytest
from pages.main_page import MainPage
from pages.main_page_locators import MainPageLocators
from pages.order_page import OrderPage, ORDER_PAGE_URL
from pages.order_page_locators import OrderPageLocators
from src import data


class TestOrder:

    @allure.title('Оформление заказа на доставку')
    @pytest.mark.parametrize('button, generation_user', [
        (MainPageLocators.ORDER_BUTTON_IN_HEADER, data.USER_1),
        (OrderPageLocators.ORDER_BUTTON, data.USER_2)
    ])
    def test_placing_an_order(self, driver, button, generation_user):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open_main_page()
        main_page.wait_visibility_cookie()
        main_page.close_cookie_window()
        main_page.scroll_to_element(button)
        main_page.wait_element_to_be_clickable(button)
        main_page.click_on_element(button)

        current_url = main_page.get_url_page()
        assert ORDER_PAGE_URL in current_url

        order_page.order_first_form(generation_user)
        order_page.order_second_form(generation_user)
        status = order_page.get_button_status_text()

        assert 'Посмотреть статус' in status