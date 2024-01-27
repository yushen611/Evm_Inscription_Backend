from fastapi import APIRouter,HTTPException
from responce.Response import *
from typing import Union

router = APIRouter()
# todo: 这里写token info（ywy）

@router.get("/token/ping")
def read_root():
    # 使用成功响应的帮助函数
    return success_response(data={"Hello": "token"})