#Импорт модуля time для работы с задержками
import time
# Импорт необходимых модулей Selenium для работы с Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
# Импорт webdriver-manager для автоматической установки драйвера Chrome последней версии
from webdriver_manager.chrome import ChromeDriverManager


CONFIG = {
    'base_url': 'https://www.saucedemo.com/',
    'window_size': (1920, 1080),
    'credentials': {
        'standard_user': {'login': 'standard_user', 'password': 'secret_sauce'}
    }
}


LOCATORS = {
    'login_page': {
        'username': (By.XPATH, "//input[@id='user-name']"),
        'password': (By.XPATH, "//input[@id='password']"),
        'login_button': (By.XPATH, "//input[@id='login-button']")
    }
}


def open_browser(driver): #Открытие сайта указанным браузером
    # Переход на указанную страницу в браузере
    driver.get(CONFIG.get('base_url'))
    # Установка размера окна браузера в разрешение 1920x1080 (FHD)
    driver.set_window_size(*CONFIG.get('window_size'))


def close_browser(driver): #Закрытие сайта указанным браузером
    #Закрытие сайта
    driver.close()


def fill_in_the_fields(driver, locator, field_value):
    # Получение ссылки на элемент (поле) ввода по его локатору
    user_name = driver.find_element(*locator)
    # Установка значения в поле
    user_name.send_keys(field_value)
    # Задержка перед выполнением следующей команды
    time.sleep(2)


def click_login_button(driver, locator): # Нажатие кнопки Login
    # получение ссылки на кнопку авторизации Login
    login_button = driver.find_element(*locator)
    login_button.click() # Нажатие на кнопку
    time.sleep(2)


def main(): #Основная программа
    # получение web драйвера браузера Chrome
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    open_browser(driver) #Открытие сайта
    # Заполнение поля логина
    fill_in_the_fields(
        driver,
        LOCATORS.get('login_page')['username'],
        CONFIG.get('credentials')['standard_user']['login']
    )
    # Заполнение поля пароля
    fill_in_the_fields(
        driver,
        LOCATORS.get('login_page')['password'],
        CONFIG.get('credentials')['standard_user']['password']
    )
    # Нажатие на кнопку Login
    click_login_button(
        driver,
        LOCATORS.get('login_page')['login_button']
    )
    close_browser(driver) #Закрытие браузера


if __name__ == '__main__':
    main()