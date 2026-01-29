from pages.base_page import BasePage

class MainPage(BasePage):
    def fork_me_icon(self):
        return self.find("img[alt='Fork me on GitHub']")

    def all_links(self):
        return self.find("a")

    def click_auth_link(self):
        self.find("a[href='/login']").click()
