```python
import requests
from underdog import underdogApi

class NftAnalytics:
    def __init__(self):
        self.dashboard_url = "metaplex.underdogprotocol.com/analytics"

    def get_total_nfts(self):
        response = requests.get(f"{underdogApi}/nfts")
        return len(response.json())

    def get_open_click_rate(self):
        response = requests.get(f"{self.dashboard_url}/open_click_rate")
        return response.json()

    def get_product_usage(self):
        response = requests.get(f"{self.dashboard_url}/product_usage")
        return response.json()

    def get_referrals(self):
        response = requests.get(f"{self.dashboard_url}/referrals")
        return response.json()

    def get_user_engagement(self, user_id):
        response = requests.get(f"{underdogApi}/users/{user_id}/engagement")
        return response.json()

    def get_user_drop_off(self, user_id):
        response = requests.get(f"{underdogApi}/users/{user_id}/drop_off")
        return response.json()

    def view_analytics(self):
        total_nfts = self.get_total_nfts()
        open_click_rate = self.get_open_click_rate()
        product_usage = self.get_product_usage()
        referrals = self.get_referrals()

        print(f"Total NFTs: {total_nfts}")
        print(f"Open/Click Rate: {open_click_rate}")
        print(f"Product Usage: {product_usage}")
        print(f"Referrals: {referrals}")

if __name__ == "__main__":
    analytics = NftAnalytics()
    analytics.view_analytics()
```