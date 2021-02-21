微博，b站，抖音实时监控脚本--W、B、Dmonitor
===========================================

[![PyPI version](https://img.shields.io/badge/python-3-blue.svg)](https://www.python.org/)  [![License](https://img.shields.io/badge/license-GPLv2-red.svg)](https://raw.githubusercontent.com/sqlmapproject/sqlmap/master/LICENSE) 

实时关注微博，b站，抖音某用户动态

详见文章：https://www.blain.top/index.php/2021/02/21/wbdmonitor/

![image](https://github.com/Bla1n/WBDmonitor/blob/main/image/1.png)

特点
====

微博，B站，抖音同时监控

使用
====

安装方法

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
git clone https://github.com/Bla1n/WBDmonitor.git
cd WBDmonitor
pip3 install requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

使用方法

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
python3 start.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

宝塔或者crontab设置定时任务
![image](https://github.com/Bla1n/WBDmonitor/blob/main/image/2.png)

注意事项，执行定时任务请把各py文件内的文件路径替换为绝对路径
