


import requests

from pytest_demo_cov.src.pay_list import pay_status


def test_pay_success():
    result = {
            "code": 0,
            "msg": "支付成功",
            "data": []
        }
    pay_status(result)
