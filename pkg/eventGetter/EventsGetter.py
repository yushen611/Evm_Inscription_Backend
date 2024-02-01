
from responce.Response import *
import requests
from config.config import *
import pkg.eventGetter.Event as e
from  pkg.save_load.save_load import save_from_block,load_from_block
from pkg.Enum.mode import Mode

def get_events(mode:Mode=Mode.default) -> list[e.Event]:
    # 如果是默认模式
    if mode == Mode.default:
        from_block = load_from_block()
    elif mode == Mode.init:
        # 这个是初始化模式
        from_block = FROM_BLOCK
    url = ("https://api-sepolia.etherscan.io/api"
              "?module=logs"
              "&action=getLogs"
              f"&fromBlock={from_block}"
              "&toBlock=latest"
              f"&address={CONTRACT_ADDRESS}"
              f"&topic0={TOPIC_0}"
              f"&apikey={ETHERSCAN_API_KEY}")
    response = requests.get(url).json()
    data_list = response['result']
    event_list = []
    for data in data_list:
        event = e.dict_to_event(data)
        event_list.append(event)
    # 最后一个event的blockNumber
    save_from_block(event_list[-1].blockNumber)
    return event_list





