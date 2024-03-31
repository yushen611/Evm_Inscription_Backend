# Evm_Inscription_Backend
EVM上的铭文系统后端
[PPT：https://gamma.app/docs/SemiToken-Inscription-on-EVM-25abptmvmyjwgf2?mode=doc](https://gamma.app/docs/SemiToken-Inscription-on-EVM-25abptmvmyjwgf2?mode=doc)    


[Show Video mint:https://drive.google.com/file/d/1yUQsU0vMiZzkRpoYN4oq3YLccLPpm5kK/view?usp=sharing](https://drive.google.com/file/d/1yUQsU0vMiZzkRpoYN4oq3YLccLPpm5kK/view?usp=sharing)  


[Show Video Indexer:https://drive.google.com/file/d/1-kkEtzdEI6P99HW_F_npQ_fITLnIeO-O/view?usp=sharing](https://drive.google.com/file/d/1-kkEtzdEI6P99HW_F_npQ_fITLnIeO-O/view?usp=sharing)  


## 安装fastapi 

https://fastapi.tiangolo.com/zh/

```bash
pip install fastapi
pip install "uvicorn[standard]"
pip install web3
pip install requests
```

## !启动方式
在项目跟目录 输入下面的命令启动
```bash
python -m uvicorn main:app --reload
```
## 如何使用conda如何快速复现
1. 首先导出当前环境的配置：
```bash
conda env export > environment.yml
```
2. 将 environment.yml 文件复制到新电脑 

3. 在新电脑上创建环境： 

在新电脑上，确保已安装了 conda。然后使用以下命令创建与原来相同的环境：
```bash
conda env create -f environment.yml
```
这个命令会根据 environment.yml 文件中的配置，创建一个新的 conda 环境，并安装所有必要的包。  

4. 激活新环境： 

一旦环境创建完成，你可以使用以下命令来激活这个环境：
```bash
conda activate BC
```
## 说明

在金融和交易的语境中，“ticker”或“ticker symbol”通常是指代股票、债券、货币等交易工具的简短代码。所以在这里，tick 可能是用来唯一标识这个 Fungible Token 协议的一种缩写或代码。  

例如，如果你有一个关于以太坊（Ethereum）的 Fungible Token，tick 可能会是 ETH 的类似标识符。

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
