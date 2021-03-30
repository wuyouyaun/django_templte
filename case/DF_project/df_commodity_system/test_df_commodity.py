import pytest
import requests
import allure
from case.DF_project.df_commodity_system.conftest import delete_cat_level,delete_shelfgrouplevel,delete__ware
from case.DF_project.df_commodity_system.commodity_demo import commodity_information
from case.DF_project.conftest import df_login_xadmin
from case.DF_project.df_testlogin import DF_Login

'''
@allure.severity按严重性级别来标记case　　　
执行指定测试用例 --allure-severities blocker
BLOCKER = 'blocker'　　阻塞缺陷
CRITICAL = 'critical'　严重缺陷
NORMAL = 'normal'　　  一般缺陷
MINOR = 'minor'　　    次要缺陷
TRIVIAL = 'trivial'　　轻微缺陷　
'''


class TestClass_list:
    '''
    商品信息用例
    '''
    @allure.title("验证导入功能的有效性")
    @allure.story("新增商品类目组")
    @allure.severity("normal")
    def test_import_commodity_01(self,df_login_xadmin):

        with allure.step("step1 :登录"):
            s = df_login_xadmin
            DF_Login(s)
        with allure.step("step2 :进入到商品系统-品类管理页"):
            pass
        with allure.step("step3 :点击导入功能按钮，选择要上传的文件"):
            import_group=commodity_information(s).import_source_group()
        with allure.step("step4 :断言"):
            assert import_group['code'] == 'success'
            assert import_group['data'] == None



    test_data=[
        ({"rfIds":"866673","skuIds":"","itemNums":"","sapTitle":""},{'code': 'success', 'result': '操作成功'},"1.输入商家商品编码，验证查询的有效性"),
        ({"rfIds":"","skuIds":"101495123","itemNums":"","sapTitle":""},{'code': 'success', 'result': '操作成功'},"2.输入商品sku，验证查询的有效性"),
        ({"rfIds":"","skuIds":"","itemNums":"111100003434","sapTitle":""},{'code': 'success', 'result': '操作成功'},"2.输入国际条码，验证查询的有效性"),
        ({"rfIds":"","skuIds":"","itemNums":"","sapTitle":"柬埔寨鸡中翅"},{'code': 'success', 'result': '操作成功'},"2.输入商品名称，验证查询的有效性")
        ]

    @allure.story("商品信息")
    @allure.title("{title}")
    @pytest.mark.parametrize("test_input,expected,title",
                             test_data
                             )
    @allure.severity("normal")
    def test_get_query_02(self,df_login_xadmin,test_input,expected,title):
        with allure.step("step1 :登录"):
            s = df_login_xadmin
            DF_Login(s)
        with allure.step("step2 :进入到商品系统列表页"):
            pass
        with allure.step("step3 :输入商家商品编码，点击查询"):
            result=commodity_information(s).get_query_ware(test_input["rfIds"],test_input["skuIds"],test_input["itemNums"],test_input["sapTitle"])
        with allure.step("step4 :断言"):
            assert result['result']==expected['result']

    @allure.story("商品信息")
    @allure.title("验证新增商品功能有效性")
    @allure.severity("blocker")
    def test_add_commmodity_03(self,df_login_xadmin):
        with allure.step("step1 :登录"):
            s = df_login_xadmin
            DF_Login(s)
        with allure.step("step2 :进入到商品系统管理"):
            pass
        with allure.step("step3 :点击新增商品按钮"):
            result=commodity_information(s).add_commmodity()
        with allure.step("step4 :断言"):
            assert result['result']=='商品20111110系統內已存在'


    @allure.story("商品信息")
    @allure.title("验证查看商品信息功能有效性")
    @allure.severity("blocker")
    def select_commodity_info_04(self):
        with allure.step("step1 :登录"):
            s = df_login_xadmin
            DF_Login(s)
        with allure.step("step2 :进入到商品系统管理"):
            pass
        with allure.step("step3: 新增商品后，点击查询该商品的查看功能键"):
            result=commodity_information(s).select_commodity_info(rfId=20111110)
            assert result['code']=='success'
            assert result['result']=='操作成功'


    @allure.story("修改商品信息")
    @allure.title("验证修改商品信息功能有效性")
    @allure.severity("normal")
    def test_update_commodity_05(self,df_login_xadmin):
        with allure.step("step1 :登录"):
            s = df_login_xadmin
            DF_Login(s)
        with allure.step("step2 :进入到商品系统管理"):
            pass
        with allure.step("step3: 新增商品后，点击修改商品"):
            result=commodity_information(s).update_commodity_info()
        with allure.step("step4: 断言"):
            assert result['result']=='操作成功'
            assert result['data']==None

    test_datas=[
        ({"pageSize":"10","currentPage":"1","name":"","code":"","purchaseCatId":""},{'code': 'success', 'result': '操作成功'},"1.验证查询页码为1，页面数量为10，查询功能的有效性"),
        ({"pageSize":"30","currentPage":"1","name":"","code":"","purchaseCatId":""},{'code': 'success', 'result': '操作成功'},"2.验证查询页码为1，页面数量为30，查询功能的有效性"),
        ({"pageSize":"60","currentPage":"1","name":"","code":"","purchaseCatId":""},{'code': 'success', 'result': '操作成功'},"3.验证查询页码为1，页面数量为60，查询功能的有效性"),
        ({"pageSize":"100","currentPage":"1","name":"","code":"","purchaseCatId":""},{'code': 'success', 'result': '操作成功'},"4.验证查询页码为1，页面数量为100，查询功能的有效性"),
        ({"pageSize":"10","currentPage":"2","name":"","code":"","purchaseCatId":""},{'code': 'success', 'result': '操作成功'},"5.验证查询页码为2，页面数量为10，查询功能的有效性"),
        ({"pageSize":"10","currentPage":"1","name":"柬埔寨货架01","code":"","purchaseCatId":""},{'code': 'success', 'result': '操作成功'},"6.验证查询货架组名称为“柬埔寨货架01”功能的有效性"),
        ({"pageSize":"10","currentPage":"1","name":"","code":"JPZ01","purchaseCatId":""},{'code': 'success', 'result': '操作成功'},"7.验证查询货架组级编码为“JPZ01”功能的有效性"),
        ({"pageSize":"10","currentPage":"1","name":"","code":"","purchaseCatId":"753912"},{'code': 'success', 'result': '操作成功'},"8.验证查询采购项目为“753912（新鲜水果）”功能的有效性"),
        ({"pageSize":"10","currentPage":"1","name":"水果部","code":"hj001","purchaseCatId":"859380"},{'code': 'success', 'result': '操作成功'},"9.验证查询组合编码和名称或类目（同于一条数据），查询出相对应的数据"),
        ({"pageSize":"10","currentPage":"1","name":"柬埔寨测试03","code":"hj001","purchaseCatId":"859380"},{'code': 'success', 'result': '沒有搜尋到相關數據'},"10.验证查询组合编码和名称或类目（不等同于一条数据），无数据")
        ]
    @allure.story("商品配置")
    @allure.title("{title}")
    @allure.severity("normal")
    @pytest.mark.parametrize("test_input,excepted,title",
                             test_datas
                             )
    def test_query_list_06(self,df_login_xadmin,test_input,excepted,title):
        with allure.step("step1 :登录"):
            s = df_login_xadmin
            DF_Login(s)
        with allure.step("step2 :进入到商品系统管理"):
            pass
        with allure.step("step3: 进入到商品配置中的货架组配置页，点击查询"):
            result=commodity_information(s).query_list_shelves(test_input['pageSize'],test_input['currentPage'],test_input['name'],test_input['code'],test_input['purchaseCatId'])
        with allure.step("step4: 断言"):
            assert result['result']==excepted['result']
            assert result['code']==excepted['code']


    @allure.story("货架组管理")
    @allure.title("验证新增货架组功能有效性")
    @allure.severity("normal")
    def test_add_shelves_07(self,df_login_xadmin,delete_shelfgrouplevel):
        '''验证新增货架组功能有效性'''
        with allure.step("step1 :登录"):
            s = df_login_xadmin
            DF_Login(s)
        with allure.step("step2 :进入到商品系统管理/商品配置"):
            pass
        with allure.step("step3: 点击新增货架组"):
            result=commodity_information(s).add_shelves(name="柬埔寨货架11")
        with allure.step("step4: 断言"):
            assert result['result']=='操作成功'


    @allure.story("货架组管理")
    @allure.title("验证已存在的货架组名称，不可再次添加")
    @allure.severity("normal")
    def test_add_shelves_08(self,df_login_xadmin,delete_shelfgrouplevel):
        '''验证已存在的货架组名称，不可再次添加'''
        with allure.step("step1 :登录"):
            s = df_login_xadmin
            DF_Login(s)
        with allure.step("step2 :进入到商品系统管理/商品配置"):
            pass
        with allure.step("step3: 点击新增货架组"):
            result=commodity_information(s).add_shelves(name="柬埔寨货架11")
            result=commodity_information(s).add_shelves(name="柬埔寨货架11")
        with allure.step("step4: 断言"):
            assert result['result']=='已經存在相同貨架組級'



    def test_add_shelves_09(self,df_login_xadmin,delete_shelfgrouplevel):
        '''验证修改货架组信息功能的有效性'''
        with allure.step("step1 :登录"):
            s = df_login_xadmin
            DF_Login(s)
        with allure.step("step2 :进入到商品系统管理/商品配置"):
            pass
        with allure.step("step3: 点击新增货架组"):
            result=commodity_information(s).update_shelves(name="柬埔寨货架13",code="JPZ011",purchaseCatId="859380",id="98")
        with allure.step("step4: 断言"):
            assert result['result']=='操作成功'

    def test_relate_shelfgrouplevel_10(self,df_login_xadmin):
        '''验证货架组关联门店功能的有效性'''
        with allure.step("step1 :登录"):
            s = df_login_xadmin
            DF_Login(s)
        with allure.step("step2 :进入到商品系统管理/商品配置/货架组级门店管理"):
            pass
        with allure.step("step3 :已创建好的货架组，点击分配门店"):
            result=commodity_information(s).relate_shelfgrouplevel()
        with allure.step("step4: 断言"):
            assert result['result']=='操作成功'


    def test_import_ware(self,df_login_xadmin,delete__ware):
        '''验证模板导入批量商品配置有效性'''
        with allure.step("step1 :登录"):
            s = df_login_xadmin
            DF_Login(s)
        with allure.step("step2 :进入到商品系统管理/商品配置/货架组级门店管理"):
            pass
        with allure.step("step3 :已创建好的货架组，点击分配门店"):
            result=commodity_information(s).import_ware()
        with allure.step("step4: 断言"):
            assert result['result']=='導入貨架組級-商品數據文件成功'


