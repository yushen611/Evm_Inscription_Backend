

from pkg.token_getter.tokens import *
import json
def testjson():
    json_string = '{ "p": "ythtest", "op": 1, "tick": "yth", "max": 1000, "lim": 10, "dec": 1 }'

    # 使用 json.loads() 将字符串转换为字典
    data = json.loads(json_string)

    print(data)
    # 输出应该是: {'p': 'ythtest', 'op': 1, 'tick': 'yth', 'max': 1000, 'lim': 10, 'dec': 1}

def testAPI():
    ntf_list, deployFT_map, ft_account_map  = get_valid_tokens(Mode.fast)
    print(ft_account_map)

def test_load():
    Ft_Account_map = load_Ft_Account_map()
    print(Ft_Account_map)
    from_block = load_from_block()
    print(from_block,type(from_block))
def testsaveload():
    download_nft_ft()


if __name__=="__main__" :
    # testsaveload()
    testAPI()
  
    ...