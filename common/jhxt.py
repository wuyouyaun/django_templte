
import requests
import urllib3
urllib3.disable_warnings()
import time
mm=int(round(time.time()*1000))
print("dssssssssssssss",mm)
cc=str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))[0:13]
print(cc)

def order_pick(s):
    url="https://open.dmall.com.hk/app/login"
    header={
            "appTypeEnum":"2",
            "userAccountType":"2",
            "loginType":"1",
            "overLayFlag":"2",
            "platform":"ANDROID"

    }
    body={
           "param":'{"agreements":[{"agreementId":3,"version":1.0}],"checkType":"1","device":"samsung SM-N9600 QP1A.190711.020.N9600ZHS5ETG3 unknown","deviceType":"1","isAgreementFlag":-1,"loginIp":"1","loginTime":1610086648619,"password":"edaf57ee618c2a6786165a6ff11fff2e7c220218e164d07a8c87d905ddf3c4c0","platform":"ANDROID","sysVersion":"Android-10","userName":"00380704","version":"1.1.0"}'
         }
    r=s.post(url,headers=header,data=body,verify=False)
    kk=r.json()['data']['token']
    print(kk)
    return r.json()['data']['token']


def person_info(s):
    url="https://open.dmall.com.hk/app/proxy"
    headers={
        "interfaceCode": "dmall_push_service-GexinAliasService-forceBindAlias",
        "Content-Type": "application/x-www-form-urlencoded",
        "appCode": "peisong",
        "versionName": "1.1.0",
        "platform": "ANDROID",
        "sysVersion": "Android-10",
        "appTypeEnum": "2",
        "loginType": "1",
        "token":order_pick(s),
        "userAccountType": "2",
        "User-Agent":"okhttp/3.12.0",
        "X-Ca-Signature":"DQbAVl7IlloXWVsrNSJkER9cWlST2v4QIZMsfRJQObZTU3meUxpqiuFVsuKEg5JzRMFJmJkfyOgr%0Au2UbybQrdLgjN1MD9vSFcrG%2BzEvnGy2P4C4jILPMegyQalewczHOYEt3sM6%2BkC1xKoin094ieOiS%0ATvNb8GfXjICpbH4REJWIaNxlL0KUOwgn0P37H19T2GXop3w3JQd4Cw%2FPFEiH2ALn6jcuiB0%2FMleF%0AK9u2bNrYYf06e7gtFJ22XcBRHu0CjZ%2BEzmU5BYOCMHrK1pGJJJm8zsKbZLwyzAC0jYF3uPsAXlkr%0AJrX0F%2FKSMr2CPFlwmJ9AH4wBCM9MyA4U%2B1UNLA%3D%3D%0A",
        "X-Ca-Timestamp": "%s"%int(round(time.time()*1000))



    }
    print(headers)

    body={
        "param":'{"alias":"698415","appId":2,"clientId":"8b6bb692c6af6c921e2c41df2bc0de5e","deliveryId":698415,"deliveryName":"Vincky Huang","processTime":1610091736572,"token":"c25dca75-5f70-42b4-a035-9c9189681f1220210108154216","userId":698415}'
        }
    r=s.post(url,headers=headers,data=body,verify=False)
    print(r.json())
    # print(s.headers)
    c=r.json()
    return r.json()






if __name__=="__main__":
    s=requests.session()
    order_pick(s)
    person_info(s)


