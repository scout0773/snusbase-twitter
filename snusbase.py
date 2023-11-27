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
    return response.json()

def check_twitter_breach(username):
    search_response = send_request('data/search', {
        'terms': [username],
        'types': ['username'],
        'breach': 'TWITTER_COM_228M_SOCIAL_012023',
        'wildcard': False,
    })

    if search_response.get('results'):
        for breach_name, breach_data in search_response['results'].items():
            if breach_data:
                result_entry = breach_data[0]
                email = result_entry.get('email')
                if email:
                    print(f"The email associated with the username {username} in the Twitter 2023 breach is: {email}")
                    return

    print(f"The username {username} was not found in the Twitter 2023 breach.")

if __name__ == '__main__':
    username_to_check = input("Enter the username to check: ")

    check_twitter_breach(username_to_check)
