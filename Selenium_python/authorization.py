#Импорт модуля time для работы с задержками
import time
# Импорт необходимых модулей Selenium для работы с Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
# Импорт webdriver-manager для автоматической установки драйвера Chrome последней версии
from webdriver_manager.chrome import ChromeDriverManager


def open_browser(driver): #Открытие сайта указанным браузером
    try:
        base_url = 'https://www.saucedemo.com/' # Базовый URL тестового сайта SauceDemo
        driver.get(base_url) # Переход на указанную страницу в браузере
        # Установка размера окна браузера в разрешение 1920x1080 (FHD)
        driver.set_window_size(1920, 1080)
        time.sleep(1) # Задержка перед выполнением следующей команды
    except Exception as e:
        print(f"Ошибка при работе с браузером: {e}") # Вывод ошибки в случае её возникновения
        driver.close() # Закрытие сайта


def close_browser(driver): #Закрытие сайта указанным браузером
    time.sleep(5) # Задержка перед выполнением следующей команды
    driver.close() # Закрытие сайта


def fill_in_the_fields(driver): # Заполнение полей Login и Password
    # Получение ссылки на элемент (поле) ввода имени пользователя по его локатору
    user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
    # Установка значения имени пользователя в поле ввода имени пользователя
    user_name.send_keys('standard_user')
    time.sleep(2) # Задержка перед выполнением следующей команды
    # получение ссылки на элемент (поле) ввода пароля пользователя по его локатору
    user_password = driver.find_element(By.XPATH, "//input[@id='password']")
    # Установка значения пароля пользователя в поле ввода пароля
    user_password.send_keys('secret_sauce')
    time.sleep(2) # Задержка перед выполнением следующей команды


def click_login_button(driver): # Нажатие кнопки Login
    # получение ссылки на кнопку авторизации Login
    login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
    login_button.click() # Нажатие на кнопку


def main(): # Основная программа
    # Получение web драйвера браузера Chrome
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    open_browser(driver) # Открытие сайта
    fill_in_the_fields(driver) # Заполнение полей
    click_login_button(driver)  # Нажатие кнопки авторизации (Login)
    close_browser(driver) # Закрытие браузера


if __name__ == '__main__':
    main()