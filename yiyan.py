import requests
import json
TOK = os.environ[TOK]
word_url = "https://v1.hitokoto.cn/?c=d"
r = requests.get(word_url)
print(r.status_code)
words = json.loads(r.text)
sentence = f'{words["hitokoto"]}--《{words["from"]}》--{words["from_who"]}'
push_url = "http://www.pushplus.plus/send?token=" + TOK +"&title=一言&content="+sentence
pushsign = requests.get(push_url);
print(pushsign.status_code);
