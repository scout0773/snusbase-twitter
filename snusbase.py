import requests

snusbase_auth = 'API_KEY'
snusbase_api = 'https://api-experimental.snusbase.com/'

def check_twitter_breach(username):
    url = f'{snusbase_api}data/search'
    body = {
        'terms': [username],
        'types': ['username'],
        'breach': 'TWITTER_COM_228M_SOCIAL_012023',
        'wildcard': False,
    }
    headers = {'Auth': snusbase_auth, 'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, json=body)

    if response.status_code != 200:
        raise Exception('Request failed', response.status_code, response.reason)

    results = response.json().get('results', {})
    for breach_name, breach_data in results.items():
        email = breach_data[0].get('email')
        if email:
            print(f"{username}: {email}")

if __name__ == '__main__':
    while True:
        check_twitter_breach(input("Enter the username to check: "))
