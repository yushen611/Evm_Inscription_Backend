from dataclasses import dataclass, field

def dict_to_transaction(transaction_dict):
    # The **operator unpacks the dictionary so that its contents are used as keyword arguments to the Transaction constructor.
    # Any missing fields in the dictionary will simply use the default values from the data class definition.
    return Transaction(**transaction_dict)

@dataclass
class Transaction:
    accessList: list = field(default=None)
    blockHash: str = field(default=None)
    blockNumber: int = field(default=None)
    chainId: int = field(default=None)
    fromAddress: str = field(default=None)
    gas: int = field(default=None)
    gasPrice: int = field(default=None)
    transactionHash: str = field(default=None)
    input: str = field(default=None)
    maxPriorityFeePerGas: int = field(default=None)
    maxFeePerGas: int = field(default=None)
    nonce: int = field(default=None)
    r: str = field(default=None)
    s: str = field(default=None)
    toAddress: str = field(default=None)
    transactionIndex: int = field(default=None)
    type: str = field(default=None)
    v: int = field(default=None)
    value: int = field(default=None)
    yParity: int = field(default=None)

