from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

URL = 'http://qa-assignment.oblakogroup.ru/board/svetlana_shironina'
DR_ADRESS = 'C:/Users/Sveta/Desktop/Test/chromedriver.exe'
driver = webdriver.Chrome(DR_ADRESS)


def test_word_wrap():
    """Проверяем наличие автоматического переноса текста,
    написанного слитно.
    """
    driver.get(URL)
    driver.find_element(By.ID, 'add_new_todo').click()
    find_text = driver.find_element(By.ID, 'project_text')
    find_text.send_keys(Keys.CONTROL, 'a')
    find_text.send_keys('ПереносСловаНаДругуюСтрочку'*5)
    driver.find_element(By.ID, 'submit_add_todo').click()


def test_space_task():
    """Проверяем возможность создания задачи, с заполнением
    поля 'Название задачи' пробелами.
    """
    driver.get(URL)
    driver.find_element(By.ID, 'add_new_todo').click()
    find_text = driver.find_element(By.ID, 'project_text')
    find_text.send_keys(Keys.CONTROL, 'a')
    find_text.send_keys('                ')
    driver.find_element(By.ID, 'submit_add_todo').click()


def test_add_object_in_category():
    """Проверяем попадёт ли в нужную категорию добавленная задача"""
    driver.get(URL)
    driver.find_element(By.ID, 'add_new_todo').click()
    select = Select(driver.find_element(By.ID, 'select_category'))
    select.select_by_visible_text('Прочее')
    find_text = driver.find_element(By.ID, 'project_text')
    find_text.send_keys(Keys.CONTROL, 'a')
    find_text.send_keys('Hello world!')
    driver.find_element(By.ID, 'submit_add_todo').click()


def test_space_heading():
    """Проверяем возможность создания задачи с незаполненным
    полем 'Заголовок'."""
    driver.get(URL)
    driver.find_element(By.ID, 'add_new_todo').click()
    select = Select(driver.find_element(By.ID, 'select_category'))
    select.select_by_visible_text('Создать новый список')
    """Поле 'Заголовок' оставляем пустым."""
    find_text = driver.find_element(By.ID, 'project_text')
    find_text.send_keys(Keys.CONTROL, 'a')
    find_text.send_keys('Кошачий корм')
    driver.find_element(By.ID, 'submit_add_todo').click()


def test_existing_title():
    """Проверяем требование: Если пользователь добавляет
    новую запись в новую категорию, но вводит название
    существующей, то запись добавляется в существующую.
    """
    driver.get(URL)
    driver.find_element(By.ID, 'add_new_todo').click()
    select = Select(driver.find_element(By.ID, 'select_category'))
    select.select_by_visible_text('Создать новый список')
    heading = driver.find_element(By.ID, 'project_title')
    heading.send_keys(Keys.CONTROL, 'a')
    heading.send_keys('Отдых')
    find_text = driver.find_element(By.ID, 'project_text')
    find_text.send_keys(Keys.CONTROL, 'a')
    find_text.send_keys('Купальник')
    driver.find_element(By.ID, 'submit_add_todo').click()
    driver.find_element(By.ID, 'add_new_todo').click()
    select = Select(driver.find_element(By.ID, 'select_category'))
    select.select_by_visible_text('Создать новый список')
    heading = driver.find_element(By.ID, 'project_title')
    heading.send_keys(Keys.CONTROL, 'a')
    heading.send_keys('Отдых')
    find_text = driver.find_element(By.ID, 'project_text')
    find_text.send_keys(Keys.CONTROL, 'a')
    find_text.send_keys('Надувной круг')
    driver.find_element(By.ID, 'submit_add_todo').click()
    driver.close()
