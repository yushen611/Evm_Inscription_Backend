from pkg.eventGetter.EventsGetter import get_events
from pkg.json_unpack.json_unpack import *
from pkg.json_unpack.json_classes_src import *
from collections import defaultdict
from pkg.eventGetter.Transaction import *
from pkg.eventGetter.Event import Event
from typing import Dict, List
from pkg.save_load.save_load import *
from pkg.Enum.mode import Mode

def get_valid_tokens(mode:Mode=Mode.default):
    # 加载老数据
    NFT_list,DeployFT_map,Ft_Account_map = load_NFT_list(),load_DeployFT_map(),load_Ft_Account_map()
    if mode == mode.fast:
        return NFT_list,DeployFT_map,Ft_Account_map
    # 加载新数据
    download_NFT_list,download_DeployFT_map,download_Ft_Account_map = download_nft_ft()
    # 合并
    if len(download_NFT_list) > 0:
        NFT_list.extend(download_NFT_list)

    if len(download_DeployFT_map) > 0:
        for key, value in download_DeployFT_map.items():
            DeployFT_map[key] = value

    if len(download_Ft_Account_map) > 0 :
        for outer_key, inner_dict in download_Ft_Account_map.items():
            for inner_key, value in inner_dict.items():
                Ft_Account_map[outer_key][inner_key] += value

    save_NFT_list(NFT_list)
    save_DeployFT_map(DeployFT_map)
    save_Ft_Account_map(Ft_Account_map)
    return NFT_list, DeployFT_map, Ft_Account_map

def download_nft_ft():
    NFT_list = []
    DeployFT_map = defaultdict(DeployFT)
    Ft_Account_map = defaultdict(lambda: defaultdict(int))

    events = get_events()
    event_handlers = {
        NFT: _handle_nft,
        DeployFT: _handle_deploy_ft,
        MintFT: _handle_mint_ft,
        TransferFT: _handle_transfer_ft
    }

    for event in events:
        obj,_ = hex_to_object(event.data)
        if obj is None:
            continue
        handler = event_handlers.get(type(obj))
        if handler:
            # print(event.transactionHash)
            handler(event, obj, NFT_list=NFT_list, DeployFT_map=DeployFT_map, Ft_Account_map=Ft_Account_map)
    return NFT_list, DeployFT_map, Ft_Account_map

def _handle_nft(
        event:Event, 
        obj:NFT,
        NFT_list: List[NFT], 
        DeployFT_map: Dict[str, DeployFT], 
        Ft_Account_map: Dict[str, Dict[str, int]]
    ):
    # 假设NFT无转移操作，只有铭刻操作
    obj.owner = get_transaction_from(event.transactionHash)
    NFT_list.append(obj)

def _handle_deploy_ft(
        event:Event, 
        obj:DeployFT, 
        NFT_list: List[NFT], 
        DeployFT_map: Dict[str, DeployFT], 
        Ft_Account_map: Dict[str, Dict[str, int]]
    ):
    # 只承认第一Deploy FT的tick有效,后面相同的tick无论规格是否相同 都视为无效
    if obj.tick not in DeployFT_map.keys():
        DeployFT_map[obj.tick] = obj
        # print(DeployFT_map)

def _handle_mint_ft(
        event:Event, 
        obj:MintFT, 
        NFT_list: List[NFT], 
        DeployFT_map: Dict[str, DeployFT], 
        Ft_Account_map: Dict[str, Dict[str, int]]
    ):
    # 这里直接把DeployFT的max记作还有多少可以被挖的量
    if obj.tick in DeployFT_map and obj.amt <= DeployFT_map[obj.tick].lim and obj.amt <= DeployFT_map[obj.tick].max:
        DeployFT_map[obj.tick].max -= obj.amt
        miner = get_transaction_from(event.transactionHash)
        Ft_Account_map[obj.tick][miner] += obj.amt

def _handle_transfer_ft(
        event:Event, 
        obj:TransferFT, 
        NFT_list: List[NFT], 
        DeployFT_map: Dict[str, DeployFT], 
        Ft_Account_map: Dict[str, Dict[str, int]]
    ):
    if obj.tick in DeployFT_map.keys() and obj.tick in Ft_Account_map.keys():
        sender = get_transaction_from(event.transactionHash)
        if obj.amt <= Ft_Account_map[obj.tick][sender]:
            Ft_Account_map[obj.tick][sender]-= obj.amt
            Ft_Account_map[obj.tick][obj.to] += obj.amt
            # 如果转账后余额为0，就把这个账户删除了
            if Ft_Account_map[obj.tick][sender] == 0:
                del Ft_Account_map[obj.tick][sender]

        
        
