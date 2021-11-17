# 百度网盘签到脚本
import time
import datetime
import requests
_t = str(int(time.time()))
headers = {
    "Host": "pan.baidu.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "netdisk;11.13.8;Mi+10;android-android;11;JSbridge4.4.0;jointBridge;1.1.0;",
    "X-Requested-With": "XMLHttpRequest",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://pan.baidu.com/act/task/mainpage?devuid=8D10C29AACC9B74110170EA14822683F%7C0&clienttype=1&channel=android_11_Mi%2010_bd-netdisk_1024328u&version=11.13.8&logid=MTYzMjExMTUyMjE1NixmZTgwOjo4NDU1OmI5ZmY6ZmU4MjozNTA1JWR1bW15MCw3OTA2MTQ&vip=0&devicename=Mi%2010&firstlaunchtime=1584228957&theme=white&apn_id=1_0&freeisp=0&queryfree=0&network_type=wifi&action=main&id=987141565000&from=wodeicon&finish_tab=4",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q\u003d0.9,en-US;q\u003d0.8,en;q\u003d0.7",
    "Cookie": "Hm_lvt_0a81f908ba6e57369b34096a4c48c232=1623851604; BDUSS_BFESS=FyZURra0lwS3l5Zm04dzhBWjBJTHE3flNxLX4tU0t-TVBtdWg0MlhoU2hUN05lRVFBQUFBJCQAAAAAAAAAAAEAAACJH26OsNfR8m9rYzMzMwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKHCi16hwoteOV; PANWEB=1; Hm_lvt_fa0277816200010a74ab7d2895df481b=1629525022; SP_FW_VER=3.230.38; SG_FW_VER=1.26.3; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1630824181,1632019969; BAIDUID=8E22BD1D19AA3A9663EDD221B7A19732:FG=1; BDUSS=FyZURra0lwS3l5Zm04dzhBWjBJTHE3flNxLX4tU0t-TVBtdWg0MlhoU2hUN05lRVFBQUFBJCQAAAAAAAAAAAEAAACJH26OsNfR8m9rYzMzMwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKHCi16hwoteOV; BAIDUCUID=Yi2680uOBuluiSfSlavc8_uSvig1iS8q_P2u8_Oz2aKXLqqqB; STOKEN=f1d8c1c1946d851fcec5a225f1956af592b22c2aa6aabd6b4be4e583f8eaae55; HTTPOnly; ab_sr=1.0.1_NGM3ZDg3NTIxNGIxMDAwYTYwNjc3Yjc4MTNiMWQ0ZWYxMzUxYzFhMzg1YTE4MTAwNzVjZWNiY2JkZGEzZGIwM2Y3ZTY3YWExNWYxYTBjZDU2NDM0Nzk3MDUxNjZmZWMwMTY0ZjJhMGJiZjRhZDkyYThiNjcxMjVkYzg2NTNkNGQ5YWFmNGI2YzY3ZmNjMmI2N2YwMjJmOTliZGNmNTExYmM3ZWU2NTBlYjFlM2M4ZmIzYTUxNmVkNGUzODE5ZjBj"
}
url_qd = 'https://pan.baidu.com/pmall/points/signin?c=8D10C29AACC9B74110170EA14822683F%7C0&z=T3z47Bw7wplxR2NRq2T1P1N8Bz-1XcVyRYjCtSHdIH0lSU3g1AANWrWiNSGolo9he86ru1-Lv5M-holrAxdUJIw&app=android&ver=11.13.8&ua=netdisk%3B11.13.8%3Bmi%2B10%3Bandroid-android%3B11%3Bjsbridge4.4.0%3Bjointbridge%3B1.1.0%3B&channel=android&version=11.13.8&time=1632111532&devuid=8D10C29AACC9B74110170EA14822683F%7C0&rand=2138b7c8eb86addac823f6bc07464c4e4c621a41&ev=sign&hjs=1&aid=5820&clienttype=1&_t=' + _t
url_list = 'https://pan.baidu.com/pmall/points/signinlist?from=pointscenter&_t=' + _t

#url = 'https://pan.baidu.com/pmall/points/signinlist?from=pointscenter_t='
res_qd = requests.get(url=url_qd, headers=headers)
data_qd = res_qd.json()
if not data_qd['errno']:
    print('')
    if data_qd['is_first']:
        print('这是今天第一次签到')
    else:
        print('今天已经签到过了')


res_list = requests.get(url_list, headers=headers)
data_list = res_list.json()
if not data_list['errno']:
    lists = data_list['list']
    for li in lists:
        if not li['is_signin']:
            num = li['id'] - 1
            print('今天是连续第' + str(num) + '天签到')
            break
else:
    print('请求签到列表出错！！！')
