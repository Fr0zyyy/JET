import requests

def check(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"The site {url} is responding with status code 200.")
        else:
            print(f"The site {url} is responding with status code {response.status_code}.")
    except requests.exceptions.RequestException as e:
        print(f"Seems site is destroyed message: {e}")


check("https://interor.online")  #put the site you attacked
