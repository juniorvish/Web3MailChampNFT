```python
import requests
from underdog import underdogApi

def scanWallet(walletAddress):
    """
    Function to scan the user's wallet to check for certain NFTs or number of NFTs
    """
    response = underdogApi.get(f"/wallets/{walletAddress}")
    return response.json()

def tokenGate(walletAddress, requiredNfts):
    """
    Function to give access to special features, drops, etc. based on the number of NFTs in the user's wallet
    """
    wallet = scanWallet(walletAddress)
    if wallet['nfts'] >= requiredNfts:
        return True
    else:
        return False
```