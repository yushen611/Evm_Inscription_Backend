# 定义一个统一的响应结构体
class ResponseModel:
    def __init__(self, data, code: int, msg: str):
        self.code = code
        self.msg = msg
        self.data = data

    def to_dict(self):
        return {"code": self.code, "msg": self.msg, "data": self.data}

# 成功响应的帮助函数
def success_response(data):
    return ResponseModel(data=data, code=1, msg="Success").to_dict()

# 失败响应的帮助函数
def error_response(message):
    return ResponseModel(data={}, code=-1, msg=message).to_dict()