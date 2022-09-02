import requests
import json
import os
import re
from random import choice
from data.load_data import read_one
from data.load_data import read_imglist
group = json.load(open("./config.json", encoding='utf-8'))["group"]
apikey= json.load(open("./config.json", encoding='utf-8'))["apikey"]
ban_words = json.load(open("./config.json", encoding='utf-8'))["ban_words"]
mao_path = json.load(open("./config.json", encoding='utf-8'))["mao_path"]
rr_path = json.load(open("./config.json", encoding='utf-8'))["rr_path"]
key_words = json.load(open("./config.json", encoding='utf-8'))["key_words"]

help_base = "这里是帮助菜单：\n"
help_base += "1.发送猫猫图，返回一张猫猫表情包\n"
help_base += "2.发送若若爆照，可以看到我的自拍\n"
help_base += "3.发送城市+天气，获取城市天气\n"
help_base += "4.私聊调教对话 例如aaa+bbb \n"
help_base += "那么发送aaa就会返回bbb啦~\n"
help_base += "可以发送rmaaa+bbb删除对话哦~\n"
help_base += "快来和若若聊天吧~\n"

def help_menu(msg):
	if msg == "help":
		return [True,help_base]
	return [False]

def add_data(msg,all_data):
	one=False
	if "＋" in msg:
		return add_sxt_data(msg,all_data)
	if msg.count("+") != 1:
		return [False]
	if "/" in msg or "|" in msg:
		return [True,"不能含有/或|呀~"]
	if msg.split("+")[1]=="":
		return [False]
	msg = msg.split("+")
	if len(msg[0])< 2:
		one=True
		all_data=read_one()
	for row in all_data:
		if msg[0] == row[0]:
			if msg[1] in row[1]:
				return [True,"oh，这句话我已经会啦，不用再教我啦~"]
			row[1].append(msg[1])
			save_data(all_data,one)
			return [True,"添加成功！"]
	all_data.append([msg[0], [msg[1]]])
	save_data(all_data,one)
	return [True,"添加成功！"]

def save_data(all_data,one):
	if one:
		f=open("./data/talk_data/oneword","w",encoding='UTF-8')
	else:
		f = open("./data/talk_data/words","w",encoding='UTF-8')
	for row in all_data:
		temp = row[0]+"|"+"".join([i+"/" for i in row[1]])
		f.writelines(temp+"\n")
	f.close()

def del_data(del_data,all_data):
	one=False
	if del_data[:2] != "rm":
		return [False]
	if "＋" in del_data:
		msg = del_data[2:].split("＋")
	else:
		msg = del_data[2:].split("+")
	if len(msg[0])<2:
		one=True
		all_data=read_one()

	for i in range(len(all_data)):
		if msg[0] == all_data[i][0]:
			if len(all_data[i][1]) == 1:
				all_data.pop(i)
				save_data(all_data,one)
				return [True,"已经删除啦~"]
			all_data[i][1].remove(msg[1])
			save_data(all_data,one)
			return [True,"已经删除啦~"]
	return [True,"删除出错啦~"]

def mao_pic(msg):
    if msg in ["来张猫猫图", "来张猫图", "猫图", "喵图", "maomao","猫猫图","猫","喵","猫猫"]:
        setu_list = os.listdir(mao_path)
        local_img_url = "[CQ:image,file=file://"+mao_path+choice(setu_list)+"]"
        return [True, local_img_url]
    return [False]

def rr_pic(msg):
	if "若若爆照" in msg:
		setu_list = os.listdir(rr_path)
		local_img_url = "[CQ:image,type=flash, file=file://"+rr_path+choice(setu_list)+"]"
		return [True, local_img_url]
	return [False]

def detect_ban(msg,user_id,group_id):
	if group_id not in group:
		return [False]

	for i in ban_words:
		s = re.search(i,msg)
		if not s == None:
			data = {
			'user_id':user_id,
			'group_id':group_id,
			'duration':60
			}
			cq_url = "http://127.0.0.1:5700/set_group_ban"
			requests.post(cq_url,data=data)
			return [True,"不要说不该说的话啦~"]
	return [False]
