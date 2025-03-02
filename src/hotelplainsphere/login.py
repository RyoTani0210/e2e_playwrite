from playwright.sync_api import Page

class LoginPage:
    """
    ログイン画面のpageオブジェクト
    """
    def __init__(self, page: Page, testdata):
        self.page = page
        self.url = testdata["url"] + "/login.html"
        self.email_input_locator = "input[name='email']"
        self.password_input_locator = "input[name='password']"
        self.login_button_locator = "text=ログイン"
    
    def openpage(self):
        self.page.goto(self.url)
    
    def login(self, email: str, password: str):
        """
        ログイン操作
        """
        self.page.fill(self.email_input_locator, email)
        self.page.fill(self.password_input_locator, password)
        self.page.click(self.login_button_locator)
