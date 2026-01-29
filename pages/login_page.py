from pages.base_page import BasePage

class LoginPage(BasePage):
    def login(self, user, password):
        self.find("#username").fill(user)
        self.find("#password").fill(password)
        self.find("button[type='submit']").click()

    def error_message(self):
        return self.find("#flash").inner_text()
