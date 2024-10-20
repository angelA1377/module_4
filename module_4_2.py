# Домашняя работа по уроку "Пространство имен."
# Домашнее задание по уроку "Пространство имен"
#
# Создайте новый проект в PyCharm
# Запустите созданный проект
# Ваша задача:
# Создайте новую функцию test_function
# Создайте внутри test_function другую функцию - inner_function, Эта функция должна печатать значение "Я в области видимости функции test_function"
# Вызовите функцию inner_function внутри функции test_function
# Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы
# Файл с кодом module_4_2.py загрузите на GitHub репозиторий и пришлите ссылку на него.


def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


# Вызовем test_function
test_function()

# Попробуем вызвать inner_function вне test_function
try:
    inner_function()
except NameError as e:
    print(f"Ошибка: {e}")