from fastapi import APIRouter,HTTPException
from responce.Response import *
from typing import Union


router = APIRouter()



@router.get("/Example/ping")
def read_root():
    # 使用成功响应的帮助函数
    return success_response(data={"Hello": "World"})

@router.get("/Example/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    # 使用成功响应的帮助函数
    return success_response(data={"item_id": item_id, "q": q})

# 你还可以添加一个错误处理路由来展示错误响应的使用
@router.get("Example/error")
def read_error():
    # 使用失败响应的帮助函数
    raise HTTPException(status_code=400, detail=error_response("An error occurred"))