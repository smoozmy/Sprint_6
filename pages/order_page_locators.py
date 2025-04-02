from selenium.webdriver.common.by import By


class OrderPageLocators:
    FIRST_NAME_FIELD = (By.XPATH, ".//input[@placeholder='* Имя']")
    LAST_NAME_FIELD = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    METRO_LIST = (By.XPATH, ".//li[@class='select-search__row']")
    PHONE_NUMBER_FIELD = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    CONTINUE_BUTTON = (By.XPATH, './/button[text()="Далее"]')

    SCOOTER_DATE_DELIVERY_FIELD = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    SCOOTER_RENTAL_PERIOD = (By.XPATH, ".//div[text()='* Срок аренды']")
    SCOOTER_RENTAL_PERIOD_DAYS = (By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() ='трое суток']")
    COMMENT_FIELD = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button')
    CREATE_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")
    YES_ORDER_BUTTON = (By.XPATH, ".//button[text()='Да']")
    VIEW_STATUS_BUTTON = (By.XPATH, ".//button[text()='Посмотреть статус']")

    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')
    CLICK_BODY_PAGE = (By.TAG_NAME, "body")