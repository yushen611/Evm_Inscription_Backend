from fastapi import APIRouter,HTTPException
from responce.Response import *
from typing import Union

router = APIRouter()
# todo: 根据contract地址 获取所有的events(qhx)

@router.get("/events/ping")
def read_root():
    # 使用成功响应的帮助函数
    return success_response(data={"Hello": "events"})