from playwright.sync_api import Page
class HotelPlanispherePage:
    """
    トップページのpageオブジェクト
    """
    def __init__(self, Page, test_data):
        self.page = Page
        self.url = test_data["url"] + "/index.html"
        self.home_button = "text=ホーム"
        self.reservation_button = "text=宿泊予約"
        self.register_button = "text=会員登録"
        self.login_button = "text=ログイン"
        self.notice_button = "text=お知らせ"

    def open_page(self):
        """ページを開く"""
        self.page.goto(self.url)
    
    def is_home_button_clickable(self):
        """ホームボタンがクリックできる状態か確認"""
        return self.page.is_visible(self.home_button) and self.page.is_enabled(self.home_button)


    def click_home(self):
        """ホームボタンをクリックする"""
        self.page.click(self.home_button)

    def click_reservation(self):
        """宿泊予約ボタンをクリックする"""
        self.page.click(self.reservation_button)

    def click_register(self):
        """会員登録ボタンをクリックする"""
        self.page.click(self.register_button)

    def click_login(self):
        """ログインボタンをクリックする"""
        self.page.click(self.login_button)

    def click_notice(self):
        """お知らせボタンをクリックする"""
        self.page.click(self.notice_button)