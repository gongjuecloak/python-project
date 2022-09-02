import urllib
from urllib.parse import quote
import string
import requests
def check_with_api(msg):
    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg=' + msg
    s = quote(url, safe=string.printable)
    with urllib.request.urlopen(s) as response:
        html = response.read()
        # 将获取到的响应内容进行解码，并将json字符串内容转换为python字典格式
        # 通过下标取到机器人回复的内容
        with urllib.request.urlopen(s) as response:
            html = response.read()
        # 将获取到的响应内容进行解码，并将json字符串内容转换为python字典格式
        # 通过下标取到机器人回复的内容
            msg=eval(html.decode("utf-8"))["content"].replace('{br}', '\n')
            msg=msg.replace('菲菲', '若若')
            msg=msg.replace('未获取到相关信息','找若若有什么事吗？')
        return msg