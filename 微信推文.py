import json
import datetime
import random
import string
import requests

# 向网址发送get请求，获取token
r1 = requests.get(
    url = "https://api.weixin.qq.com/cgi-bin/token",
    params={
        'grant_type':'client_credential',
        'appid': 'wxa419d5dbb340507d',
        'secret': 'b034fa19408db754212617671b4f8f49'
    }
)

access_token = r1.json().get('access_token')

wx_id = 'oavHW6Cc5T9kf3eu8l68AbYkHBQM'


# 普通消息推送

"""
body = {
    'touser':wx_id,
    'msgtype':"text",
    'text':{
        "content":'测试消息'
    }
}


r2 = requests.post(
    url='https://api.weixin.qq.com/cgi-bin/message/custom/send',
    params={
        'access_token': access_token
    },
    data=bytes(json.dumps(body,ensure_ascii=False),encoding='utf-8')
)

print(r2.text) 
"""
# 给指定用户发送模板消息


# 获取日期信息
curr_time = datetime.datetime.now()
timestamp=curr_time.date()
todayyear =curr_time.year
todaymonth=curr_time.month
todayday=curr_time.day
week_list = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
num = datetime.date(todayyear,todaymonth,todayday).weekday()
date = str(timestamp)+week_list[num]
d1 = curr_time
d2 = datetime.datetime(2022,8,5)
d3 = datetime.datetime(2022,11,13)
# num1是在一起天数
num1 =(d1-d2).days
# num2是距离100天还剩的天数
num2 = (d3-d1).days

# 获取天气信息
def getWeather(name):
    url = 'http://wthrcdn.etouch.cn/weather_mini'
    response = requests.get(url, {'city': name})
    result = json.loads(response.content.decode())
    data = result.get('data').get('forecast')[0]
    return data
weatherdata = getWeather('赣州市')
weather = weatherdata.get('type')
min_temperature = weatherdata.get('low').replace('低温', '')
max_temperature = weatherdata.get('high').replace('高温 ', '')



# 字体颜色和鸡汤短文数组

colorlist = ['#FFB6C1','#4169E1','#48D1CC','#FFFF33','#8B008B','#00FFFF','#FF1493']
note_enlist = ["Be alayman, be a vagrant life, clean and free.",
               "Who can, as always, not change his appearance.",
               "Arose by any other name would smell assweet.",
               "If you weeped for the missing sunset,youwould miss allthe shining stars.",
               "Youth is so short, butithas notlearned tocherish.",
               "The world is splendid and grand. welcome home.",
               "To be ahappy man, reading,travel, hardwork, care forthe bodyand mind."]
note_cnlist = ['做个俗人，浪荡一生，干净自由。',
               '谁能一如既往，不改初见模样',
               '玫瑰即使换个名字，也依然芬芳',
               '如果你为着错过夕阳而哭泣，那么你就要错群星了。',
               '青春如此短暂，可却还没学会珍惜。',
               '世界灿烂盛大，欢迎回家',
               '做一个幸福的人，读书，旅行，努力工作，关心身体和心情。']
notenum = random.randint(0,7)

body = {
    'touser':wx_id,
    "template_id": "2zWbKvgbC0XRJfCfDd57adKEbp_WI7MTxiMCBufDze4",
    "data":{
        "date":{
            "value":date,
            "color":colorlist[random.randint(0,6)]
        },
        "city":{
            "value":'江西省赣州市',
            "color":colorlist[random.randint(0,6)] 
        },
        "weather":{
            "value":weather,
            "color":colorlist[random.randint(0,6)]
        },
        "min_temperature":{
            "value":min_temperature,
            "color":'#00FF7F'
        },
        "max_temperature":{
            "value":max_temperature,
            "color":'#FFA500'
        },
        "love_day":{
            "value":num1+1,
            "color":colorlist[random.randint(0,6)]
        },
        "birthday":{
            "value":num2,
            "color":colorlist[random.randint(0,6)]
        },
        "note_en":{
            "value":note_enlist[notenum],
            "color":colorlist[random.randint(0,6)]
        },
        "note_ch":{
            "value":note_cnlist[notenum],
            "color":colorlist[random.randint(0,6)]
        },

    }
}


r2 = requests.post(
    url='https://api.weixin.qq.com/cgi-bin/message/template/send',
    params={
        'access_token': access_token
    },
    data=json.dumps(body)
)

print(r2.text)



