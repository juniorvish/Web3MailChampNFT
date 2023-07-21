```python
import requests
import csv

class SynapAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.synap.io/"

    def get_nft_list(self):
        url = self.base_url + "nfts"
        headers = {"Authorization": "Bearer " + self.api_key}
        response = requests.get(url, headers=headers)
        return response.json()

    def upload_csv(self, file_path):
        url = self.base_url + "upload_csv"
        headers = {"Authorization": "Bearer " + self.api_key}
        with open(file_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(url, headers=headers, files=files)
        return response.json()

synap_api = SynapAPI("your_synap_api_key")
```