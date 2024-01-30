def dict_to_transaction(transaction_dict):
    transaction = Transaction()
    if 'accessList' in transaction_dict:
        transaction.accessList = transaction_dict['accessList']
    if 'blockHash' in transaction_dict:
        transaction.blockHash = transaction_dict['blockHash']
    if 'blockNumber' in transaction_dict:
        transaction.blockNumber = transaction_dict['blockNumber']
    if 'chainId' in transaction_dict:
        transaction.chainId = transaction_dict['chainId']
    if 'from' in transaction_dict:
        transaction.fromAddress = transaction_dict['from']
    if 'gas' in transaction_dict:
        transaction.gas = transaction_dict['gas']
    if 'gasPrice' in transaction_dict:
        transaction.gasPrice = transaction_dict['gasPrice']
    if 'transactionHash' in transaction_dict:
        transaction.transactionHash = transaction_dict['transactionHash']
    if 'input' in transaction_dict:
        transaction.input = transaction_dict['input']
    if 'maxPriorityFeePerGas' in transaction_dict:
        transaction.maxPriorityFeePerGas = transaction_dict['maxPriorityFeePerGas']
    if 'maxFeePerGas' in transaction_dict:
        transaction.maxFeePerGas = transaction_dict['maxFeePerGas']
    if 'nonce' in transaction_dict:
        transaction.nonce = transaction_dict['nonce']
    if 'r' in transaction_dict:
        transaction.r = transaction_dict['r']
    if 's' in transaction_dict:
        transaction.s = transaction_dict['s']
    if 'to' in transaction_dict:
        transaction.toAddress = transaction_dict['to']
    if 'transactionIndex' in transaction_dict:
        transaction.transactionIndex = transaction_dict['transactionIndex']
    if 'type' in transaction_dict:
        transaction.type = transaction_dict['type']
    if 'v' in transaction_dict:
        transaction.v = transaction_dict['v']
    if 'value' in transaction_dict:
        transaction.value = transaction_dict['value']
    if 'yParity' in transaction_dict:
        transaction.yParity = transaction_dict['yParity']

    return transaction


class Transaction:
    def __init__(self):
        self._accessList = None
        self._blockHash = None
        self._blockNumber = None
        self._chainId = None
        self._fromAddress = None
        self._gas = None
        self._gasPrice = None
        self._transactionHash = None
        self._input = None
        self._maxPriorityFeePerGas = None
        self._maxFeePerGas = None
        self._nonce = None
        self._r = None
        self._s = None
        self._toAddress = None
        self._transactionIndex = None
        self._type = None
        self._v = None
        self._value = None
        self._yParity = None

    @property
    def accessList(self):
        return self._accessList

    @accessList.setter
    def accessList(self, value):
        # 添加额外的逻辑（如果有需要的话）
        self._accessList = value

    @property
    def blockHash(self):
        return self._blockHash

    @blockHash.setter
    def blockHash(self, value):
        # 添加额外的逻辑（如果有需要的话）
        self._blockHash = value

    @property
    def blockNumber(self):
        return self._blockNumber

    @blockNumber.setter
    def blockNumber(self, value):
        # 添加额外的逻辑（如果有需要的话）
        self._blockNumber = value

    @property
    def chainId(self):
        return self._chainId

    @chainId.setter
    def chainId(self, value):
        # 添加额外的逻辑（如果有需要的话）
        self._chainId = value

    @property
    def fromAddress(self):
        return self._fromAddress

    @fromAddress.setter
    def fromAddress(self, value):
        # 添加额外的逻辑（如果有需要的话）
        self._fromAddress = value

    @property
    def gas(self):
        return self._gas

    @gas.setter
    def gas(self, value):
        # 添加额外的逻辑（如果有需要的话）
        self._gas = value

    @property
    def gasPrice(self):
        return self._gasPrice

    @gasPrice.setter
    def gasPrice(self, value):
        # 添加额外的逻辑（如果有需要的话）
        self._gasPrice = value

    @property
    def transactionHash(self):
        return self._transactionHash

    @transactionHash.setter
    def transactionHash(self, value):
        # 添加额外的逻辑（如果有需要的话）
        self._transactionHash = value

    @property
    def input(self):
        return self._input

    @input.setter
    def input(self, value):
        # 添加额外的逻辑（如果有需要的话）
        self._input = value

    @property
    def maxPriorityFeePerGas(self):
        return self._maxPriorityFeePerGas

    @maxPriorityFeePerGas.setter
    def maxPriorityFeePerGas(self, value):
        # 添加额外的逻辑（如果有需要的话）
        self._maxPriorityFeePerGas = value

    @property
    def maxFeePerGas(self):
        return self._maxFeePerGas

    @maxFeePerGas.setter
    def maxFeePerGas(self, value):
        # 添加额外的逻辑（如果有需要的话）
        self._maxFeePerGas = value

    @property
    def nonce(self):
        return self._nonce

    @nonce.setter
    def nonce(self, value):
        # 添加额外的逻辑（如果有需要的话）
        self._nonce = value

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, value):
        # 添加额外的逻辑（如果有需要的话）
        self._r = value

    @property
    def s(self):
        return self._s

    @s.setter
    def s(self, value):
        # 添加额外的逻辑（如果有需要的话）
        self._s = value

    @property
    def toAddress(self):
        return self._toAddress

    @toAddress.setter
    def toAddress(self, value):
        # 添加额外的逻辑（如果有需要的话）
        self._toAddress = value

    @property
    def transactionIndex(self):
        return self._transactionIndex

    @transactionIndex.setter
    def transactionIndex(self, value):
        # 添加额外的逻辑（如果有需要的话）
        self._transactionIndex = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        # 添加额外的逻辑（如果有需要的话）
        self._type = value

    @property
    def v(self):
        return self._v

    @v.setter
    def v(self, value):
        # 添加额外的逻辑（如果有需要的话）
        self._v = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        # 添加额外的逻辑（如果有需要的话）
        self._value = value

    @property
    def yParity(self):
        return self._yParity

    @yParity.setter
    def yParity(self, value):
        # 添加额外的逻辑（如果有需要的话）
        self._yParity = value

    def __str__(self):
        return f"Transaction(" \
               f"accessList={self._accessList}, " \
               f"blockHash={self._blockHash}, " \
               f"blockNumber={self._blockNumber}, " \
               f"chainId={self._chainId}, " \
               f"fromAddress={self._fromAddress}, " \
               f"gas={self._gas}, " \
               f"gasPrice={self._gasPrice}, " \
               f"transactionHash={self._transactionHash}, " \
               f"input={self._input}, " \
               f"maxPriorityFeePerGas={self._maxPriorityFeePerGas}, " \
               f"maxFeePerGas={self._maxFeePerGas}, " \
               f"nonce={self._nonce}, " \
               f"r={self._r}, " \
               f"s={self._s}, " \
               f"toAddress={self._toAddress}, " \
               f"transactionIndex={self._transactionIndex}, " \
               f"type={self._type}, " \
               f"v={self._v}, " \
               f"value={self._value}, " \
               f"yParity={self._yParity}" \
               f")"
