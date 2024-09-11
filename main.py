import jwt
import time
import requests
import json

secret_key = '17ad51b0-08c3-4263-a711-d94477ad7ea3'

def generate_token():
    try:
        payload = {
            'sub': 'find_a_realtor',
            'exp': int(time.time()) + 60 * 60  # Token expires in 1 hour
        }

        token = jwt.encode(payload, secret_key, algorithm='HS256')
        return token
    except Exception as e:
        return False


def make_requests():
    token = generate_token()
    url = "https://www.realtor.com/realestateagents/api/v3/search?nar_only=1&offset=20&limit=20&marketing_area_cities=NY_NEW%20YORK&postal_code=&is_postal_search=true&name=&types=agent&sort=recent_activity_high&far_opt_out=false&client_id=FAR2.0&recommendations_count_min=&agent_rating_min=&languages=&agent_type=&price_min=&price_max=&designations=&photo=true&seoUserType={%22isBot%22:false,%22deviceType%22:%22desktop%22}"
    headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "authorization": f"Bearer {token}",
    "if-none-match": "W/\"2cc70-HPEL5jimrZ2aksyH85J8XvI5m+s\"",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-newrelic-id": "VwEPVF5XGwQHXFNTBAcAUQ=="
  }
    response = requests.get(url, headers=headers)
    response = json.dumps(response.json())
    with open("file.json","w",encoding="utf-8") as f:
        f.write(response)

make_requests()