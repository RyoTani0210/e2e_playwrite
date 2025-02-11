import pytest
from playwright.sync_api import Page


def test_example(page: Page, test_data):
    """
    example.comのタイトルがあっているか確認する
    """
    page.goto(test_data["url"])
    page.pause()
    assert page.title() == test_data["expected_title"]
    