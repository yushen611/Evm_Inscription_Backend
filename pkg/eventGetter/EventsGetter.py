from fastapi import APIRouter
from responce.Response import *
import csv
import os
import requests
from dotenv import load_dotenv
from config.config import *

# 根据contract地址 获取所有的events(qhx)

# 加载环境变量
load_dotenv()

api_key = API_KEY
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


# todo 转换成封装结构会无法请求etherscan？目前不知道是为什么
def get_data():
    url = ("https://api-sepolia.etherscan.io/api"
              "?module=logs"
              "&action=getLogs"
              f"&fromBlock={from_block}"
              "&toBlock=latest"
              f"&address={contract_address}"
              f"&topic0={topic0}"
              f"&apikey={api_key}")

    response = requests.get(url).json()
    data = response['result']
    return data


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

def get_event():
    # 这里返回list of envets
    result = get_data()
    ...



