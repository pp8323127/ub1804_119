# -- coding:utf-8 --
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# 關閉瀏覽器跳出訊息
prefs = {
    'profile.default_content_setting_values' :
        {
        'notifications' : 2
         }
}
options.add_experimental_option('prefs',prefs)
options.add_argument("--headless")            #不開啟實體瀏覽器背景執行
options.add_argument("--incognito")           #開啟無痕模式

driver = webdriver.Chrome(options=options)
#driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get("https://www.cwb.gov.tw/V8/C/W/Town/Town.html?TID=6703700") #ID改成需要的行政區域，此處為高雄前鎮區
DateTime = driver.find_element_by_id('GT_Time').text
Temp = driver.find_element_by_id('GT_C_T').text
bodyTemp = driver.find_element_by_id('GT_C_AT').text
RelativeHumidity = driver.find_element_by_id('GT_RH').text
Rain = driver.find_element_by_id('GT_Rain').text
Sunrise = driver.find_element_by_id('GT_Sunrise').text
Sunset = driver.find_element_by_id('GT_Sunset').text
driver.quit()
content="\n"+"中西區天氣概況"+"\n"+"系統時間 : "+DateTime+"\n"+"現在溫度 : "+Temp+"°C"+"\n"+"體感溫度 : "+bodyTemp+"°C"+"\n"+"相對溼度 : "+RelativeHumidity+"%"+"\n"+"降雨量 : "+Rain+"mm"+"\n"+"日出時間 : "+Sunrise+"\n"+"日落時間 : "+Sunset

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
