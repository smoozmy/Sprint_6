from selenium.webdriver.common.by import By


class MainPageLocators():
    ORDER_BUTTON_IN_HEADER = (By.XPATH, "//button[contains(@class, 'Button_Button')]")
    LOGO_YANDEX_LINK = (By.XPATH, ".//a[contains(@class, 'Header_LogoYandex')]")
    LOGO_SCOOTER_LINK = (By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]")
    COOKIE_BUTTON = (By.XPATH, "//button[@id='rcc-confirm-button']")
    FAQ_SECTION = (By.XPATH, ".//div[contains(@class, 'Home_FAQ')]")

    FAQ_QUESTIONS = {
        1: [By.ID, "accordion__heading-0"],
        2: [By.ID, "accordion__heading-1"],
        3: [By.ID, "accordion__heading-2"],
        4: [By.ID, "accordion__heading-3"],
        5: [By.ID, "accordion__heading-4"],
        6: [By.ID, "accordion__heading-5"],
        7: [By.ID, "accordion__heading-6"],
        8: [By.ID, "accordion__heading-7"]
    }

    FAQ_ANSWERS = {
        1: [By.ID, "accordion__panel-0"],
        2: [By.ID, "accordion__panel-1"],
        3: [By.ID, "accordion__panel-2"],
        4: [By.ID, "accordion__panel-3"],
        5: [By.ID, "accordion__panel-4"],
        6: [By.ID, "accordion__panel-5"],
        7: [By.ID, "accordion__panel-6"],
        8: [By.ID, "accordion__panel-7"]
    }

