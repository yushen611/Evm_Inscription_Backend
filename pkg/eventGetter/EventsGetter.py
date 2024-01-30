import json

from fastapi import APIRouter
from responce.Response import *
import csv
import os
import requests
from dotenv import load_dotenv
from config.config import *
from Event import Event as E
from Transaction import Transaction as T
import Event
import Transaction
# 根据contract地址 获取所有的events(qhx)

# 加载环境变量
load_dotenv()

etherscan_api_key = ETHERSCAN_API_KEY
infura_api_key = INFURA_API_KEY
contract_address = CONTRACT_ADDRESS
topic0 = TOPIC_0
from_block = CONTRACT_BLOCK
event_csv_file_path = EVENT_FILE


# 判断文件是否存在
def is_file_exists(file_path):
    if os.path.exists(file_path):
        return True
    else:
        return False


# 判断文件是否为空
def is_file_Empty(file_path):
    if os.path.getsize(file_path):
        return False
    else:
        return True


# 创建文件并写表头
def create_event_file_with_header(file_path):
    # 如果文件不存在则创建
    if not is_file_exists(file_path):
        file = open(file_path, "w")
        # print("创建{}文件".format(file_path))
        file.close()




# 写event文件
def write_events_file(file_path,data):
    with open(file_path, 'a', newline='') as file:
        csv_headers = list(data[0].keys())
        csv_writer = csv.writer(file)
        # 如果文件为空写表头
        if is_file_Empty(file_path):
            # print(csv_headers)
            csv_writer.writerow(csv_headers)
        for row in data:
            # 写每行数据
            values = [row.get(field, '') for field in csv_headers]
            csv_writer.writerow(values)



def get_events():
    url = ("https://api-sepolia.etherscan.io/api"
              "?module=logs"
              "&action=getLogs"
              f"&fromBlock={from_block}"
              "&toBlock=latest"
              f"&address={contract_address}"
              f"&topic0={topic0}"
              f"&apikey={etherscan_api_key}")

    response = requests.get(url).json()
    data_list = response['result']
    event_list = []
    for data in data_list:
        event = Event.dict_to_event(data)
        event = get_transaction(event)
        event_list.append(event)
    return event_list


def get_transaction(event):
    transactionHash = event.transactionHash
    url = f"https://sepolia.infura.io/v3/{INFURA_API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {
        "jsonrpc": "2.0",
        "method": "eth_getTransactionReceipt",
        "params": [transactionHash],
        "id": 1
    }

    response = requests.post(url, json=data, headers=headers).json()
    sender = response['result']['from']
    event.sender = sender
    return event


if __name__=="__main__":
    data = get_events()
    for e in data:
        print(e)
