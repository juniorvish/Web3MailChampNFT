```python
import requests

class DispatchAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_nfts(self):
        response = requests.get(f"{self.base_url}/nfts")
        return response.json()

    def update_nft_metadata(self, nft_id, metadata):
        response = requests.patch(f"{self.base_url}/nfts/{nft_id}", json=metadata)
        return response.json()

    def send_nft_batch(self, nft_batch):
        response = requests.post(f"{self.base_url}/nfts/batch", json=nft_batch)
        return response.json()

    def draft_cnft_message(self, cnft_message):
        response = requests.post(f"{self.base_url}/cnft/message", json=cnft_message)
        return response.json()

dispatchApi = DispatchAPI("https://api.dispatch.com")
```