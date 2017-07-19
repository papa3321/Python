import requests

cs_url   = 'http://ip.taobao.com/service/getIpInfo.php'
my_param = {'ip':'8.8.8.8'}

r = requests.get(cs_url, params = my_param)

print r.json()['data']['country'].encode('utf-8')