from pages.base_page import BasePage
from pages.order_page_locators import OrderPageLocators as opl
import allure

from src.data import BASE_URL, ORDER_PATH_URL

ORDER_PAGE_URL = BASE_URL + ORDER_PATH_URL

class OrderPage(BasePage):
    def __init__(self, driver):
      super().__init__(driver)

    def wait_visibility_cookie(self):
        cookie_locator = opl.COOKIE_BUTTON
        self.wait_visibility_of_element_located(cookie_locator)

    @allure.step('Окно Cookie закрыто')
    def close_cookie_window(self):
        self.click_on_element(opl.COOKIE_BUTTON)


    @allure.step('Заполнение первой страницы оформления заказа')
    def order_first_form(self, helpers):
        self.wait_visibility_of_element_located(opl.FIRST_NAME_FIELD)
        self.wait_element_to_be_clickable(opl.FIRST_NAME_FIELD)
        self.send_keys_field(opl.FIRST_NAME_FIELD, helpers[0])
        self.send_keys_field(opl.LAST_NAME_FIELD, helpers[1])
        self.send_keys_field(opl.ADDRESS_FIELD, helpers[2])
        self.click_on_element(opl.METRO_FIELD)
        self.send_keys_field(opl.METRO_FIELD, helpers[3])
        self.click_on_element(opl.METRO_LIST)
        self.send_keys_field(opl.PHONE_NUMBER_FIELD, helpers[4])
        self.click_on_element(opl.CONTINUE_BUTTON)



    @allure.step('Заполнение второй страницы оформления заказа')
    def order_second_form(self, helpers):
        self.wait_visibility_of_element_located(opl.SCOOTER_DATE_DELIVERY_FIELD)
        self.wait_element_to_be_clickable(opl.SCOOTER_DATE_DELIVERY_FIELD)
        self.send_keys_field(opl.SCOOTER_DATE_DELIVERY_FIELD, helpers[5])
        self.click_on_element(opl.CLICK_BODY_PAGE)

        self.click_on_element(opl.SCOOTER_RENTAL_PERIOD)
        self.click_on_element(opl.SCOOTER_RENTAL_PERIOD_DAYS)

        self.send_keys_field(opl.COMMENT_FIELD, helpers[6])

        self.wait_element_to_be_clickable(opl.CREATE_ORDER_BUTTON)
        self.click_on_element(opl.CREATE_ORDER_BUTTON)

        self.wait_element_to_be_clickable(opl.YES_ORDER_BUTTON)
        self.click_on_element(opl.YES_ORDER_BUTTON)

    @allure.step('Получение текста кнопки "Посмотреть статус"')
    def get_button_status_text(self):
        self.wait_visibility_of_element_located(opl.VIEW_STATUS_BUTTON)
        return self.get_element_text(opl.VIEW_STATUS_BUTTON)