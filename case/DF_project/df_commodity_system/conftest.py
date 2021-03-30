import pytest
import requests
from case.DF_project.df_commodity_system.commodity_mysql import db_connect,select_sql,delete_db


# function 函数或方法  class 类  module py 文件  session 跨文件
@pytest.fixture(scope="session")
def delete_cat_level():
    ''' 执行删除类目课组信息操作  '''
    sql = "delete  from cat_framework_level where code='JPZ-09';"
    delete_db(db=db_connect(), sql_delete=sql)
    print("1111")
    print("后置操作")
    yield


@pytest.fixture(scope="function")
def delete_shelfgrouplevel():
    '''执行删除货架组的操作'''
    sql="delete  from  shelf_group_level WHERE name='柬埔寨货架11';"
    delete_db(db=db_connect(), sql_delete=sql)
    print("2222")
    print("后置操作")
    yield

@pytest.fixture(scope="function")
def delete__ware():
    '''删除货架组级商品管理'''
    sql="delete  from  shelf_group_level_ware_map WHERE sku_id='101301591';"
    delete_db(db=db_connect(), sql_delete=sql)
    print("333")
    print("后置操作")
    yield
