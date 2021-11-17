# 百度网盘签到脚本
import time
import datetime
import requests
import os

_t = str(int(time.time()))
headers = os.environ["BAIDUHD"]
headers = headers.json()
TOK = os.environ["TOK"]
url_qd = 'https://pan.baidu.com/pmall/points/signin?c=8D10C29AACC9B74110170EA14822683F%7C0&z=T3z47Bw7wplxR2NRq2T1P1N8Bz-1XcVyRYjCtSHdIH0lSU3g1AANWrWiNSGolo9he86ru1-Lv5M-holrAxdUJIw&app=android&ver=11.13.8&ua=netdisk%3B11.13.8%3Bmi%2B10%3Bandroid-android%3B11%3Bjsbridge4.4.0%3Bjointbridge%3B1.1.0%3B&channel=android&version=11.13.8&time=1632111532&devuid=8D10C29AACC9B74110170EA14822683F%7C0&rand=2138b7c8eb86addac823f6bc07464c4e4c621a41&ev=sign&hjs=1&aid=5820&clienttype=1&_t=' + _t
url_list = 'https://pan.baidu.com/pmall/points/signinlist?from=pointscenter&_t=' + _t

sentence = ""
#url = 'https://pan.baidu.com/pmall/points/signinlist?from=pointscenter_t='
res_qd = requests.get(url=url_qd, headers=headers)
data_qd = res_qd.json()
if not data_qd['errno']:
    print('')
    if data_qd['is_first']:
        sentence = sentence + '这是今天第一次签到'
        print('这是今天第一次签到')
    else:
        sentence = sentence + "今天已经签到过了"
        print(sentence)

sentence = sentence + '\n'

res_list = requests.get(url_list, headers=headers)
data_list = res_list.json()
if not data_list['errno']:
    lists = data_list['list']
    for li in lists:
        if not li['is_signin']:
            num = li['id'] - 1
            print('今天是连续第' + str(num) + '天签到')
            sentence = sentence + '今天是连续第' + str(num) + '天签到'
            break
else:
    sentence = sentence + '请求签到列表出错！！！'
    print('请求签到列表出错！！！')


push_url = "http://www.pushplus.plus/send?token=" + \
    TOK + "&title=百度网盘签到&content=" + sentence
p1 = requests.get(push_url)

if p1.status_code:
    print("推送成功")
else:
    print("推送失败")
