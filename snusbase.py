import json
import requests

snusbase_auth = 'API_KEY'
snusbase_api = 'https://api-experimental.snusbase.com/'

def send_request(url, body=None):
    headers = {
        'Auth': snusbase_auth,
        'Content-Type': 'application/json',
    }
    method = 'POST' if body else 'GET'
    data = json.dumps(body) if body else None
    response = requests.request(method, snusbase_api + url, headers=headers, data=data)
    if response.status_code != 200:
        raise Exception('request failed', response.status_code, response.reason)
    return response.json()

def check_twitter_breach(username):
    search_response = send_request('data/search', {
        'terms': [username],
        'types': ['username'],
        'breach': 'TWITTER_COM_228M_SOCIAL_012023',
        'wildcard': False,
    })

    if not search_response.get('results'):
        return print(f"The username {username} was not found in the Twitter 2023 breach.")

    for breach_name, breach_data in ((name, data) for name, data in search_response.get('results', {}).items() if data):
        email = breach_data[0].get('email')
        if email:
            print(f"{username}: {email}")
    
if __name__ == '__main__':
    while True:
        check_twitter_breach(input("Enter the username to check: "))