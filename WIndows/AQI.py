import json, urllib.request
with urllib.request.urlopen("http://opendata2.epa.gov.tw/AQI.json") as url:
    data = json.loads(url.read().decode())
for i in data:
    if i["SiteName"] in "左營的空氣品質":
        if i["Status"] != "":
            response = "{} 的空氣品質{}\nAQI: {}\nPM2.5: {}μg/m3\nPM10: {}\n更新時間為 {}" .format(i["SiteName"], i["Status"], i["AQI"], i["PM2.5_AVG"], i["PM10_AVG"], i["PublishTime"])
        else:
            response = "{} 的空氣品質\nAQI: {}\nPM2.5: {}μg/m3\nPM10: {}\n更新時間為 {}" .format(i["SiteName"], i["AQI"], i["PM2.5_AVG"], i["PM10_AVG"], i["PublishTime"])
        print(response)
    else:
         response = "無法找到這個監測站。"
print(response)