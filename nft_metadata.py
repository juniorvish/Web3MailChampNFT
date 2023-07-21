```python
import requests
from underdog import underdogApi

def updateNftMetadata(nft_id, metadata):
    """
    Function to update the metadata of a specific NFT using the Underdog API
    """
    url = f"{underdogApi}/nfts/{nft_id}"
    headers = {"Content-Type": "application/json"}
    data = {"metadata": metadata}
    response = requests.patch(url, headers=headers, json=data)

    if response.status_code == 200:
        print(f"Metadata for NFT {nft_id} updated successfully.")
    else:
        print(f"Failed to update metadata for NFT {nft_id}. Error: {response.text}")

def getNftMetadata(nft_id):
    """
    Function to get the metadata of a specific NFT using the Underdog API
    """
    url = f"{underdogApi}/nfts/{nft_id}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['metadata']
    else:
        print(f"Failed to get metadata for NFT {nft_id}. Error: {response.text}")
        return None
```