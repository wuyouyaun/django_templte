# from ke16.form_data_xadmin import add_teacher_name
# from ke12.connet_mysql import select_sql,execute_sql
# import pytest
#
#
# # 前置操作：先清空数据
# @pytest.fixture(scope="function")
# def delete_teacher():
#     sql = "DELETE FROM djangoweb.hello_teacher WHERE teacher_name = 'yoyo333';"
#     execute_sql(sql)
#     yield
#     print("数据清理的操作")
#
#
#
# def test_add_teacher(login_xmain, delete_teacher):
#     # 新增数据
#     s =login_xmain
#     text = add_teacher_name(s)
#     # 查询数据库结果
#     sql = "SELECT count(*) as sum from djangoweb.hello_teacher WHERE teacher_name = 'yoyo333'"
#     result1 = select_sql(sql)[0]["sum"]
#     # 校验结果
#     assert result1 == 1

import random

# cc=str(random.randint(1000, 9999))
# MM="GH"+cc
# print(cc)
# print(type(cc))
# print(MM)
# print((type(MM)))
import json

# body='({"name":null})'
# print(body)
# print(eval(body))
# bodys=json.dumps(body)
# bodyss=json.loads(body)
# print(type(bodyss))
# print(type(body))




















#
# # python基础数据类型
# a=None      #None
# print(a)
#
# b=False         #bool
# print(b)
# print(type(b))
#
# c,d=8,12.7     #int ,float
# print(c)
# print(d)
#
# f=[1,2,4,23,34,3]   #list
# print(f)
#
# p=(1,3,2,54,"fds")  # tuple
# print(p)
#
# kk={                # dict
#     "a":"233",
#     "b":"yww"
# }
# print(kk)
#
#
# # ks="ewwr"
# kk['ks']="ewwr"
# print(kk)





# params={"12","23","cba"}   # 集合
# print(type(params))
#
#
# a1=set("12andfd")   #集合
# print("ceshi")
# print(a1)
# print(type(a1))
#
#
#
#
#
#
bb1={
    "a":"123",
    "b":"234",
    "dsf":"wyy"
    }
# bb1["g"]="xxx"     # 增
# print(bb1)
# del(bb1['a'])     #删
# print(bb1)
#
# bb1["b"]="110"    # 该
# print(bb1)
#
# print(bb1["dsf"])   #查
# print(bb1.get("dsf"))
#
#
#
#
# test={
#         "name":"wyy",
#         "mail":"353558733@qq.com",
#         "tel":"18571519920",
#         "age":"23"
#         }
# c=test.values()   # dict_values(['wyy', '353558733@qq.com', '18571519920', '23'])
# print(c)
# print(test.keys()) # dict_keys(['name', 'mail', 'tel', 'age'])
# print(test.items()) # dict_items([('name', 'wyy'), ('mail', '353558733@qq.com'), ('tel', '18571519920'), ('age', '23')])
#
# #字典遍历取值
# for key,values in test.items():
#     print(key,values)
#
# ll_li={
#        "token":"122",
#         "sign":"qqqq"
#         }
# # 更新到字典a中
# test.update(ll_li)
# print(test)  # {'name': 'wyy', 'mail': '353558733@qq.com', 'tel': '18571519920', 'age': '23', 'token': '122', 'sign': 'qqqq'}
#
#
#
#
# import json
# dls={
#     "a":"23432",
#     "b":"rerer",
#     "c":"434232",
#     "d":"12223",
#     }
# print(type(dls))
# js=json.dumps(dls)     # dict 转 json ，需要用到dump函数
# print(js)
# print(type(js))
#
# # json 转字典
# ls=json.loads(js)
# print(ls)
#
# #字典转字符串
# ld=str(dls)
# print(ld)
# print(type(ld))
#
# #字符串转字典  用eval函数
# ldd=eval(ld)
# print(ldd)
# print(type(ldd))
#
# import random
# # random.
#
#
# print(r.text())
# print(r.json())


# ff="{"mainAccount": account_cards, "supplierAccount": account_cards,
#                   "mobile": mobile, "supplierName": "深圳大源源呐939", "accountType": 1,
#                   "contacts": contacts, "email": email, "companyId": 10820, "supplierGroup": "GH000089",
#                   "sourceName": "来客", "accountTypeDesc": "管理賬號（壹級賬號）", "statusStr": "正常", "source": 2, "status": status, "id": 4437,
#                   "martCode": "dfkh", "venderId": 10039, "lastOptUser": "大源源呗[Dd00631484]", "created": 1602567391000, "yn": 1,
#                   "ynDesc": "有效", "createdStr": "2020-10-13 13:36:31", "modifiedStr": "2020-10-13 14:18:31"}"
#
# print(str(ff))


# print(a)











import re
import json

# result={
#     "code":"0",
#     "data":[
#         {
#         "age":"32",
#         "time":"2019-12-12",
#         "id":"1",
#         "sex":"1"
#         },
#         {
#         "age":"12",
#         "time":"2019-12-12",
#         "id":"2",
#         "sex":"4"
#          }],
#         "message":"success"
#         }
# result_to_json=json.dumps(result)
# res=re.findall("",result_to_json) #正则从json中提取



# print(dir(__builtins__))
#
# print(dir())
#
# import os
# # aa=os.path.dirname(path)
# # print(aa)
#
# bb=os.path.dirname(os.path.realpath(__file__))
# print(bb)











# import pytest
# @pytest.mark.paramtrize("x",[1,2])
# @pytest.mark.paramtrize("y",[4,2,7])
# def test_op(x,y):
#     print("测试数据组合：x ->%s, y ->%s"%(x,y))
#
#
#
#
# if __name__=="__main__":
#     pytest.main(["-s","ll_list.py"])













# 交换
a="hello"
b="world"

# 1.中间变量

# temp=a
# print(temp)
#
# a=b
# print(a,b)
# b=temp
# print(a,b)

# 2.pythonic
a,b=b,a

print(a,b)



a="abcba"
#1.切片，前闭后开

print(a[:2:1])

print(a[:2:-1])

a1=[1,2,3,4,5,6,7,8,9]
print(a1[6::-1])
print(a1[6:])
print(a1[-1:-6:-1])











