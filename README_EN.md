# QA Automation: The Internet Herokuapp

Test task for QA Automation role.
Stack: **Python + Playwright + Pytest**.

## About

Autotests for [the-internet.herokuapp.com](https://the-internet.herokuapp.com).
PageObject pattern implemented.

Coverage:
*   Main Page (elements and links verification).
*   Login (positive and negative cases).
*   Secure Area (content check, logout).

## Local Run

1.  Setup:
    
    python -m venv venv
    venv\Scripts\activate


2.  Dependencies:

    pip install -r requirements.txt
    playwright install chromium


3.  **Run**:
    ```bash
    pytest
    ```
    
    To run with browser (headed):
    ```bash
    pytest --headed
    ```

    To change base URL:

    pytest --base-url http://another-url.com
