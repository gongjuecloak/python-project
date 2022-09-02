import socket
import requests
import os
import json
from dingtalkchatbot.chatbot import DingtalkChatbot
# WebHook地址
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=bc3ea7cd1be17c242c2a1daec01405f491d058e9ecfea40823061ca1eb53c0da'
# 初始化机器人小丁
xiaoding = DingtalkChatbot(webhook)

#指定 api 的接口地址并设定 url 参数
api_url = 'https://v1.hitokoto.cn/?c=b&encode=json'
#向网站 api 发送请求并获取返回的数据
response = requests.get(api_url)
#将 json 数据对象转化为字典
res = json.loads(response.text)
#取出一言正文和出处拼装为字符串
msg = res['hitokoto']+' _____'+'《'+res['from']+'》'
#输出一言
#print(msg)

#xiaoding.send_text(msg, is_at_all=False)

xiaoding.send_markdown(title='一言语录', 
                       text='### 一言即一话，或感动，或开心，或回忆 \n'
                       '> ![每天60S](https://api.03c3.cn/zb/)\n'
                        + msg,
                       is_at_all=False)

file_handle = open('./hitokoto.txt', mode='a')
file_handle.write(msg + '\n')
file_handle.close()
