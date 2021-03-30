# coding:utf-8
import requests
import pytest
from case.DF_project.df_testlogin import DF_Login
from nb_log import LogManager
from nb_log_config import LOG_PATH
import json
import os
import random
import shutil
from case.VC_project.connect_mysql import db_connect,delete_db

logger = LogManager("api").get_logger_and_add_handlers(is_add_stream_handler=True,
                                                       log_filename="api.log",
                                                       log_path=LOG_PATH

                                                        )
def delete_register():
    ''' 执行删除公司信息操作  '''
    sql = "delete  from cx_company where company_name='深圳大源源呐939';"
    delete_db(db=db_connect(), sql_delete=sql)
    print("1111")
    print("后置操作")





# companyName公司名称不能為空    'basicAccount': '銀行基本戶帳號不能為空', 'taxpayerNumber': '納稅識別號不能為空' 'bankAccountName': '銀行開戶名不能為空'
def save_supplier_information(s, taxpayerType="Z1", companyName="深圳大源源呐939", legalPeople="大源源",
                                    companyAddress="2222", taxpayerNumber="111111111111111", bankCode="1111111111",
                                    simpleName="11111", basicAccount="11111111111",
                                    bankName="建行",bankAccountName="建行西丽分行"):

    '''
    新增公司信息档案               #  taxpayerType 纳税类型    # companyName  公司名称   #  legalPeople 法人   # companyAddress 公司地址
                                   #   taxpayerNumber 纳税人识别号    # bankCode 支行联行号  # simpleName  公司简称  # 公司联系人和公司联系人手机号非空
    :return: r                     #   basicAccount   银行账号     # bankName 开户银行   #  bankAccountName  開戶銀行名
    '''

    data = {"taxpayerType": taxpayerType, "companyName": companyName, "legalPeople": legalPeople,
            "companyAddress": companyAddress, "taxpayerNumber": taxpayerNumber, "bankCode": bankCode,
            "simpleName": simpleName, "basicAccount": basicAccount,
            "bankName": bankName, "bankAccountName": bankAccountName, "mainName": "22222", "mainPhone": "18571519920"}

    datas = json.dumps(data)       # 将字典转换成json

    url = "https://testdf-vc-supplier.dmall.com.hk/cx/company/save"
    headers = {"Referer": "https://testpartner.dmall.com.hk/"}
    body = {
          "form_data": datas

            }
    r = s.post(url, data=body, headers=headers, verify=False)
    logger.debug("返回日志：%s" % r.json())
    return r.json()


def check_supplier_information(s):
    '''
    公司信息档案详情
    :param s: id
    :return: r.json()
    '''
    delete_register()
    common = save_supplier_information(s)['data']
    data = {"id": common}
    datas = str(data)
    body11 = datas.replace(" ", "")
    print("---------", body11)

    body12 = eval(body11)         # 先将字符串转换成字典
    dataes = json.dumps(body12)     # 将字典转换成json格式
    print(type(dataes))
    url = "https://testdf-vc-supplier.dmall.com.hk/cx/company/details"
    header = {
            "Referer": "https://testpartner.dmall.com.hk/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            "Origin": "https://testpartner.dmall.com.hk",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"

        }
    body = {
            "form_data": dataes
            }

    print("123456",body)
    r = s.post(url, headers=header, data=body, verify=False)
    logger.debug("返回日志：%s" % r.json())
    return r.json()


def update_supplier_infor(s, taxpayerType = "Z1", companyName = "深圳大源源呐990", legalPeople = "大源源",
                            companyAddress="2222", taxpayerNumber="111111111111111", bankCode="1111111111",
                            simpleName="11111", basicAccount="11111111111", bankName="建行",
                            bankAccountName="建行西丽分行", mainName="22222", mainPhone="18571519920"):
    '''
    修改公司信息
    '''
# "createdStr": "2020-10-22 19:52:02","modifiedStr": "2020-10-22 19:52:02",
    ids = save_supplier_information(s)['data']   # 新增公司信息返回的id
    print(ids)
    data = {
            "taxpayerType": taxpayerType,
            "companyName": companyName, "legalPeople": legalPeople,
            "companyAddress": companyAddress, "taxpayerNumber": taxpayerNumber, "bankCode": bankCode,
            "simpleName": simpleName, "basicAccount": basicAccount,
            "bankName": bankName, "bankAccountName": bankAccountName,
            "mainName": mainName, "mainPhone": mainPhone,
            "id": ids, "isUpdate": "I", "companyType": "1", "manageMode": 1,
            "groupNo": "GH000172", "martCode": "dfhk",
            "statusStr": "正常", "companyTypeStr": "商品類供應商",
            "manageModeName": "制造商", "taxpayerTypeName": "壹般納稅人(0;9%;13%)", "source": 2,
            "status": 3, "ynDesc": "有效", "venderId": 10032, "lastOptUser": "有源[Dd00631483]",
            "createdStr": "" + "2020-10-22 19:52:02", "modifiedStr": "" + " 2020-10-22 19:52:02",
            "created": 1603367522000, "yn": 1, "modified": "1603367522000"
             }

    print("@@@@@@@@@@@@@@  ----", data)
    bodys = json.dumps(data)
    print("######## ----- ----", bodys)
    body1 = bodys.replace(" ", "")
    print("111111", body1)
    url = "https://testdf-vc-supplier.dmall.com.hk/cx/company/update"
    headers = {"Referer": "https://testpartner.dmall.com.hk/"}
    body = {

        "form_data": body1

        }

    print("----------", body)
    print(type(body))
    r = s.post(url, headers=headers, data=body, verify=False)
    logger.debug("返回日志：%s" % r.json())
    return r.json()


def supplier_loadown_template(s):
    '''
    公司档案信息模板下载
    :param s:
    :return:
    '''
    url = "https://testdf-vc-supplier.dmall.com.hk/cx/company/template"
    headers = {
            "Referer": "https://testpartner.dmall.com.hk/"
                }
    r = s.get(url, headers=headers, verify=False)
    logger.debug("返回日志: %s" % r)
    print (r.text)
    # return r
    # print("124345")
    # path = os.path.dirname(os.path.realpath(__file__))
    # print(path)
    # real_path = os.path.join(path, "供商公司導入模板.xls")
    # print(real_path)
    # # if os.path.exists(real_path):
    # #     shutil.rmtree(real_path)
    # fp = open("供商公司導入模板.xls", "wb")
    # fp.write(r.content)
    # fp.close()
    return r.text
    # return r.text


def import_company(s, name="供商公司導入模板 (5).xls"):
    '''
    公司档案信息模板导入
    :return:
    '''
    # name = name
    url = "https://testdf-vc-supplier.dmall.com.hk/cx/company/import"
    headers = {
                "Referer": "https://testpartner.dmall.com.hk/"

                }
    path = os.path.dirname(os.path.realpath(__file__))
    real_path = os.path.join(path, name)
    f = {
        "file": (name, open(real_path, "rb"), "Content-Type: application/vnd.ms-excel")
    }
    r = s.post(url, headers=headers, files=f, verify=False)
    logger.debug("返回日志: %s" % r.json())
    print(r.json())
    return r.json()


def find_supplier_infor(s, pageSize="20", currentPage="1", companyName="深圳大源源呐939"):
    '''
    查询公司信息列表接口
    :return:
    '''
    form_data = {"pageSize": pageSize, "currentPage": currentPage, "companyName": companyName}
    form_datas = json.dumps(form_data)
    url="https://testdf-vc-supplier.dmall.com.hk/cx/company/find"
    headers = {"Referer": "https://testpartner.dmall.com.hk/"}
    body = {
            "form_data": form_datas
        }

    r = s.post(url, data=body, headers=headers, verify=False)
    logger.debug("返回日志：%s" % r.json())
    return r.json()


def find_account_list(s, pageSize="20", currentPage="1", supplierName="深圳大源源呐939" ):
    '''
    账号管理列表查询
    :return:                                        #   还有查询条件
    '''
    form_data = {"pageSize": pageSize, "currentPage": currentPage, "supplierName": supplierName}
    form_datas = json.dumps(form_data)
    url = "https://testdf-vc-supplier.dmall.com.hk/cx/account/find"
    headers = {"Referer": "https://testpartner.dmall.com.hk/"}
    body = {
            "form_data": form_datas

        }
    r = s.post(url, data=body, headers=headers, verify=False)
    logger.debug("返回日志：%s" % r.json())
    return r.json()


def find_account_cards(s):
    '''
    查看账号卡号详情
    :return:
    '''
    account_card = find_supplier_infor(s)
    account_cards = account_card['data']['list'][0]['groupNo']
    card = {"supplierAccount": account_cards, "pageSize": 20, "currentPage": 1}
    print("@@@@@@@@", card)
    cards = json.dumps(card)     # 将字典转换成json
    url = "https://testdf-vc-supplier.dmall.com.hk/cx/supplier/find"
    headers = {"Referer": "https://testpartner.dmall.com.hk/"}
    body = {

        "form_data": cards
        }
    r = s.post(url, headers=headers, data=body, verify=False)
    logger.debug("返回日志：%s" % r.json())
    return r.json()


def update_account_information(s, mobile="18571519920", contacts="2" , email="353558733@qq.com",status=2):
    '''
    修改账号信息（校验手机号，邮箱及启用状态）     #cx_supplier_account
    :return:r.json
    '''                                            # status 启用状态 1.禁用 2.启用
    account_card = find_supplier_infor(s)
    account_cards = account_card['data']['list'][0]['groupNo']
    form_list = {"mainAccount": account_cards, "supplierAccount": account_cards,
                  "mobile": mobile, "supplierName": "深圳大源源呐939", "accountType": 1,
                  "contacts": contacts, "email": email, "companyId": 10820, "supplierGroup": "GH000089",
                  "sourceName": "来客", "accountTypeDesc": "管理賬號（壹級賬號）", "statusStr": "正常", "source": 2, "status": status, "id": 4437,
                  "martCode": "dfkh", "venderId": 10039, "lastOptUser": "大源源呗[Dd00631484]", "created": 1602567391000, "yn": 1,
                  "ynDesc": "有效", "createdStr": "2020-10-13 13:36:31", "modifiedStr": "2020-10-13 14:18:31"}
    print("#####", 124344)
    print(form_list)
    form_data = json.dumps(form_list)
    print("-------------  %s" % form_data)
    url = "https://testdf-vc-supplier.dmall.com.hk/cx/account/update"
    headers = {"Referer": "https://testpartner.dmall.com.hk/"}
    body = {
           "form_data": form_data
                        }
    r = s.post(url, data=json.dumps(body), headers=headers, verify=False)
    logger.debug("返回日志：%s" % r.json())
    return r.json()


def account_resetPWD(s,supplierAccount="supplierAccount", contactsPhone="contactsPhone"):
    '''
    账号重置密码
    :return:                # 1.先调用公司信息接口  2.再调用账号管理接口
    '''
    # account_reset = find_supplier_infor(s)
    # account_resets = account_reset['data']['list'][0]['groupNo']
    # account_list = find_account_list(s, pageSize="20", currentPage="1", supplierName="深圳大源源呐939")
    # print(account_list['data']['list'][0]['mobile'])
    # account_lists = account_list['data']['list'][0]['mobile']
    account = {"martCode": "dfkh", "supplierAccount": supplierAccount, "contactsPhone": contactsPhone}
    form_account = json.dumps(account)
    url = "https://testdf-vc-supplier.dmall.com.hk/cx/account/resetPWD"
    headers = {"Referer": "https://testpartner.dmall.com.hk/"
               }
    body = {
            "form_data": form_account
            }
    r = s.post(url, data=body, headers=headers, verify=False)
    logger.debug("返回日志：%s" % r.json())
    return r.json()


class Add_supplier_card():
    ''' 卡号管理 '''
    def __init__(self, s):
        self.s = s

    def card_list(self):
        """
        卡号管理列表查询
        :return:r.json()
        """
        url = "https://testdf-vc-supplier.dmall.com.hk/cx/supplier/find"
        headers = {"Referer": "https://testpartner.dmall.com.hk/"}
        body = {
            "form_data": '{"currentPage":1,"pageSize":20}'
            }
        r = self.s.post(url, data=body, headers=headers, verify=False)
        logger.debug("返回日志：%s" % r.json())
        return r.json()


    def get_companys(self,supplier_hk):
        '''
        通过公司姓名获取供商账号
        '''

        # kk = check_supplier_information(s=self.s)    # 公司信息档案详情
        # print("@##@#@#@#@##@#@#",kk)
        # supplier_hk = kk['data']['accountList'][0]['companyId']
        # print("########",supplier_hk)
        get_supplier ={"id":supplier_hk}
        get_suppliers=json.dumps(get_supplier)
        url = "https://testdf-vc-supplier.dmall.com.hk/cx/company/get"
        headers = {"Referer": "https://testpartner.dmall.com.hk/"}
        body={ "form_data": get_suppliers }
        r=self.s.post(url, data=body, headers=headers, verify=False)
        logger.debug("返回日志: %s" % r.json())
        return r.json()

        # cx_supplier
    def add_supplier_cards(self,supplierFullName="深圳大源源呐939",businessType="1",supplierType="1",supplierStatus="1",
                             returnSupplier="1",contacts="22222",contactsPhone="18571519920",remark="",bizType="TO_C",
                             supplierCode="777778",supplierShortName="11111",taxType="Z1",
                             purchaseGroup="1002",plannedDeliveryTime="1",minOrderAmount="0",orderCalendar="23",
                             manualPriceRevision="1",autoConfirmOrders="0",settleCompany="10039",payType="1",
                             drawer="",settlePeriod="2",settleMethod="2",accountPeriodStartDay="0",accountPeriod="30",
                             grossProfitCompensate="2",paymentFreeze="0",generateZeroSettleSheet="0",checkStock="0",
                             checkCost="0"
                             ):
        """                    # supplierFullName 公司名称   # supplierAccount 供商账号  # businessType 经营类型  # supplierType 供商类型
        新增供应商卡号         # supplierStatus 供商状态  # returnSupplier 退货供应商  # contacts 联系人 # contactsPhone  联系电话
                               # bizType 供应商服务类型   # supplierCode 供商卡号 # supplierShortName 公司简称 # taxType 税类型
                               # supplierGroup 供商组号
                               # remark  备注   # purchaseGroup 采购组   # plannedDeliveryTime 計劃交貨天數 # minOrderAmount 最小订货金额
                               # orderCalendar 訂貨日歷   # manualPriceRevision 允许手工改价 # autoConfirmOrders 自动确认订单
                               # settleCompany 结算公司  #  payType 付款方式（枚举类） # drawer 出票方 # settlePeriod 结算周期 # settleMethod 结算方式
                               # accountPeriodStartDay 账单起算日 # accountPeriod 账期 # grossProfitCompensate 毛利补偿 # paymentFreeze 付款凍結
                               # generateZeroSettleSheet 生成0元結算單 # checkStock 考核库存 # checkCost 考核费用
        """
        kk = check_supplier_information(s=self.s)    # 公司信息档案详情
        print("@##@#@#@#@##@#@#",kk)
        supplier_hk = kk['data']['accountList'][0]['companyId']
        supplierAccounts = self.get_companys(supplier_hk)
        print("****************--------",supplierAccounts)
        supplierAccount=supplierAccounts['data']['groupNo']
        print("*****", supplierAccount)
        supplierGroup="GH"+str(random.randint(9990, 9999))
        companyid=find_account_list(s=self.s)     # 账号信息查询查出companyid
        companyId=companyid['data']['list'][0]['companyId']
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%***************',companyId)
        supplier_infor={
                        "supplierFullName":supplierFullName,"supplierAccount":supplierAccount,"businessType":businessType,"supplierType":supplierType,
                        "supplierStatus":supplierStatus,"returnSupplier":returnSupplier,"contacts":contacts,"contactsPhone":contactsPhone,
                        "remark":remark,"bizType":bizType,"supplierCode":supplierCode,"supplierShortName":supplierShortName,"taxType":taxType,
                        "supplierGroup":supplierGroup,"plannedDeliveryTime":plannedDeliveryTime,"minOrderAmount":minOrderAmount,
                        "orderCalendar":orderCalendar,"manualPriceRevision":manualPriceRevision,"autoConfirmOrders":autoConfirmOrders,
                        "settleCompany":settleCompany,"payType":payType,"drawer":drawer,"settlePeriod":settlePeriod,"settleMethod":settleMethod,
                        "accountPeriodStartDay":accountPeriodStartDay,"accountPeriod":accountPeriod,"grossProfitCompensate":grossProfitCompensate,
                        "paymentFreeze":paymentFreeze,"generateZeroSettleSheet":generateZeroSettleSheet,"checkStock":checkStock,"checkCost":checkCost,
                        "purchaseGroup":'1002',"companyId":companyId,"email":"353558733@qq.com","configers":[]
                        }

        print("---------",supplier_infor)
        supplier_infors=json.dumps(supplier_infor)
        print("kkkkkkkkkkk",supplier_infor)
        url = "https://testdf-vc-supplier.dmall.com.hk/cx/supplier/add"
        headers = {
                "Referer": "https://testpartner.dmall.com.hk/",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"

                    }
        body = {
                "form_data":supplier_infors
        }
        print("!!!!!!!!!!!!!!!!!----------",body)
        r = self.s.post(url, data=body, headers=headers, verify=False)
        logger.debug("返回日志：%s" % r.json())
        return r.json()



    def approve_supplier_card(self,source_id,status):
        '''
        卡号审批     status：2.同意 4.驳回
        :return:
        '''
        changing={"supplierCode":source_id,"status":status,"rejectCause":"同意","martCode":"dfkh"}
        changing_id=json.dumps(changing)
        url = "https://testdf-vc-supplier.dmall.com.hk/cx/supplier/approve"
        headers = {
            "Referer": "https://testpartner.dmall.com.hk/",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"

                }
        body = {
            "form_data": changing_id
            }
        r = self.s.post(url, data=body, headers=headers, verify=False)
        logger.debug("返回日志：%s" % r.json())
        return r.json()


if __name__ == "__main__":
    s = requests.session()
    df_login = DF_Login(s)
    # save_supplier_information(s)
    # cc= Add_supplier_card(s)

    # check_supplier_information(s)
    # kk = check_supplier_information(s)    # 公司信息档案详情
    # print("@##@#@#@#@##@#@#",kk)
    # supplier_hk = kk['data']['accountList'][0]['companyId']
    # print("########",supplier_hk)
    # Add_supplier_card(s).get_companys(supplier_hk)
    # Add_supplier_card(s).add_supplier_cards(supplierFullName="深圳大源源呐939",businessType="1",supplierType="1",supplierStatus="1",
    #                                         returnSupplier="1",contacts="22222",contactsPhone="18571519920",remark="",bizType="TO_C",
    #                                         supplierCode="9999910",supplierShortName="11111",taxType="Z1",
    #                                         plannedDeliveryTime="1",minOrderAmount="0",orderCalendar="23",
    #                                         manualPriceRevision="1",autoConfirmOrders="0",settleCompany="10039",payType="1",
    #                                         drawer="",settlePeriod="2",settleMethod="2",accountPeriodStartDay="0",accountPeriod="30",
    #                                         grossProfitCompensate="2",paymentFreeze="0",generateZeroSettleSheet="0",checkStock="0",
    #                                         checkCost="0"
    #                        )
    #
    # Add_supplier_card(s).approve_supplier_card(source_id='9999014',status='4')
    # save_supplier_information(s, taxpayerType="Z1", companyName="", legalPeople="大源源",
    #                                 companyAddress="2222", taxpayerNumber="111111111111111", bankCode="1111111111",
    #                                 simpleName="11111", basicAccount="11111111111",
    #                                 bankName="建行",bankAccountName="建行西丽分行")
    # supplier_loadown_template(s)
    Add_supplier_card(s).add_supplier_cards(supplierFullName="深圳大源源呐939",businessType="1",supplierType="1",supplierStatus="1",
                             returnSupplier="1",contacts="22222",contactsPhone="18571519920",remark="",bizType="TO_C",
                             supplierCode="777778",supplierShortName="11111",taxType="Z1",
                             purchaseGroup="1002",plannedDeliveryTime="1",minOrderAmount="0",orderCalendar="23",
                             manualPriceRevision="1",autoConfirmOrders="0",settleCompany="10039",payType="1",
                             drawer="",settlePeriod="2",settleMethod="2",accountPeriodStartDay="0",accountPeriod="30",
                             grossProfitCompensate="2",paymentFreeze="0",generateZeroSettleSheet="0",checkStock="0",
                             checkCost="0"
                             )




