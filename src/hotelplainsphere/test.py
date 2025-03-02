import pytest
from playwright.sync_api import Page

from toppage import HotelPlanispherePage
from login import LoginPage


@pytest.mark.parametrize("button_name, click_method, expected_path", [
    ("home", "click_home", "/index.html"),
    ("reservation", "click_reservation", "/plans.html"),
    ("register", "click_register", "/signup.html"),
    ("login", "click_login", "/login.html")
])
def test_all_buttons_navigation(page: Page, test_data, button_name, click_method, expected_path):
    """
    すべてのボタンをクリックした後のURLが期待値と一致するか確認（パラメータ化）
    """
    # 準備
    hotel_page = HotelPlanispherePage(page, test_data)
    hotel_page.open_page()

    # ボタンをクリック（`getattr` を使って動的にメソッドを呼び出す）
    getattr(hotel_page, click_method)()

    # 遷移後のURLを検証
    expected_url = test_data["url"] + expected_path
    assert page.url == expected_url


@pytest.mark.parametrize("email, password, expected", [
    ("ichiro@example.com", "password", True),#ログイン成功
    ("sakura@example.com", "pass1234", True),#ログイン成功
    ("ichiro@example.com", "passw0rd", False) #ログイン失敗
])
def test_auth(page: Page, test_data, email, password, expected):
    """
    ログイン機能のテスト
    """

    # 準備
    # browser =page.chronium.launch(headerless=False)
    login_page = LoginPage(page, test_data)
    login_page.openpage()

    # ログイン
    login_page.login(email, password)

    # 結果確認
    # page.wait_for_timeout(10*1000) #デバック用。10秒まつ
    is_mypage = page.url == test_data["url"] + "/mypage.html"
    
    assert is_mypage == expected
