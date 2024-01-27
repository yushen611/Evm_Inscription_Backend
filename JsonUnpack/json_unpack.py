from json_classes_src import *


def json_format_check(json_data: str) -> bool:
    try:
        loads(json_data)
        return True
    except JSONDecodeError:
        return False


def json_to_nft_object(json_data: str) -> NFT:
    if not json_format_check(json_data):
        print("Invalid JSON")
    return NFT.from_json(json_data)


def json_to_ft_object(json_data: str) -> FT:
    if not json_format_check(json_data):
        print("Invalid JSON")
    ft = loads(json_data)
    match ft["op"]:
        case 1:
            ft = DeployFT.from_json(json_data)
        case 2:
            ft = MintFT.from_json(json_data)
        case 3:
            ft = TransferFT.from_json(json_data)
        case _:
            ft = None
    return ft


if __name__ == '__main__':
    pass
