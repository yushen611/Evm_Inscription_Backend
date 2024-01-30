from dataclasses import dataclass, field

@dataclass
class Event:
    address: str = field(default=None)
    topics: list = field(default=None)
    data: str = field(default=None)
    blockNumber: int = field(default=None)
    blockHash: str = field(default=None)
    timeStamp: int = field(default=None)
    gasPrice: int = field(default=None)
    gasUsed: int = field(default=None)
    logIndex: int = field(default=None)
    transactionHash: str = field(default=None)
    transactionIndex: int = field(default=None)
    sender: str = field(default=None) # Assuming you want to keep this field as well.

def dict_to_event(event_dict):
    return Event(**event_dict)
