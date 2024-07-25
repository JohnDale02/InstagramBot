import time
import hashlib
import requests

username = 'jackshneider5'
password = 'TeddyD123123!'

# Generate the 'enc_password' field similar to Instagram's login request
# Note: This is a simplified example and may not be exactly as required by Instagram
time_now = int(time.time())
enc_password = f'#PWD_INSTAGRAM_BROWSER:0:{time_now}:{password}'

session = requests.Session()

# Function to get CSRF token
def get_csrf_token():
    response = session.get('https://www.instagram.com/')
    csrf_token = response.cookies.get('csrftoken')
    return csrf_token

# Function to log in to Instagram
def login():
    csrf_token = get_csrf_token()
    login_url = 'https://www.instagram.com/accounts/login/ajax/'
    login_data = {
        'username': username,
        'enc_password': enc_password,
        'queryParams': {},
        'optIntoOneTap': 'false'
    }
    headers = {
        'X-CSRFToken': csrf_token,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://www.instagram.com/',
    }
    login_response = session.post(login_url, data=login_data, headers=headers)
    login_response.raise_for_status()
    return login_response.json()

# Perform login
login_response_json = login()
if login_response_json.get('authenticated'):
    print('Successfully logged in!')
else:
    print('Failed to log in.')

# Replace with the actual username of the live stream account you want to watch
username_to_watch = 'dale_shots'

# Function to get user profile and extract live stream URL
def get_live_stream_url():
    user_profile_url = f'https://www.instagram.com/{username_to_watch}/'
    profile_response = session.get(user_profile_url)
    profile_response.raise_for_status()
    # Parse the response to extract the live stream URL (This part is illustrative)
    # You may need to use a HTML parser like BeautifulSoup to extract the URL
    # live_stream_url = extract_live_stream_url(profile_response.text)
    live_stream_url = 'extracted_live_stream_url'  # Placeholder for the actual extraction logic
    return live_stream_url

# Extract live stream URL
live_stream_url = get_live_stream_url()
print(f'Live stream URL: {live_stream_url}')
