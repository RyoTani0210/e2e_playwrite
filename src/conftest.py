"""
多くのテストで使う共通設定ファイル
"""

import pytest

@pytest.fixture
def test_data():
    return {
        "url": "https://example.com",
        "expected_title": "Example Domain",
        }
