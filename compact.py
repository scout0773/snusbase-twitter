import requests
def check_twitter_breach(username):
    r = requests.post(f'https://api-experimental.snusbase.com/data/search', headers={'Auth': 'API_KEY', 'Content-Type': 'application/json'}, json={'terms': [username], 'types': ['username'], 'breach': 'TWITTER_COM_228M_SOCIAL_012023', 'wildcard': False})
    if r.status_code == 200:
        for breach_name, breach_data in r.json().get('results', {}).items():
            email = breach_data[0].get('email')
            if email: print(f"{username}: {email}")
if __name__ == '__main__':
    while True: check_twitter_breach(input("Enter the username to check: "))