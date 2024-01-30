from json_classes_src import *


def hex_to_json_str(hex_string: str) -> (str, bool):
    try:
        return bytes.fromhex(hex_string).decode('utf-8'), True
    except BaseException as e:
        print(f"Hex String Decode error: {e}")
        return "", False


def json_to_object(json_data: str) -> (DeployFT| MintFT | TransferFT | NFT | None, bool):
    try:
        loads(json_data)
    except BaseException as e:
        print(f"Invalid JSON: {e}")
        return None, False
    ft = loads(json_data)
    if 'op' not in ft:
        try:
            ft = NFT(ft)
        except BaseException as e:
            print(f"JSON Parsing to NFT error: {e}")
            return None, False
    else:
        try:
            match ft["op"]:
                case FTOp.deploy.value:
                    ft = DeployFT(json_data)
                case FTOp.mint.value:
                    ft = MintFT(json_data)
                case FTOp.transfer.value:
                    ft = TransferFT(json_data)
                case _:
                    ft = None
        except BaseException as e:
            print(f"JSON Parsing to FT error {e}")
            return None, False
    return ft, True


def hex_to_object(hex_string: str) -> (FT | NFT | None, bool):
    try:
        return json_to_object(hex_to_json_str(hex_string)[0])[0], True
    except BaseException as e:
        print(f"Hex String Parse to Obj error: {e}")
        return None, False


