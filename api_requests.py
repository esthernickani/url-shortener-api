import requests
import pdb

from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

#Get token from .env
TOKEN = environ.get("API_SHORTENER_TOKEN")

def get_shorter_link(link):
#header for API
    headers = {
    'Authorization': f"Bearer {TOKEN}",
    'Content-Type': 'application/json',
    }

    data = { 
        "long_url": link, 
        "domain": "bit.ly"
        }

    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=data).json()

    if 'link' in response:
        return {'response': 'success',
                'message' : response['link']}
    else: 
        return {'response': 'error',
                'message': 'Request cannot be completed'}
    #{'message': 'INVALID_ARG_LONG_URL', 'resource': 'bitlinks', 'description': 'The value provided is invalid.', 'errors': [{'field': 'long_url', 'error_code': 'invalid'}]}
    #{'created_at': '2024-01-13T05:01:22+0000', 'id': 'bit.ly/4aXWcIc', 'link': 'https://bit.ly/4aXWcIc', 'custom_bitlinks': [], 'long_url': 'https://www.frontendmentor.io/', 'archived': False, 'tags': [], 'deeplinks': [], 'references': {'group': 'https://api-ssl.bitly.com/v4/groups/Bo1d4qmesRJ'}}