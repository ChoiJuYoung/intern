import requests

ua= 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
ct= 'application/x-www-form-urlencoded'
ka= 'sdk/1.36.6 os/javascript lang/en-US device/Win32 origin/http%3A%2F%2F34.64.230.227:5000'

apiKey = '66b0c1e32951f47316c956ad08248683'
url = 'https://sharer.kakao.com/talk/friends/picker/link'

header = {}

header['User-Agent'] = ua
data = {
    'app_key': apiKey,
    'validation_action': 'default',
    'validation_params': '{}',
    'ka': ka,
    'lcba': ''
}

res = requests.post(url, headers=header, data=data)

print(dir(res))
print(res.__attrs__)
print(res.cookies)
print(res.url)
print(res.request)