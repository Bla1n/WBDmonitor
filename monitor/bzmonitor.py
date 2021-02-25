#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : B1ain
# Action    : B站
# Desc      : B站主模块

import requests,json,sys,re

class bzMonitor():
	def __init__(self, ):
		self.reqHeaders = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
			'Content-Type': 'application/x-www-form-urlencoded',
			'Referer': 'https://space.bilibili.com/3345720/video',
			'Connection': 'close',
			'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
		}
		self.uid = ['3345720']#这里添加关注人的uid
	#获取各用户的json连接
	def getbzurl(self):
		try:
			self.bzurl = []
			for i in self.uid:
				url = 'https://api.bilibili.com/x/space/navnum?mid=%s&jsonp=jsonp&callback='%(i)
				self.bzurl.append(url)
		except Exception as e:
			self.echoMsg('Error',e)
			sys.exit()
	#获取各用户当前视频数目
	def getBZQueue(self):
		try:
			for i in self.bzurl:
				res = requests.get(i,headers=self.reqHeaders)
				num = res.json()['data']['video']
				with open('bilibili.txt','a') as f:
					f.write(i+':'+str(num)+'\n')
				self.echoMsg('Info','视频数目获取成功')
		except Exception as e:
			self.echoMsg('Error',e)
			sys.exit()
	#监控函数
	def startbzmonitor(self, ):
		returnDict = {} #获取视频相关内容
		try:
			bilibili = []
			with open('bilibili.txt','r') as f:
				for line in f.readlines():
					line = line.strip('\n')
					bilibili.append(line)
			for i in self.bzurl:
				res = requests.get(i,headers=self.reqHeaders)
				num = res.json()['data']['video']
				url2 = i+':'+str(num)
				if url2 not in bilibili:
					with open('bilibili.txt','a') as f:
						f.write(url2+'\n')
					self.echoMsg('Info','B站视频更新啦!!!')
					uid = re.findall('\d+', i)[0]
					req = requests.get('https://space.bilibili.com/'+str(uid),headers=self.reqHeaders)
					nickName = re.findall('<title>(.*?)的个人空间', req.text)[0]
					returnDict['nickName'] = nickName
					return returnDict
		except Exception as e:
			self.echoMsg('Error',e)
			sys.exit()
	#格式化输出
	def echoMsg(self, level, msg):
		if level == 'Info':
			print('[Info] %s'%msg)
		elif level == 'Error':
			print('[Error] %s'%msg)