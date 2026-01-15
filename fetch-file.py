import requests

url = "https://github.com/janSathsarani/COE3200---Assignment/blob/main/hello.py"

response = requests.get(url)
content = response.text