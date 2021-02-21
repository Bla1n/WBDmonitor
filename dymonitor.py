#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : B1ain
# Action    : 狗子抖音
# Desc      : 只关注狗子抖音

import requests,json,sys,re

class dyMonitor():
	def __init__(self, ):
		self.reqHeaders = {
			'User-Agent': 'com.ss.android.ugc.aweme/130901 (Linux; U; Android 5.1.1; zh_CN; OPPO R11; Build/NMF26X; Cronet/TTNetVersion:58eeeb7f 2020-11-03 QuicVersion:47946d2a 2020-10-14)',
			'Accept-Encoding': 'gzip, deflate',
			'X-Khronos': '1613835749',
			'X-Gorgon': '0404e037000157bde21de1a7a66c8667ef29e76c1b17b927527e',
			'Connection': 'close'
		}
		self.url = 'https://api5-core-c-lf.amemv.com/aweme/v1/user/profile/other/?sec_user_id=MS4wLjABAAAAnCz_s5xyosgWTo5lTxKCmoYX1-uiytDsAKBye1LbfDE&device_type=OPPO+R11&app_name=aweme&channel=tengxun_new&device_platform=android&iid=1917973789965607&version_code=130900&device_id=1759644089585086&os_version=5.1.1'
	#获取狗子抖音视频数目
	def getDYQueue(self):
		try:
			res = requests.get(self.url,headers=self.reqHeaders)
			num = res.json()['user']['aweme_count']
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
			num = res.json()['user']['aweme_count']
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