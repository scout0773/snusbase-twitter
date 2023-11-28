import requests

snusbase_auth = 'API_KEY'

def check_twitter_breach(username):
    body = {
        'terms': [username],
        'types': ['username'],
        'breach': 'TWITTER_COM_228M_SOCIAL_012023',
        'wildcard': False,
    }
    headers = {'Auth': snusbase_auth, 'Content-Type': 'application/json'}
    response = requests.post('https://api-experimental.snusbase.com/data/search', headers=headers, json=body)

    if response.status_code != 200:
        raise Exception('Request failed', response.status_code, response.reason)

    results = response.json().get('results', {})

    if not results:
        return print(f"The username {username} was not found in the Twitter 2023 breach.")

    for breach_name, breach_data in results.items():
        email = breach_data[0].get('email')
        if email:
            print(f"{email}")

if __name__ == '__main__':
    while True:
        check_twitter_breach(input("Enter the username to check: "))