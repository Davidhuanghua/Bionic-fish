# -*- coding:utf-8 -*-

import requests

def up():
    
    url = "http://api.heclouds.com/bindata"

    headers = {
        "Content-Type": "image/jpg", # 
        "api-key": "6XdM1tqZ9xw2cWms=AZa9U=TDBU=", # API-key（在产品概况）
    }

    # device_id是你的设备id（在设备管理）
    # datastream_id是你的数据流名称（在数据流模板）
    querystring = {"device_id": "38964809", "datastream_id": "88888888"}

    # 流式上传
    with open('./photos/3.jpg', 'rb') as f:
        requests.post(url, params=querystring, headers=headers, data=f)

    print('success')

if __name__ == '__main__':
    up()
