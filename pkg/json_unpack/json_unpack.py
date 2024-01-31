from pkg.json_unpack.json_classes_src import *
from web3 import Web3
import json


def decode_contract_string(hex_string) -> str:
    try:
        # 移除开头的 "0x"（如果存在）
        if hex_string.startswith("0x"):
            hex_string = hex_string[2:]

        # 将十六进制字符串解码为字节
        decoded_bytes = Web3.to_bytes(hexstr=hex_string)

        # 提取字符串长度
        str_length = int(decoded_bytes[32:64].hex(), 16)

        # 提取实际字符串
        original_str = decoded_bytes[64:64 + str_length].decode()
        return original_str
    except BaseException as e:
        # print(f"Hex String Decode error: {e}")
        return None


def hex_to_object(hex_string: str) -> (DeployFT | MintFT | TransferFT | NFT | None, bool):
    # print("---begin hex_to_object----")
    json_str = decode_contract_string(hex_string)
    try:
        json_data = json.loads(json_str)  # 把json_str 转成字典
    except BaseException as e:
        # print(f"Invalid JSON: {e}")
        return None, False
    # print(json_data)
    if "op" not in json_data:
        try:
            ft = NFT(json_data)
        except BaseException as e:
            # print(f"JSON Parsing to NFT error: {e}")
            return None, False
    else:
        try:
            match json_data["op"]:
                case FTOp.deploy.value:
                    ft = DeployFT(json_data)
                case FTOp.mint.value:
                    ft = MintFT(json_data)
                case FTOp.transfer.value:
                    ft = TransferFT(json_data)
                case _:
                    return None, False
        except BaseException as e:
            # print(f"JSON Parsing to FT error {e}")
            return None, False
    # print(type(ft), ft.__dict__)
    return ft, True
