# Импорт библиотеки вебдрайвера
from selenium import webdriver
#импорт библиотеки времени, для ожидания прогрузки страницы
import time
#Импорт библиотеки By
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys

#-----------------инициализация библиотеки для firefox-------------
from selenium.webdriver.firefox.options import Options
#-----------------инициализация библиотеки для firefox-------------
#-----------------Использование Jenkins в headless режиме (без графического интерфейса)----------------
options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
#-----------------Использование Jenkins в headless режиме (без графического интерфейса)----------------

link = "https://webtucre.ru/testovaya-stranicza-6/"
browser = webdriver.Firefox()
browser.get(link)
# Строка поиска=serch_string
search_string = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div/main/article/div/div/div/section[2]/div/div[1]/div/div/div/form/div/input")
#Ввод поискового запроса в строку поиска
search_string.send_keys("QA228")
#Кнопка поиска
knopka = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div/main/article/div/div/div/section[2]/div/div[1]/div/div/div/form/div/button")
#Клик по кнопке поиска
knopka.click()
time.sleep(2)
#Проверка того что мы действительно нашли то что искали
proverka = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[1]/main/div/article[1]/div/div/header/h2").text
#Вывод сообщения о найденом элементе
print(proverka)
# Проверяем раздел на существующее название (Мы взяли переменную=proverka1 со словом "тестирование"
# и взяли обычную переменную=proverka, которая ищет наш запрос и берет оттуда просто текст=.text
# и мы говорим, давайте сравним в цикле if и else и выведем на экран соответствующие надписи)
proverka1 = "QA228"
if proverka == proverka1:
    print("Тест прошел успешно")
else:
    print("Тест проверку не прошел")
#Закрываем открытые окна браузера после теста
browser.quit()
