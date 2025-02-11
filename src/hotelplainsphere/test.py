import pytest
from playwright.sync_api import Page

from toppage import HotelPlanispherePage  #`HotelPlanispherePage` クラスがあるファイルをimport


@pytest.mark.parametrize("button_name, click_method, expected_path", [
    ("home", "click_home", "index.html"),
    ("reservation", "click_reservation", "plans.html"),
    ("register", "click_register", "signup.html"),
    ("login", "click_login", "login.html")
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


