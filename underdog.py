```python
import requests
import json

class Underdog:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.underdogprotocol.com"

    def create_list(self, list_name):
        url = f"{self.base_url}/lists"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {"name": list_name}
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()

    def collect_wallet_addresses(self, list_id, addresses):
        url = f"{self.base_url}/lists/{list_id}/addresses"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {"addresses": addresses}
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()

    def send_cNFTs(self, list_id, nft_id):
        url = f"{self.base_url}/lists/{list_id}/send"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {"nft_id": nft_id}
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()

    def get_nfts(self):
        url = f"{self.base_url}/nfts"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(url, headers=headers)
        return response.json()

    def update_nft_metadata(self, nft_id, metadata):
        url = f"{self.base_url}/nfts/{nft_id}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {"metadata": metadata}
        response = requests.patch(url, headers=headers, data=json.dumps(data))
        return response.json()

    def batch_send_nfts(self, list_id, nft_ids):
        url = f"{self.base_url}/lists/{list_id}/batch_send"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {"nft_ids": nft_ids}
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()
```