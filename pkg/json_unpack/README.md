# The specific interpretation of runic inscriptions.
The detailed explanation for NFT and FT inscriptions is as follows:
## NFT
```json
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
```

## FT
### The types of operations for FT inscriptions.
```python
class FTOp(Enum):
    deploy: int = 1
    mint: int = 2
    transfer: int = 3
```
If additional features are needed, enum types can be incrementally added later.

### To deploy a FT
```json
{ 
  "p": "Protocol",
  "op": "Type of event (deploy)",
  "tick": "4 letter identifier of the Protocol",
  "max": "Max supply",
  "lim": "Limit per",
  "dec": "Decimal precision"
}
```
### To mint a FT
```json
{ 
  "p": "Protocol",
  "op": "Type of operation (mint)",
  "tick": "4 letter identifier of the Protocol",
  "amt": "Amount to mint"
}
```
### To transfer a FT
```json
{ 
  "p": "Protocol",
  "op": "Type of operation (transfer)",
  "tick": "4 letter identifier of the Protocol",
  "to": "Receiver's address",
  "amt": "Amount to transfer"
}
```
## Usages of functions provided
This package provide 3 functions, namely:
```python
# this function parse the event data(in hex) to FT or NFT object
# when error occurs during parsing, the function returns None
# the second return value is a flag for whether the parsing is successful
def hex_to_object(hex_string: str) -> (FT | NFT | None, bool):
```
```python
# this function parses json data(str) to FT | NFT object
# the meaning of the second return value is same as above
def json_to_object(json_data: str) -> (FT | NFT | None, bool):
```
```python
# this function translate the hex str into utf-8 str
# the meaning of the second return value is same as above 
def hex_to_json_str(hex_string: str) -> (str, bool):
```