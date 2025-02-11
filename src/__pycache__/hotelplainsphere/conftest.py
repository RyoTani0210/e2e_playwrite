"""
多くのテストで使う共通設定ファイル
"""

import pytest

@pytest.fixture
def test_data():
    return {
        "url": "https://hotel-example-site.takeyaqa.dev/ja/",
        "users":{
            "one":{#プレミアム会員
                "email": "ichiro@example.com",
                "password": "password",
            },
            "two":{#一般会員
                "email": "sakura@example.com",
                "password": "pass1234",
            },
            "three":{#プレミアム会員
                "email": "jun@example.com",
                "password": "pa55w0rd!",
            },
            "four":{#一般会員
                "email": "yoshiki@example.com",
                "password": "pass-pass",
            },
        }
        }
