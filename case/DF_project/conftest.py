# encoding:utf-8
import requests
from case.DF_project.df_testlogin import DF_Login
import pytest
from nb_log import LogManager
from nb_log_config import LOG_PATH

logger = LogManager("api").get_logger_and_add_handlers(is_add_stream_handler=True,
                                                       log_filename="api.log",
                                                       log_path=LOG_PATH
                                                        )

@pytest.fixture(scope="session")
def df_login_xadmin(request):
    s = requests.session()
    DF_Login(s)
    return s
































































