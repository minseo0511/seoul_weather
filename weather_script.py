# openweather api로 요청을해서
# 그 결과를 csv로 저장하는 py
import requests
import csv 
from datetime import datetime 
import os


CITY = "Seoul"
API_KEY = os.getenv("OPENWEATHER_API_KEY")
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

# temp
temp = data["main"]["temp"]

# humidity
humidity = data["main"]["temp"]

# description
description = data["weather"][0]["description"]

timezone = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(temp, humidity, description)

# 위의 4개의 데이터를 가지는 csv파일 생성!!
csv_filename = "seoul_weather.csv"
header = ["timezone", "temp", "humidity", "description"]

# csv가 존재하면 -> True
# csv가 존재하지 않으면 -> False
file_exist = os.path.isdir(csv_filename)

# mode = "a" -> if not is file -> create
# if is file -> write
with open(csv_filename, "a", newline="") as file:
    writer = csv.writer(file)

    # 파일이 존재하지 않는다 -> 헤더가 없다
    if not file_exist:
        writer.writerow(header)

    writer.writerow([timezone, temp, humidity, description]) 

    print("csv 저장 완료!!")
