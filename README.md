# QA Automation: The Internet Herokuapp

Тестовое задание на позицию QA Automation.
Стек: **Python + Playwright + Pytest**.

## О проекте

Автотесты для [the-internet.herokuapp.com](https://the-internet.herokuapp.com).
Реализован паттерн PageObject.

Покрытие:
*   Главная страница (проверка элементов, ссылок).
*   Логин (позитивные и негативные кейсы).
*   Личный кабинет (проверка контента, логаут).

## Запуск локально

1.  Подготовка:

    python -m venv venv
    venv\Scripts\activate


2.  Зависимости:

    pip install -r requirements.txt
    playwright install chromium


3.  **Запуск**:
    ```bash
    pytest
    ```
    
    Для запуска с браузером (headed):
    ```bash
    pytest --headed
    ```

    Можно поменять базовый URL:

    pytest --base-url http://another-url.com


