from playwright.sync_api import Page

class MyPage:
    def __init__(self, page: Page, testdata):
        self.page = page
        self.url = testdata["url"] + "/mypage.html"
        self.email_locator = "text=メールアドレス"
        self.name_locator = "text=氏名"
        self.rank_locator = "text=会員ランク"
        self.address_locator = "text=住所"
        self.phone_locator = "text=電話番号"
        self.gender_locator = "text=性別"
        self.birthday_locator = "text=生年月日"
        self.newsletter_locator = "text=お知らせ"
        self.icon_setting_locator = "text=アイコン設定"
        self.withdraw_locator = "text=退会する"
        self.logout_button_locator = "text=ログアウト"
    
    def navigate(self):
        self.page.goto("https://hotel-example-site.takeyaqa.dev/ja/mypage.html")
    
    def get_user_info(self):
        """
        ユーザ情報取得
        """
        return {
            "email": self.page.text_content(self.email_locator + " + *"),
            "name": self.page.text_content(self.name_locator + " + *"),
            "rank": self.page.text_content(self.rank_locator + " + *"),
            "address": self.page.text_content(self.address_locator + " + *"),
            "phone": self.page.text_content(self.phone_locator + " + *"),
            "gender": self.page.text_content(self.gender_locator + " + *"),
            "birthday": self.page.text_content(self.birthday_locator + " + *")
        }
    
    def toggle_newsletter(self):
        self.page.click(self.newsletter_locator + " + input")
    
    def open_icon_settings(self):
        self.page.click(self.icon_setting_locator)
    
    def click_withdraw(self):
        """
        退会ボタンを押す
        """
        self.page.click(self.withdraw_locator)

    def logout(self):
        """
        ログアウトボタンを押す
        """
        self.page.click(self)