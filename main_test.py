
from pkg.eventGetter.EventsGetter import get_events
from pkg.token_getter.tokens import *
import json
def testEvent():
    data = get_events()
    for e in data:
        print(e)
def testjson():
    json_string = '{ "p": "ythtest", "op": 1, "tick": "yth", "max": 1000, "lim": 10, "dec": 1 }'

    # 使用 json.loads() 将字符串转换为字典
    data = json.loads(json_string)

    print(data)
    # 输出应该是: {'p': 'ythtest', 'op': 1, 'tick': 'yth', 'max': 1000, 'lim': 10, 'dec': 1}

def testAPI():
    ntf_list, deployFT_map, ft_account_map  = get_valid_tokens()
    print(deployFT_map)

if __name__=="__main__" :
    testAPI()
