import requests

url = 'https://api.genius.com/search/'
client_access_token = 'IWpFzVkQwjDM7lHOCJMLwmE_2gXA_AdIvY8WWPJSCKU8YxnSn1MJt_bBhtNROwL_'

def get_by_artist(artist):
    params = {'q': artist}
    token = 'Bearer {}'.format(client_access_token)
    headers = {'Authorization': token}
    response = requests.get(url=url, params=params, headers=headers)
    response = response.json()
    return response['response']['hits']