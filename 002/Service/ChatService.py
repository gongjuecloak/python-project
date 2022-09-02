from send_message.word_detect import *
from random import choice
from data.talk_data.base_talk import others_answer
from random import randint
from data.load_data import read_one
from func.api import check_with_api

def match(msg,talk_data):
	if (len(msg)==1):
		talk_data=read_one()
		return match_oneword(msg,talk_data)
	for row in talk_data:
		if row[0] in msg:
			x=randint(0,len(row[1])-1)
			return [True,row[1][x]]
	return [False,check_with_api(msg)]

def match_oneword(msg,talk_data):
	for row in talk_data:
		if msg in row[0]:
			x=randint(0,len(row[1])-1)
			return [True,row[1][x]]
	return [False,choice(others_answer["no_answer"])]


def talk_to_user(rev,talk_data):#这里可以DIY对私聊和群聊中@白若的操作
	msg=rev["raw_message"]
	#--------------------------------------------------------------------------------------帮助页面
	if_help = help_menu(msg)
	if if_help[0] == True:
		return if_help[1]
	#--------------------------------------------------------------------------------------删除数据
	if_del = del_data(msg,talk_data)
	if if_del[0] == True:
		return if_del[1]
	#--------------------------------------------------------------------------------------添加数据
	if_add = add_data(msg,talk_data)
	if if_add[0] == True:
		return if_add[1]
	#--------------------------------------------------------------------------------------发送自拍
	if_setu = rr_pic(msg)
	if if_setu[0] == True:
		return if_setu[1]
    #--------------------------------------------------------------------------------------发送猫猫图
	if_setu = mao_pic(msg)
	if if_setu[0] == True:
		return if_setu[1]

	return match(msg,talk_data)[1]

def talk_to_gourp(rev,talk_data):#这里可以DIY对群聊的操作
	msg=rev["raw_message"]
	user_id=rev["user_id"]
	group_id=rev["group_id"]
	#--------------------------------------------------------------------------------------检测关键字禁言
	if_ban = detect_ban(msg,user_id,group_id)
	if if_ban[0] == True:
		return if_ban[1]
	#--------------------------------------------------------------------------------------发送猫猫图
	if_setu = mao_pic(msg)
	if if_setu[0] == True:
		return if_setu[1]
	#--------------------------------------------------------------------------------------发送自拍
	if_setu = rr_pic(msg)
	if if_setu[0] == True:
		return if_setu[1]

	if match(msg,talk_data)[0]==True:
		return match(msg,talk_data)[1]

	return ""