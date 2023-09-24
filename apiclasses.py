import requests

class weatherClient:
    def __init__(self, base_url):
        self.base_url = base_url
    #gets response 
    def make_request(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"

        try:
            response = requests.get(url, params=params)
        #returns all param data 
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except Exception as e:
            return None
    