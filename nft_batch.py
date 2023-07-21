import requests
from underdog import underdogApi

def sendNftBatch(nftBatch):
    url = underdogApi + "/nfts/batch"
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=nftBatch)
    
    if response.status_code == 200:
        print('Batch sent successfully.')
    else:
        print('Failed to send batch. Status code:', response.status_code)

def draftNftMessage(nftMessage):
    url = underdogApi + "/nfts/message"
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=nftMessage)
    
    if response.status_code == 200:
        print('Message drafted successfully.')
    else:
        print('Failed to draft message. Status code:', response.status_code)