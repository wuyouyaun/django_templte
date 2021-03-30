

import requests


def znw_login(s):
    url="http://seedtest.ap-ec.cn/SSO-SERVER/authentication/form"
    body={"username":"zhaolei","password":"123456a","imageCode":"fcgc","deviceid":"8f9d4da4-3038-425c-b24c-33120573c6d3","loginType":"json","days":7,"aesKey":"","aesIv":""}
    r=s.post(url,json=body,verify=False)
    print(r.json())
    mm=r.json()
    print(mm["data"]['tokenInfo']['token'])
    return r

if  __name__=="__main__":
    s=requests.session()
    znw_login(s)
