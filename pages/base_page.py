from playwright.sync_api import Page, Locator

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def find(self, selector: str) -> Locator:
        return self.page.locator(selector)
    
    @property
    def title(self) -> str:
        return self.page.title()
