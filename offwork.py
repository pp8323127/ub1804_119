# -- coding:utf-8 --
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import requests

content="\n"+"下班下班下班下班下班下班下班下班下班下班下班下班下班下班下班下班下班下班下班下班下班下班下班下班下班下班下班下班下班下班"+"\n"+"肉熊哥哥快去收店"

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
