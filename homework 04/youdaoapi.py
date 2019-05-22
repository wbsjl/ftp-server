import json

import requests

def api(key):
    # 有道翻译网址
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    headers = {"User-Agent": "Mozilla/5.0"}
    data = {"i": key,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": "15561928010891",
            "sign": "74e3a25659e38d92080d347f9836169c",
            "ts": "1556192801089",
            "bv": "6dfac01e4ee085fbf06475a5a3c2a9c2",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME"}
    # 构造请求对象
    # url:数据提交网址
    # data:传输数据
    # headers:请求头
    response = requests.post(url, data, headers)
    response_data = response.text
    # 将返还回来的json字符串转换为python字典
    result = json.loads(response_data)
    # {'type': 'ZH_CN2EN', 'errorCode': 0, 'elapsedTime': 1, 'translateResult': [[{'src': '我爱', 'tgt': 'I love'}]]}
    tgt = result['translateResult'][0][0]['tgt']
    return tgt

