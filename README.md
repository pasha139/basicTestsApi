# Basic Tests API — Swagger Petstore

Автотесты для демонстрационного API [Swagger Petstore](https://petstore.swagger.io/v2).
Покрывают три группы эндпоинтов: **Pet**, **Store**, **User**.

## Стек

- **Python 3.14**
- **pytest** — тестовый фреймворк
- **requests** — HTTP-клиент
- **pydantic** — валидация и сериализация моделей

## Как запустить

# 1. Клонировать репозиторий и перейти в него
git clone https://github.com/pasha139/basicTestsApi.git

cd basicTestsApi


# 2. Создать виртуальное окружение
python3 -m venv venv

source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows


# 3. Установить зависимости
pip install -r requirements.txt

# Запуск всех тестов
## все тесты
pytest

## с подробным выводом
pytest -v

## конкретный файл
pytest tests/test_pet.py

## конкретный тест
pytest tests/test_pet.py::test_pet_create

только упавшие в прошлый раз
pytest --lf

остановиться на первой ошибке
pytest -x

## показать 5 самых медленных тестов
pytest --durations=5
