#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : B1ain
# Action    : 监控
# Desc      : 启动模块

from monitor import wbmonitor,bzmonitor,dymonitor
import requests 
import http.client
import json
import ssl
import urllib.parse
ssl._create_default_https_context = ssl._create_unverified_context

headers = {
	'Connection': 'Keep-Alive',
	'Accept': 'text/html, application/xhtml+xml, */*',
	'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
	'Accept-Encoding': 'gzip, deflate',
	'User-Agent': 'Mozilla/6.1 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
	'Content-Type': 'application/json'
}

#调用的wxpusher平台，数据包详情见https://wxpusher.zjiecode.com/docs/#/
def notify_user(contents, summarys):
	url='http://wxpusher.zjiecode.com/api/send/message'
	datas={
		"appToken":"AT_XXX",
		"content": contents,
		"summary": summarys,
		"contentType":1,
		"topicIds":[],
		"uids":[
			"UID_XXX"
		],
		"url":""
	}
	requests.post(url=url, headers=headers, json=datas).json()

def wbweixin(dicts):
	flag = True
	try:
		summarys = dicts['nickName']+"发布新微博！\n"
		contents = "发送时间: "+dicts['created_at']+"\n"
		notify_user(contents, summarys)
	except Exception as e:
		print(e)
		flag = False
	return flag

def bzweixin(dicts):
	flag = True
	try:
		summarys = dicts['nickName']+"更新B站！\n"
		contents = "[B站]"
		notify_user(contents, summarys)
	except Exception as e:
		print(e)
		flag = False
	return flag

def dyweixin(dicts):
	flag = True
	try:
		summarys = dicts['nickName']+"更新抖音！\n"
		contents = "[抖音]"
		notify_user(contents, summarys)
	except Exception as e:
		print(e)
		flag = False
	return flag

def main():
	#微博部分
	w = wbmonitor.weiboMonitor()
	w.getweiboInfo()
	with open('/root/monitor/wbIds.txt','r') as f:
		text = f.read()
		if text == '':
			w.getWBQueue()
	newWB = w.startmonitor()
	if newWB is not None:
		print(wbweixin(newWB))#发送邮件成功则输出True
	#B站部分
	b = bzmonitor.bzMonitor()
	b.getbzurl()
	with open('/root/monitor/bilibili.txt','r') as f2:
		text = f2.read()
		if text == '':
			b.getBZQueue()
	newBZ = b.startbzmonitor()
	if newBZ is not None:
		print(bzweixin(newBZ))
	#抖音部分
	d = dymonitor.dyMonitor()
	with open('/root/monitor/douyin.txt','r') as f3:
		text = f3.read()
		if text == '':
			d.getDYQueue()
	newDY = d.startdymonitor()
	if newDY is not None:
		print(dyweixin(newDY))

if __name__ == '__main__':
	main()
