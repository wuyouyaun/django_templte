import requests







# s=requests.session()
# url="http://10.40.2.32:8898/api/login/"
# headers={
#          "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
#          }
# body={
#     "account":"admin",
#     "password":"123456a"
#
#     }
# r=s.post(url,headers=headers,data=body,verify=False)
# print(r.text)
# print(s.cookies)
import random
# random=random.randint(9999001,9999050)
# for i in random:
#     print(i)
# randoms=random.randint(9999001,9999050)
# print(randoms)


# def supplier_code():
#     random=random.randint(9999001,9999050)
#     print(random)
#     return random
#     # for i in random:
#     #     return i

s=requests.session()
print("访问网页前的",s.cookies)
url="https://www.baidu.com"
r=s.get(url)
print("访问网页后的",s.cookies)
















