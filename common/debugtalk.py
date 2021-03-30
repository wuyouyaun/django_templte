
import requests
import os

def login_info(loginName="admin",loginPassword="Dmall@1234"):
    s=requests.session()
    url="http://testdf-vc-basemanage.dmall.com.hk/retails"
    headers={
              "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
              "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36" \
                            "(KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
              "Referer": "http://testdf-vc.dmall.com.hk"
            }
    body={
              "loginName": loginName,
              "loginPassword": loginPassword,
              "retailId": ""
    }
    r=s.post(url,data=body,headers=headers,verify=False)
    print(r.json())
    c=r.json()['data'][0]['value']
    print(c)
    return r.json()['data'][0]['value']

def db_connect():
    db=pymysql.connect( host="10.40.2.23",
                        port=5707,
                        user="my_user_5707",
                        password="my_user_5707@df&",
                        db="df_vc_basemanage_supplier"
                        )
    return db

def select_sql(db,sql):
    '''
    查询
    :param sql:
    :return:
    '''
    db=db_connect()
    cur=db.cursor()
    cur.execute(sql)
    data=cur.fetchall()
    print(data)



def delete_db(sql_delete):
    db=db_connect()
    cur = db.cursor()
    try:
        cur.execute(sql_delete)   # 执行
        db.commit()              # 提交
    except Exception as e:
        print("操作异常: %s" % str(e))
        # 错误回滚
        db.rollback()
    finally:
        db.close()



def get_file(filePath="供商公司導入模板 (5).xls"):
    path = os.path.dirname(os.path.realpath(__file__))
    real_path = os.path.join(path, filePath)
    print(real_path)
    c=open(real_path, "rb")
    print(c)
    return c





if __name__=="__main__":
    # token=login_info()
    # print(token)
    # delete_db(sql_delete="delete  from cx_company where company_name='深圳大源源呐942';")
    get_file(filePath="供商公司導入模板 (5).xls")