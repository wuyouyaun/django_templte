
import re
import requests


def login_test(s):
    url="http://49.235.92.12:7001/xadmin/"
    headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
            }
    r=s.get(url,verify=False)
    print(r.text)
    csrfmiddlewaretokens=re.findall(r"name='csrfmiddlewaretoken' value='(.+?)' ",r.text)
    print(type(csrfmiddlewaretokens))
    print(csrfmiddlewaretokens[0])
    csrfmiddlewaretoken=csrfmiddlewaretokens[0]
    body={
          "csrfmiddlewaretoken":csrfmiddlewaretoken,
          "username":"admin",
          "password":"yoyo123456",
          "this_is_the_login_form":"1",
          "next":"/xadmin/"
    }
    print("#########",body)
    r=s.post(url,data=body,verify=False)
    print(r.text)

def add_student():
    url="http://49.235.92.12:7001/xadmin/hello/student/add/"
    body={
         "csrfmiddlewaretoken":"DLBfBlXxerxabaFi8qfQoSQRmPGqBpvgr8or8S5NPSdDsYzPXyMFq1rsGJ1zjzIv",
         "csrfmiddlewaretoken":"DLBfBlXxerxabaFi8qfQoSQRmPGqBpvgr8or8S5NPSdDsYzPXyMFq1rsGJ1zjzIv",
         "student_id":"2121",
        "name":"测试1",
        "gender":"M",
        "age":"12",
        "_save":""
    }



if __name__=="__main__":
    s=requests.session()
    login_test(s)

