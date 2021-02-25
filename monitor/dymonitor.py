#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : B1ain
# Action    : 狗子抖音
# Desc      : 只关注狗子抖音

import requests,json,sys,re

class dyMonitor():
	def __init__(self, ):
		self.reqHeaders = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
			'Accept': 'application/json',
			'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
			'Accept-Encoding': 'gzip, deflate',
			'X-Requested-With': 'XMLHttpRequest',
			'DNT': '1',
			'Connection': 'close'
		}
		self.url = 'https://www.iesdouyin.com/web/api/v2/user/info/?sec_uid=MS4wLjABAAAAnCz_s5xyosgWTo5lTxKCmoYX1-uiytDsAKBye1LbfDE'
	#获取狗子抖音视频数目
	def getDYQueue(self):
		try:
			res = requests.get(self.url,headers=self.reqHeaders)
			num = res.json()['user_info']['aweme_count']
			with open('douyin.txt','w') as f:
				f.write(str(num)+'\n')
			self.echoMsg('Info','抖音数目获取成功')
		except Exception as e:
			self.echoMsg('Error',e)
			sys.exit()
	#监控函数
	def startdymonitor(self, ):
		returnDict = {}
		try:
			douyin = []
			with open('douyin.txt','r') as f:
				for line in f.readlines():
					line = line.strip('\n')
					douyin.append(line)
			douyin = douyin[0]
			res = requests.get(self.url,headers=self.reqHeaders)
			num = res.json()['user_info']['aweme_count']
			if str(num) != str(douyin):
				with open('douyin.txt','w') as f:
					f.write(str(num))
				self.echoMsg('Info','狗子抖音更新啦!!!')
				returnDict['nickName'] = '狗子'
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