
import requests




def test_demo_01(base_url):
    print(base_url)
    print(type(base_url))
    assert requests.get(base_url+"/yoyoketang/tag/docker/").status_code == 200


