import requests
import yaml
import os


def yaml_path(curpathread):
    '''
    获取新增公司信息数据
    :param curpathread:
    :return: data
    '''
    # real_path = os.path.dirname(os.path.realpath(__file__))
    # ture_path = os.path.join(real_path,"supplier_company")
    # print(ture_path)
    f = open(curpathread, "r", encoding="utf-8")
    yamlpath = f.read()
    print(yamlpath)
    data = yaml.load(yamlpath, Loader=yaml.FullLoader)
    return data


def updata_company(curpathread):
    '''
    获取修改公司信息的数据
    :return:
    '''

    f = open(curpathread, "r", encoding="utf-8")
    yamlpath = f.read()
    print(yamlpath)
    data = yaml.load(yamlpath, Loader=yaml.FullLoader)
    return data


def find_company_infor(curpathread):
    '''
    获取查询公司信息列表数据
    :return:
    '''
    f = open(curpathread, "r", encoding="utf-8")
    yamlpath = f.read()
    print(yamlpath)
    data = yaml.load(yamlpath, Loader=yaml.FullLoader)
    return data


def find_account_lists(curpathread):
    '''
    获取查询账号管理列表数据
    :return:
    '''
    f = open(curpathread, "r", encoding="utf-8")
    yamlpath = f.read()
    print(yamlpath)
    data = yaml.load(yamlpath, Loader=yaml.FullLoader)
    return data


def update_account_informations(curpathread):
    '''
    获取修改卡号信息数据
    :return:
    '''
    f = open(curpathread, "r", encoding="utf-8")
    yamlpath = f.read()
    print(yamlpath)
    data = yaml.load(yamlpath, Loader=yaml.FullLoader)
    return data

def add_supplier_infos(curpathread):
    '''
    获取新增供应商信息
    '''
    f = open(curpathread, "r", encoding="utf-8")
    yamlpath = f.read()
    print(yamlpath)
    data = yaml.load(yamlpath, Loader=yaml.FullLoader)
    return data

# def apporve_supplier_cards(curpathread):
#     '''
#     审核供应商卡号
#     '''
#     f = open(curpathread, "r", encoding="utf-8")
#     yamlpath = f.read()
#     print(yamlpath)
#     data = yaml.load(yamlpath, Loader=yaml.FullLoader)
#     return data







if __name__ == "__main__":

    real_path = os.path.dirname(os.path.realpath(__file__))
    update_path = os.path.join(real_path, "supplier_company")
    print(update_path)

    # real_path_yaml = yaml_path(curpathread)
    # print(type(real_path_yaml))
    # print(real_path_yaml['updata_company_information'])
    # updata_company(update_path)
    updatas = updata_company(update_path)
    print(updatas['updata_company_information'])
