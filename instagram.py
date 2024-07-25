

# Replace with your actual Instagram credentials
username = 'jackshneider5'
password = 'TeddyD123123!'

import requests
import subprocess

login_url = 'https://www.instagram.com/accounts/login/ajax/'
session = requests.Session()

# Get CSRF token
session.get('https://www.instagram.com/')
csrf_token = session.cookies['csrftoken']

# Login to Instagram
login_data = {
    'username': username,
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}',
    'queryParams': {},
    'optIntoOneTap': 'false'
}
headers = {
    'X-CSRFToken': csrf_token
}
login_response = session.post(login_url, data=login_data, headers=headers)
login_response.raise_for_status()

# Check login status
if login_response.json().get('authenticated'):
    print('Successfully logged in!')
else:
    print('Failed to log in.')

username_to_watch = 'dale_shots'
# Get live stream URL (this part may require specific handling based on how you retrieve the stream URL)
# Example: Navigate to the user's profile and find the live stream URL
user_profile_url = f'https://www.instagram.com/{username_to_watch}/'
profile_response = session.get(user_profile_url)
profile_response.raise_for_status()

# Extract live stream URL from the profile page or specific endpoint (requires custom logic)
live_stream_url = 'extracted_live_stream_url'


end_of_url = "dale_shots/live/?broadcast_id=17965427855773658"
subprocess.run(["ffmpeg", "-cookies", f"sessionid={session}", f"csrftoken={csrf_token}", "-i", "https://www.instagram.com/{end_of_url}", "-c", "output.mp4"]) 
