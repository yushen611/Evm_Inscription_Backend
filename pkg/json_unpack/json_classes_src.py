"""
Json索引器
"""
from enum import Enum
from json import *

"""
# Non-Fungible Tokens Metadata Schema
{
  "name": "Identifies the asset to which this NFT represents",
  "description": "Describes the asset to which this NFT represents",
  "image": "Image data conforming to RFC2397 standard.",
  "attributes": [
    {
      "key": "",
      "value": ""
    },
    {
      "key": "",
      "value": ""
    },
    {
      "key": "",
      "value": ""
    }
  ]
}
"""


class NFT:
    name: str
    description: str
    image: str
    attributes: dict[str, str]

    def __init__(self, json_data: str):
        data = dumps(json_data)
        self.name = data['name']
        self.description = data['description']
        self.image = data['image']
        temp: list[dict[str, str]] = list(data['attributes'])
        self.attributes: dict[str, str] = dict()
        for it in temp:
            self.attributes[it.pop('key')] = it.pop('value')
        self.owner = None # NFt的拥有者


"""
# Fungible Tokens Metadata Standard
# deploying Fungible Tokens
{ 
  "p": "Protocol",
  "op": "Type of event (deploy)",
  "tick": "4 letter identifier of the Protocol",
  "max": "Max supply",
  "lim": "Limit per",
  "dec": "Decimal precision"
}
"""


class FTOp(Enum):
    deploy: int = 1
    mint: int = 2
    transfer: int = 3

    def to_json_serializable(self):
        return self.value


class DeployFT:
    p: str
    op: FTOp = FTOp.deploy
    tick: str
    max: int
    lim: int
    dec: int

    def __init__(self, json_data):
        data = json_data
        self.p = data['p']
        self.op = FTOp.deploy
        self.tick = data['tick']
        self.max = data['max']
        self.lim = data['lim']
        self.dec = data['dec']


"""
# minting Fungible Tokens
{ 
  "p": "Protocol",
  "op": "Type of operation (mint)",
  "tick": "4 letter identifier of the Protocol",
  "amt": "Amount to mint"
}
"""


class MintFT:
    p: str
    op: FTOp = FTOp.mint
    tick: str
    amt: int

    def __init__(self, json_data):
        data = json_data
        self.p = data['p']
        self.op = FTOp.mint
        self.tick = data['tick']
        self.amt = data['amt']


"""
# transferring Fungible Tokens
{ 
  "p": "Protocol",
  "op": "Type of operation (transfer)",
  "tick": "4 letter identifier of the Protocol",
  "to": "Receiver's address",
  "amt": "Amount to transfer"
}
"""


class TransferFT:
    p: str
    op: FTOp = FTOp.transfer
    tick: str
    to: str
    amt: int

    def __init__(self, json_data):
        data = json_data
        self.p = data['p']
        self.op = FTOp.transfer
        self.tick = data['tick']
        self.to = data['to']
        self.amt = data['amt']


class FT(Enum):
    deploy = DeployFT,
    mint = MintFT,
    transfer = TransferFT,
