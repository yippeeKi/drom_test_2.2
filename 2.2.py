# импортируем нужные методы
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
chrome_options = Options()

# оборачиваем всё глобально в try - except
# если что-то пойдет не так, то тест всегда будет считаться проваленным
try:
    driver.get("https://auto.drom.ru/")
    driver.delete_all_cookies()
    # chrome_options.addArgument("--user-data-dir=C:\Users\malec\AppData\Local\Google\Chrome\User Data")

    auth_form = driver.find_element(By.CLASS_NAME, "css-1h9spzo")
    auth_form.click()

# всегда ждем 20 секунд, пока не найдем элемент строки ввода логина
# в противном случае считаем, что нарвались на капчу
# пока нашел только решение отключить капчу вручную за эти 20 секунд
    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "sign"))
        )
    except:
        print("it's a captcha!!!")

# обрабатываем нужные кнопки, добавив свои данные для авторизации
    form_login = driver.find_element(By.ID, "sign")
    form_login.send_keys("79039**3546")
    form_password = driver.find_element(By.ID, "password")
    form_password.send_keys("DromTest****")
    sign_button = driver.find_element(By.ID, "signbutton")
    sign_button.click()
    cars_slide = driver.find_element(By.CLASS_NAME, "flicking-camera")
    cars_slide.click()

# если авто уже в избранном, то нужно обработать другой класс css, поэтому добавляем его в исключение
# таким образом мы будем удалять из избранного автомобиль
    try:
        favorite_cars = driver.find_element(By.CLASS_NAME, "css-1b2zlcs")
        favorite_cars.click()

    except:
        favorite_cars_full = driver.find_element(By.CLASS_NAME, "css-1fw5pgf")
        favorite_cars_full.click()
    driver.implicitly_wait(5)
    print('successful test')

except:
    print("failed test")
