import requests
import json
import os
TOK = os.environ["TOK"]
TOK1 = os.environ["TOK1"]
word_url = "https://v1.hitokoto.cn/?c=d"
r = requests.get(word_url)
print(r.status_code)
words = json.loads(r.text)
sentence = f'{words["hitokoto"]}--《{words["from"]}》--{words["from_who"]}'
push_url = "http://www.pushplus.plus/send?token=" + TOK +"&title=一言&content="+sentence
push_url1 = "http://www.pushplus.plus/send?token=" + TOK1 +"&title=一言&content="+sentence
p1 = requests.get(push_url);
p2 = requests.get(push_url1);
print(p1.status_code);

