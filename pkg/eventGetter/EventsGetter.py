
from responce.Response import *
import requests
from config.config import *
import pkg.eventGetter.Event as e



def get_events() -> list[e.Event]:
    url = ("https://api-sepolia.etherscan.io/api"
              "?module=logs"
              "&action=getLogs"
              f"&fromBlock={FROM_BLOCK}"
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
    return event_list





