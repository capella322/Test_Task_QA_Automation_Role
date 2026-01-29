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

1.  **Подготовка**:
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Linux/Mac
    source venv/bin/activate
    ```

2.  **Зависимости**:
    ```bash
    pip install -r requirements.txt
    playwright install chromium
    ```

3.  **Запуск**:
    ```bash
    pytest
    ```
    
    Для запуска в headless режиме (без браузера):
    ```bash
    pytest --headless
    ```

    Можно поменять базовый URL:
    ```bash
    pytest --base-url http://another-url.com
    ```

## CI/CD
Настроен GitHub Actions — тесты гоняются при каждом пуше в ветку.
