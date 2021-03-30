import requests



# def login(s):
#
#     url="http://8.129.172.40/zentaopms/www/user-login.html"
#     body={
#         "account":"wuyy",
#         "password":"Wuyy123",
#         "keepLogin[]":"on",
#         "referer":""
#         }
#     r=s.post(url,data=body,verify=False)
#     print(r.text)
#
# if __name__=="__main__":
#     s=requests.session()
#     login(s)


import yaml

with open("demo_list.yml","r",encoding="utf-8") as fp:
    b=fp.read()
    print(b)
    print(type(b))
c=yaml.load(b,Loader=yaml.FullLoader)
print(c)
print(type(c))


