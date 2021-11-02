# Автоматизированные тесты 
## О проекте 
Тесты реализованы с нуля на python с использованием библиотеки Selenium и браузера Google Chrome.

Для того чтобы тесты запустились необходимо импортировать меттоды:
webdriver; By; Keys; Select

URL = http://qa-assignment.oblakogroup.ru/board/svetlana_shironina


В DR_ADRESS записываем путь к драйверу на ПК

Test Suite состоит из 5 тестов:


1 test_word_wrap;


2 test_space_task;


3 test_add_object_in_category;


4 test_space_heading;


5 test_existing_title.

## О тестах
test_word_wrap - проверяет наличие автоматического переноса текста, написанного слитно.


test_space_task - проверяет возможность создания задачи, с заполнением поля 'Название задачи' пробелами.


test_add_object_in_category - проверяет попадёт ли в нужную категорию добавленная задача.


test_space_heading - проверяет возможность создания задачи с незаполненным полем 'Заголовок'.


test_existing_title - проверяет требование: Если пользователь добавляет новую запись в новую 
категорию, но вводит название существующей, то запись добавляется в существующую.
    
  

