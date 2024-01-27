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

    def __init__(self, name: str, description: str, image: str, attributes: dict[str, str]):
        self.name = name
        self.description = description
        self.image = image
        self.attributes = attributes

    @classmethod
    def from_json(cls, json_data):
        data = loads(json_data)
        return cls(
            name=data['name'],
            description=data['description'],
            image=data['image'],
            attributes=data['attributes']
        )

    def to_json(self):
        return dumps({
            'name': self.name,
            'description': self.description,
            'image': self.image,
            'attributes': self.attributes
        })


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
    tick: bytes
    max: int
    lim: int
    dec: int

    def __init__(self, p: str, tick: bytes, max: int,
                 lim: int, dec: int, op: FTOp = FTOp.deploy):
        self.p = p
        self.op = op
        self.tick = tick
        self.max = max
        self.lim = lim
        self.dec = dec

    @classmethod
    def from_json(cls, json_data):
        data = loads(json_data)
        return cls(
            p=data['p'],
            op=FTOp(data['op']),
            tick=bytes.fromhex(data['tick']),
            max=data['max'],
            lim=data['lim'],
            dec=data['dec']
        )

    def to_json(self):
        return dumps({
            'p': self.p,
            'op': self.op.to_json_serializable(),
            'tick': self.tick.hex(),
            'max': self.max,
            'lim': self.lim,
            'dec': self.dec
        })


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
    tick: bytes
    amt: int

    def __init__(self, p: str, tick: bytes, amt: int, op=FTOp.mint):
        self.p = p
        self.op = op
        self.tick = tick
        self.amt = amt

    @classmethod
    def from_json(cls, json_data):
        data = loads(json_data)
        return cls(
            p=data['p'],
            op=FTOp(data['op']),
            tick=bytes.fromhex(data['tick']),
            amt=data['amt']
        )

    def to_json(self):
        return dumps({
            'p': self.p,
            'op': self.op.value,
            'tick': self.tick.hex(),
            'amt': self.amt
        })


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
    tick: bytes
    to: bytes
    amt: int

    def __init__(self, p: str, tick: bytes, to: bytes, amt: int, op: FTOp = FTOp.transfer):
        self.p = p
        self.op = op
        self.tick = tick
        self.to = to
        self.amt = amt

    @classmethod
    def from_json(cls, json_data):
        data = loads(json_data)
        return cls(
            p=data['p'],
            op=FTOp(data['op']),
            tick=bytes.fromhex(data['tick']),
            to=bytes.fromhex(data['to']),
            amt=data['amt']
        )

    def to_json(self):
        return dumps({
            'p': self.p,
            'op': self.op.value,
            'tick': self.tick.hex(),
            'to': self.to.hex(),
            'amt': self.amt
        })


class FT(Enum):
    deploy = DeployFT,
    mint = MintFT,
    transfer = TransferFT,
