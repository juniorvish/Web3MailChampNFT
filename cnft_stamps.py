```python
import requests
from underdog import underdogApi

def get_on_chain_stamps(nft_id):
    response = underdogApi.get(f"/nfts/{nft_id}/stamps")
    return response.json()

def add_on_chain_stamp(nft_id, stamp):
    response = underdogApi.post(f"/nfts/{nft_id}/stamps", json=stamp)
    return response.json()

def update_on_chain_stamp(nft_id, stamp_id, new_stamp):
    response = underdogApi.put(f"/nfts/{nft_id}/stamps/{stamp_id}", json=new_stamp)
    return response.json()

def delete_on_chain_stamp(nft_id, stamp_id):
    response = underdogApi.delete(f"/nfts/{nft_id}/stamps/{stamp_id}")
    return response.status_code == 204
```