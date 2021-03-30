import requests
from case.DF_project.df_testlogin import DF_Login
import os

from nb_log import LogManager
from nb_log_config import LOG_PATH

logger = LogManager("api").get_logger_and_add_handlers(is_add_stream_handler=True,
                                                       log_filename="api.log",
                                                       log_path=LOG_PATH
                                                        )

class commodity_information():
    '''
    商品模块信息
    '''
    def __init__(self,s):
        self.s=s


    def import_source_group(self):
        '''
        导入类目二级课组,通过导入进行新增
        :param s:
        :return:
        '''
        real_path=os.path.dirname(os.path.realpath(__file__))
        really_path=os.path.join(real_path,"catframeworklevel.xls")
        url = "https://testware-partner.dmall.com.hk/purchase/import"
        headers = {
            "Referer": "https://testpartner.dmall.com.hk/",
                     }
        f={

            "file":("catframeworklevel.xls",open(really_path,"rb"),"Content-Type: application/vnd.ms-excel")


        }

        r = self.s.post(url, headers=headers,files=f, verify=False)
        logger.debug("返回日志：%s" % r.json())
        return r.json()


    def get_query_ware(self,rfIds,skuIds,itemNums,sapTitle):
        '''
        商品管理列表查询
        :param s:
        :return:
        '''
        url = "https://testware-partner.dmall.com.hk//waremanager/queryware"
        headers = {
            "Referer": "https://testpartner.dmall.com.hk/",
            "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarymtihAXjI7bkLcUsc"
                   }
        body={
                "rfIds": rfIds,
                "skuIds": skuIds,
                "itemNums": itemNums,
                "sapTitle": sapTitle
                }

        r=self.s.post(url, data=body, headers=headers, verify=False)
        logger.debug("返回日志：%s" % r.json())
        return r.json()


    def add_commmodity(self):
        '''
        新增商品
        :param s:
        :return:
        '''

        url = "https://testware-partner.dmall.com.hk//wareInfo/addOrUpdate/add"
        headers = {
            "Origin": "https://testpartner.dmall.com.hk",
            "Referer": "https://testpartner.dmall.com.hk/",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
                   }

        body = {
                 "wareStr":'{"wareId":null,"rfId":"20111110","wareType":"PTSP","specType":"0","venderId":10039,'
                           '"basicInfo":{"sapTitle":"柬埔寨--红枣","produceArea":"测试","thirdCatId":"11341",'
                           '"weight":"0","matkl":"0010101","mwskz":"0.17","mwskzName":"1","unit":"EA","estiamteType":"1001",'
                           '"brandId":"28741","storageType":"1","wareLife":"","purchaseReceiveRadio":"","warningShelfLife":"",'
                           '"factorySite":"","telephone":"","canFillManufactureDate":"0","eattingType":"","materialDetail":"",'
                           '"specQty":"","specUnit":"","manufacturer":"","chine":"克"},"multiWareInfo":[],"warePackageInfo":'
                           '[{"warePackageUnit":"EA","warePackageRatio":1,"warePackageName":"克"}],"wareItemNumInfo":[{"packageUnit":'
                           '"EA","ratio":1,"wareItemNumEAN":"20111110","wareItemNumMain":1}],"delMultiWareInfoIds":[],"delWarePackageInfoIds":[],'
                           '"delWareItemNumInfoIds":[],"localeInfo":"{\'en_US\':\'{}\'}"}'
                    }

        r = self.s.post(url, data=body, headers=headers, verify=False)
        logger.debug("返回日志：%s" % r.json())
        return r.json()


    def select_commodity_info(self,rfId):
        '''                                   # 因新建的商品数据从es推送下来的，删除ware_ware库无法清除页面上数据
        查询商品信息接口
        :param s:  rfId(商品商家编码)  , venderId(商家id)
        :return:
        '''
        url = "https://testware-partner.dmall.com.hk//wareInfo/selectOne"
        headers = {
            "Referer": "https://testpartner.dmall.com.hk/",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
                   }
        body = {
                "rfId": rfId,
                "venderId": 10039

                }
        r=self.s.post(url, data=body, headers=headers, verify=False)
        logger.debug("返回日志：%s" % r.json())
        return r.json()


    def update_commodity_info(self):
        '''
        修改商品信息
        :return:
        '''

        url="https://testware-partner.dmall.com.hk//wareInfo/addOrUpdate/update"
        headers = {
            "Referer": "https://testpartner.dmall.com.hk/",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
                   }

        body={

            "wareStr": '{"wareId":101084188,"rfId":"20111110","wareType":"PTSP","specType":0,'
                       '"venderId":10039,"basicInfo":{"sapTitle":"柬埔寨--红枣","produceArea":"测试",'
                       '"thirdCatId":11341,"weight":"0","matkl":"0010101","mwskz":"0.17","mwskzName":"1",'
                       '"unit":"EA","estiamteType":"1001","brandId":28741,"storageType":1,"wareLife":"1",'
                       '"purchaseReceiveRadio":"11","warningShelfLife":"1","factorySite":"","telephone":"",'
                       '"canFillManufactureDate":0,"eattingType":"","materialDetail":"","specQty":"",'
                       '"specUnit":"","manufacturer":"","chine":"克"},"multiWareInfo":[],"warePackageInfo":'
                       '[{"id":2105932,"warePackageUnit":"EA","warePackageRatio":1,"warePackageWeight":null,'
                       '"warePackageLength":null,"warePackageWidth":null,"warePackageHeight":null,"warePackageCubage":null,'
                       '"warePackageName":"克"}],"wareItemNumInfo":[{"id":22161624,"packageUnit":"EA","ratio":1,'
                       '"wareItemNumEAN":"20111110","wareItemNumMain":1}],"delMultiWareInfoIds":[],"delWarePackageInfoIds":[],'
                       '"delWareItemNumInfoIds":[],"localeInfo":"{\'en_US\':\'{}\'}"}'}
        r=self.s.post(url, data=body, headers=headers, verify=False)
        print(r.json())
        logger.debug("返回日志： %s" % r.json())
        return r.json()


    def query_list_shelves(self,pageSize,currentPage,name,code,purchaseCatId):
        '''
        货架组列表查询
        :return:
        '''
        url="https://testware-partner.dmall.com.hk/shelfgrouplevel/query/list"
        headers = {
            "Referer": "https://testpartner.dmall.com.hk/",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
                   }

        body={
            "pageSize": pageSize,
            "currentPage": currentPage,
            "name":name,
            "code":code,
            "purchaseCatId":purchaseCatId
            }
        r = self.s.post(url, data=body, headers=headers, verify=False)
        logger.debug("返回日志： %s" % r.json())
        return r.json()


    def add_shelves(self,name):
        '''
        货架组新增
        :return:
        '''
        url = "https://testware-partner.dmall.com.hk/shelfgrouplevel/add"
        headers = {
            "Referer": "https://testpartner.dmall.com.hk/",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
                   }

        body = {
                "name": name,
                "code": "JPZ011",
                "venderId": "10039",
                "purchaseCatId": "859380",
                "repetition": "0",
                "localeInfo": "{'en_US':'{}'}"
                }
        r=self.s.post(url, data=body, headers=headers, verify=False)
        logger.debug("返回日志： %s" % r.json())
        return r.json()


    def delete_shelves(s):
        """
        货架组移除
        :return:
        """
        url="https://testware-partner.dmall.com.hk/shelfgrouplevel/delete/81"
        body={
            "": ""
        }
        headers={
            "Referer": "https://testpartner.dmall.com.hk/"
            }
        r = s.post(url, headers=headers, data=body, verify=False)
        print(r.json())
        logger.debug("返回日志： %s" % r.json())
        return r.json()


    def update_shelves(self,name,code,purchaseCatId,id):
        '''
        修改货架组信息
        :return:
        '''
        url="https://testware-partner.dmall.com.hk/shelfgrouplevel/update"
        headers = {
            "Referer": "https://testpartner.dmall.com.hk/",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
                   }

        body = {
                "name": name,
                "code": code,
                "venderId": "10039",
                "purchaseCatId": purchaseCatId,
                "repetition": "0",
                "id":id,
                "localeInfo": "{'en_US':'{}'}"
                }
        r=self.s.post(url, data=body, headers=headers, verify=False)
        logger.debug("返回日志： %s"% r.json())
        return r.json()

    def query_shelves(self):
        '''
        查看货架组信息
        :return:
        '''
        url="https://testware-partner.dmall.com.hk/shelfgrouplevel/query/77?_=1602776678508"
        headers={
            "Referer": "https://testpartner.dmall.com.hk/"
            }
        r=self.get(url, verify=False)
        logger.debug("返回日志： %s"% r.json())
        print(r.json())


    def query_shelfgrouplevel(s):
        '''
        货架组级门店管理列表查询
        :return:
        '''
        url="https://testware-partner.dmall.com.hk/shelfgrouplevel/query/list"
        body={
                "code": "",
                "name": "",
                "purchaseCatId": "",
                "pageSize": "10",
                "currentPage": "1"
                }
        headers = {
            "Referer": "https://testpartner.dmall.com.hk/",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
                   }

        r=s.post(url, data=body, headers=headers, verify=False)
        logger.debug("返回日志： %s"% r.json())


    def relate_shelfgrouplevel(self):
        '''
        关联门店
        :return:
        '''
        url = "https://testware-partner.dmall.com.hk/shelfgrouplevel/shop"
        body = {
                "id": "89",
                "code": "JPZ02",
                "name": "柬埔寨货架01",
                "venderId": "10039",
                "stores[0][code]": "107533",
                "stores[0][value]": "000001    柬埔寨门店01",
                "shops[0].id": "107533"

          }
        headers = {
            "Referer": "https://testpartner.dmall.com.hk/",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
                   }
        r = self.s.post(url, headers=headers, data=body, verify=False)
        logger.debug("返回日志： %s" % r.json())
        return r.json()


    def import_ware(self):
        '''
        货架组级--商品数据导入
        :return:
        '''

        real_path = os.path.dirname(os.path.realpath(__file__))
        print(real_path)

        cur_path = os.path.join(real_path, "shelfGroupLevelWare.xlsx")
        print(cur_path)

        url= "https://testware-partner.dmall.com.hk/shelfgrouplevel/importware"
        headers={
            "Referer": "https://testpartner.dmall.com.hk/"}
        f = {
           "file": ("shelfGroupLevelWare.xlsx", open(cur_path, "rb"), "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        }

        r=self.s.post(url, headers=headers, files=f, verify=False)
        logger.debug("返回日志：%s" % r.json())
        return r.json()





if __name__== "__main__":
    s = requests.session()
    DF_Login(s)
    # get_query_ware(s)
    # print("@@@@@@@@@@@@@@@@@---------",)
    # cc=commodity_information(s).import_source_group()
    # print("#@@@@@@@@@@@@@@@@@@@@@@@@@",cc)
    # print(cc['code'])
    #
    # commodity_information(s).add_shelves(name="柬埔寨货架11")
    # commodity_information(s).update_shelves(name="柬埔寨货架13",code="JPZ011",purchaseCatId="859380",id="98")
    commodity_information(s).import_ware()
