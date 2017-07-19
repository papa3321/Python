import requests

def baidu_func(url):
    headers = {}
    params = {}
    req = requests.get(url, headers=headers, params=params)
    print(req.text)

if __name__ == '__main__':
    url = "https://dump-dev.askeycloudapi.com/javadump"
    baidu_func(url)