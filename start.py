#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : B1ain
# Action    : 监控
# Desc      : 监控启动模块
#邮件功能在linux上迷之用不了

from monitor import wbmonitor,bzmonitor,dymonitor
import requests 
import urllib.parse
#import smtplib
#from email.mime.text import MIMEText
#from email.utils import formataddr
#from email.header import Header

#推送函数
def notify(text):
	flag = True
	try:
		qs = urllib.parse.urlencode(dict(
			#一键免费推送信息到手机https://sre24.com/
			token="",#token对应微信
			msg=text,
		))
		rs = requests.get(url="https://sre24.com/api/v1/push?" + qs).json()
		assert int(rs["code"] / 100) == 2, rs
	except Exception as e:
		print(e)
		flag = False
	return flag

def wbweixin(dicts):
	text = "宁关注的："+dicts['nickName']+"发布微博啦\n"
	text += "发送时间: "+dicts['created_at']+"\n"
	flag = notify(text)
	return flag

def bzweixin(dicts):
	text = "宁关注的："+dicts['nickName']+"更新B站啦\n"
	flag = notify(text)
	return flag

def dyweixin(dicts):
	text = "宁关注的："+dicts['nickName']+"更新抖音啦\n"
	flag = notify(text)
	return flag

#def sendMail(dicts):
#	flag = True
#	#使用邮件前记得修改下面参数
#	_user = "" #发件人
#	_pwd  = "" #授权码，不是密码
#	_to   = "" #收件人
#	try:
#		text = u'发送时间: '+dicts['created_at']+u'<br>'
#		text += u'发送内容: <br>'+dicts['text']+u'<br>'
#		text += u'<br>来自: '+dicts['source']
#
#		msg=MIMEText(text.encode('utf-8'),'html','utf-8')
#		msg['Subject']=u"宁关注的："+dicts['nickName']+u"发布微博啦"
#		msg['From'] = formataddr(["微博实时关注",_user])
#		msg['To'] = formataddr(["微博实时关注",_to])
#		#print(msg.as_string())
#		server = smtplib.SMTP_SSL('smtp.sina.com',465)
#		server.login(_user,_pwd)
#		server.sendmail(_user, _to, msg.as_string())
#		server.quit()
#	except Exception as e:
#		print(e)
#		flag = False
#	return flag

def main():
	#微博部分
	w = wbmonitor.weiboMonitor()
	w.getweiboInfo()
	with open('wbIds.txt','r') as f:
		text = f.read()
		if text == '':
			w.getWBQueue()
	newWB = w.startmonitor()
	if newWB is not None:
		print(wbweixin(newWB))#推送成功则输出True
	#B站部分
	b = bzmonitor.bzMonitor()
	b.getbzurl()
	with open('bilibili.txt','r') as f2:
		text = f2.read()
		if text == '':
			b.getBZQueue()
	newBZ = b.startbzmonitor()
	if newBZ is not None:
		print(bzweixin(newBZ))
	#抖音部分
	d = dymonitor.dyMonitor()
	with open('douyin.txt','r') as f3:
		text = f3.read()
		if text == '':
			d.getDYQueue()
	newDY = d.startdymonitor()
	if newDY is not None:
		print(dyweixin(newDY))

if __name__ == '__main__':
	main()
