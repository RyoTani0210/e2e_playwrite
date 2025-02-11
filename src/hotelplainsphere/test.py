import pytest
from playwright.sync_api import Page

from toppage import HotelPlanispherePage  #`HotelPlanispherePage` クラスがあるファイルをimport


def test_all_buttons_navigation(page: Page, test_data):
    """
    すべてのボタンをクリックした後のURLが期待値と一致するか確認
    """

    #準備
    hotel_page = HotelPlanispherePage(page, test_data)
    hotel_page.open_page()

    # ホーム
    hotel_page.click_home()
    assert page.url == test_data["url"] + "index.html"

    # 宿泊予約
    hotel_page.click_reservation()
    assert page.url == test_data["url"] + "plans.html"

    # 会員登録
    hotel_page.click_register()
    assert page.url == test_data["url"] + "signup.html"

    # ログイン
    hotel_page.click_login()
    assert page.url == test_data["url"] + "login.html"

    


