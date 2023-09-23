import requests

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'YOUR_API_KEY'

# Replace 'latitude' and 'longitude' with the coordinates of the location you're interested in
latitude = 37.7749
longitude = -122.4194

# Specify the URL for the NWS API endpoint
api_url = f'https://api.weather.gov/points/{latitude},{longitude}/forecast'

# Set up the headers with your API key
headers = {'User-Agent': 'YourApp', 'Authorization': f'Token {api_key}'}

# Send an HTTP GET request to the NWS API
response = requests.get(api_url, headers=headers)

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    data = response.json()
    # You can now work with the weather data in the 'data' variable
    print(data)
else:
    print(f"Request failed with status code {response.status_code}")