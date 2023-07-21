```python
import requests
from underdog import underdogApi
from dispatch import dispatchApi

def getNftList():
    response = underdogApi.get("/nfts")
    return response.json()

def updateNftMetadata(nft_id, metadata):
    response = underdogApi.patch(f"/nfts/{nft_id}", json=metadata)
    return response.json()

def sendNftBatch(nft_batch):
    response = underdogApi.post("/nfts/batch", json=nft_batch)
    return response.json()

def draftNftMessage(nft_id, message):
    response = dispatchApi.post(f"/nfts/{nft_id}/message", json=message)
    return response.json()

def viewNft(nft_id):
    response = underdogApi.get(f"/nfts/{nft_id}")
    return response.json()

def notifyNft(nft_id):
    response = dispatchApi.get(f"/nfts/{nft_id}/notify")
    return response.json()
```