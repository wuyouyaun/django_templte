# 前端实现功能：根据接口返回的不同code值，判断支付的结果，给用户返回提示友好的信息
# 接口返回格式：
# {
#     "code": 0,
#     "msg": "success!",
#     "data": []
# }
#
# 错误码参照
# 0 - 成功
# 30000 - 参数错误
# 30001 - 余额不足
# 30002 - 达到当天最大额度
# 201102 - 银行卡被冻结


def pay_status(result):
    '''根据接口返回code状态，给用户提示对应的结果'''
    if result.get("code")==0:
        return "支付成功"
    elif result.get("code")==30000:
        return "支付失败: %s" % result.get("msg")
    elif result.get("code")==30001:
        return "支付失败: %s"% result.get("msg")
    elif result.get("code")==30002:
        return "支付失败: %s"% result.get("msg")
    elif result.get("code")==201102:
        return "支付失败: %s"% result.get("msg")
    else:
        return "支付失败:系统异常，未知错误"

if __name__=="__main__":
    result = {
            "code": 30000,
            "msg": "参数错误",
            "data": [],
            "id":"ewrere"
            }

    mm=pay_status(result)
    print(mm)