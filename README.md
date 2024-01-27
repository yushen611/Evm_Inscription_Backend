# Evm_Inscription_Backend
EVM上的铭文系统后端


## 安装fastapi 

https://fastapi.tiangolo.com/zh/

```bash
pip install fastapi
pip install "uvicorn[standard]"
```

## !启动方式
在项目跟目录 输入下面的命令启动
```bash
python -m uvicorn main:app --reload
```
## 任务

前端

<img src="https://gitee.com/yushen611/img/raw/master/image-20240127144026699.png" alt="image-20240127144026699" style="zoom:50%;" />

1. 发送data（前端实现 long）

 后端实现（python）

1. 根据contract地址 获取所有的events(qhx)
   * 根据contract地址 获取所有的txs
   * 再根据tx hash 读 event .data（建个csv增量读）
2. 识别是发币，交易，挖矿的(ss)
   1. json格式合法检测代码
   2. json交易合法检测代码
   3. json挖矿合法检测代码
   4. json发币合法检测代码
3. 当前拥有某个币的地址以及该币数量，以及交易记录(ywy,lzf)
   1. 某个币的交易记录
   2. 某个币拥有者有该币的数量