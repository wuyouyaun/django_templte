import pytest
import requests
from case.VC_project.connect_mysql import delete_db,delete_db,db_connect

# function 函数或方法  class 类  module py 文件  session 跨文件
@pytest.fixture(scope="function")
def delete_register():
    ''' 执行删除公司信息操作  '''
    sql = "delete  from cx_company where company_name='深圳大源源呐939';"
    delete_db(db=db_connect(), sql_delete=sql)
    print("1111")
    print("后置操作")
    yield


@pytest.fixture(scope="function")
def delete_account_infor():
    ''' 执行账号操作  '''
    sql = "delete  from cx_supplier_account where supplier_name='深圳大源源呐939';"
    delete_db(db=db_connect(), sql_delete=sql)
    print("9999")
    print("后置操作")
    yield


@pytest.fixture(scope="session")
def delete_cards_infor():
    ''' 执行删除供应商卡号  '''
    sql = "delete from cx_supplier where supplier_Code BETWEEN '9999010' and '9999015';"
    delete_db(db=db_connect(), sql_delete=sql)
    print("00000")
    print("后置操作")
    yield

@pytest.fixture(scope="function")
def delete_changing_code():
    '''删除changing表中的source_id数据'''
    sql = "delete from changing where source_id BETWEEN '9999009' and '9999015';"
    delete_db(db=db_connect(), sql_delete=sql)
    print("00000")
    print("后置操作")
    yield











