"""
多くのテストで使う共通設定ファイル
"""

import pytest

@pytest.fixture
def test_data():
    return {
        "url": "https://hotel-example-site.takeyaqa.dev/ja/index.html",
        "expected_title": "HOTEL PLANISPHERE - テスト自動化練習サイト",
        }
