from fastapi import APIRouter,HTTPException
from responce.Response import *
from pkg.token_getter.tokens import *
from typing import Union
from pkg.Enum.mode import Mode

router = APIRouter()
# todo: 这里写token info（ywy）

@router.get("/token/ping")
def token_ping():
    # 使用成功响应的帮助函数
    return success_response(data={"Hello": "token"})

@router.get("/token/nft/all")
def get_nft_all():
    nft_list, _, _ = get_valid_tokens()
    # 使用成功响应的帮助函数
    return success_response(data=nft_list)

@router.get("/token/ft/can_mint")
def get_ft_can_mint():
    _, deployft_map, _  = get_valid_tokens(Mode.fast)
    # 使用成功响应的帮助函数
    return success_response(data=deployft_map)

@router.get("/token/ft/all")
def get_ft_all():
    _, _, ft_account_map  = get_valid_tokens(Mode.fast)
    # 使用成功响应的帮助函数
    return success_response(data=ft_account_map)

@router.get("/token/ft/{ft_tick}")
def get_ft_by_tick(ft_tick: str):
    _, _, ft_account_map  = get_valid_tokens(Mode.fast)
    if ft_tick not in ft_account_map.keys():
        error_response("ft_tick is not been deployed ")
    # 使用成功响应的帮助函数
    return success_response(data=ft_account_map[ft_tick])