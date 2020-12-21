import requests
import random
import os
username = os.environ["USER_NAME"]
password = os.environ["PASSWORD"]
step = 20000 + round(10000*random.random())
url = 'https://api.muxui.com/release/parameter_api?user=' + username +'&password=' + password + '&step=' + str(step)
headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.60'}
res = requests.get(url,headers=headers,timeout=30)
text = res.text
print(text)
