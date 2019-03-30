# coding=utf-8
import xml.etree.cElementTree as ET
import sys
import requests
import json

url = 'https://oapi.dingtalk.com/robot/send?access_token='

if __name__ == '__main__':
    tree = ET.ElementTree(file=sys.argv[1])
    root = tree.getroot()
    program = {
        "msgtype": "link",
        "link": {
            "text": root[1].text + ':' + root[2].text,
            "title": "sonar扫描报告",
            "picUrl": "",
            "messageUrl": "http://ip:9000/dashboard?id=" + root[1].text + ':' + root[2].text
        }
    }
    headers = {'Content-Type': 'application/json'}
    f = requests.post(url, data=json.dumps(program), headers=headers)
    print f.json()
    print root[1].text + ':' + root[2].text
