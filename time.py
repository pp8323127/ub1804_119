# -- coding:utf-8 --
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import requests
import datetime

ISOTIMEFORMAT = '%H:%M:%S'
theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)

content="\n"+"『肉熊哥哥報時間』"+"\n"+theTime

def lineNotifyMessage(token, msg):
    headers = {
          "Authorization": "Bearer " + token, 
          "Content-Type" : "application/x-www-form-urlencoded"
      }
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code

token = '6ZuSFknc3D9goTQMouQ7O1Cm7nQMcKeKthyl6v4vsz0' #修改為自己的權杖內容，肉熊
#token = 'dK81KKbB0bTe0dVWAohdZgJ5IkMYT7raeOKOpeHfUuj' #修改為自己的權杖內容，個人
lineNotifyMessage(token, content)
