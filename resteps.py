import requests
import random
import os
username = os.environ["username"]
password = os.environ["password"]
step = 20000 + round(10000*random.random())
url = 'https://api.muxui.com/release/parameter_api?user=' + username +'&password=' + password + '&step=' + str(step)
headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.60'}
res = requests.get(url,headers=headers,timeout=30)
texts = res.text
print(texts)

murl = "https://sc.ftqq.com/SCU131060T694c69e64cf069c6246074d14eb8aab95fc3a05dcd859.send?text="
text = "小米运动步数修改"
desp = "修改成功，步数修改为:" + str(step)
uurl = murl+text+"&desp="+desp
message = requests.get(murl,timeout=30)
print(message)
