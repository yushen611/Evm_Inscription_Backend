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
### json to NFT object
`def json_to_nft_object(json_data: str) -> NFT`
### json to FT object
`def json_to_ft_object(json_data: str) -> FT`

This function will return specific enumeration class as below instead of `FT`:
```python
class FT(Enum):
    deploy = DeployFT,
    mint = MintFT,
    transfer = TransferFT,
```
If there is a need for expanding types, they can be incrementally added in the enumeration.
### `to_json` method
Implementation of `NFT` and every implementation of `FT` has already implemented the `to_json` method to generate json
string by class object.
### json format check function
```python
def json_format_check(json_data: str) -> bool
```
This function will run before parsing the json string to object.
And it can be called independently to check if a string is in json format.