import requests

url = "https://raw.githubusercontent.com/janSathsarani/COE3200---Assignment/main/hello.py"

response = requests.get(url)
content = response.text