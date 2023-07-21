```python
import requests
from underdog import underdogApi
from dispatch import dispatchApi
from synap import synapApi

class CNFTMetrics:
    def __init__(self):
        self.underdogApi = underdogApi
        self.dispatchApi = dispatchApi
        self.synapApi = synapApi

    def get_open_rate(self, nft_id):
        response = self.dispatchApi.get(f"/nfts/{nft_id}/open_rate")
        return response.json()

    def get_conversion_rate(self, nft_id):
        response = self.dispatchApi.get(f"/nfts/{nft_id}/conversion_rate")
        return response.json()

    def get_engagement_level(self, nft_id):
        response = self.dispatchApi.get(f"/nfts/{nft_id}/engagement_level")
        return response.json()

    def get_utm_parameters(self, nft_id):
        response = self.dispatchApi.get(f"/nfts/{nft_id}/utm_parameters")
        return response.json()

    def get_on_chain_stamps(self, nft_id):
        response = self.underdogApi.get(f"/nfts/{nft_id}/on_chain_stamps")
        return response.json()

    def get_product_usage(self, nft_id):
        response = self.synapApi.get(f"/nfts/{nft_id}/product_usage")
        return response.json()

    def get_referrals(self, nft_id):
        response = self.synapApi.get(f"/nfts/{nft_id}/referrals")
        return response.json()

    def get_drop_off_point(self, nft_id):
        response = self.synapApi.get(f"/nfts/{nft_id}/drop_off_point")
        return response.json()

cnftMetrics = CNFTMetrics()
```