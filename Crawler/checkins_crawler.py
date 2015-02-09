# encoding: utf-8
from selenium import webdriver
import re

def toJSON(times, places, shopID):
    result = "{\n"
    result = result + "    \"count\": " + str(len(times)) + ",\n"
    result = result + "    \"checkins\": \n    [\n"
    if len(times) == 0:
        result = result + "    \n    ]\n}"
        return result
    for i in range(0, len(times)-1):
        result = result + "        {\n            \"time\": \"" + times[i] + '\",\n            \"place\": \"' + places[i] + "\",\n" + "            \"shopID\": \"" + shopID[i] + '\"\n        },\n'
    result = result + "        {\n            \"time\": \"" + times[-1] + '\",\n            \"place\": \"' + places[-1] + "\",\n" + "            \"shopID\": \"" + shopID[-1] + '\"\n        }\n    ]\n}'
    return result

def get_checkins(ID, driver):
    driver.get("http://www.dianping.com/member/" + str(ID) + "/checkin")
    for i in range(1,10000):
        try:
            button = driver.find_element_by_id("J_more")
            button.click()
        except:
            break
    html = driver.page_source
    filter1_time = re.compile("<span class=\"time\">(.*?)\u5728</span>\n\t\t\t\t\t\t\t<a href=\"/shop/.*?\" onclick=\"pageTracker.*?;\" target=\"_blank\" title=\"\">.*?</a>")
    filter1 = re.compile("<span class=\"time\">.*?\u5728</span>\n\t\t\t\t\t\t\t<a href=\"/shop/.*?\" onclick=\"pageTracker.*?;\" target=\"_blank\" title=\"\">(.*?)</a>")
    filter1_shopID = re.compile("<span class=\"time\">.*?\u5728</span>\n\t\t\t\t\t\t\t<a href=\"/shop/(.*?)\" onclick=\"pageTracker.*?;\" target=\"_blank\" title=\"\">.*?</a>")
    filter2_time = re.compile("<span class=\"time\">(.*?)\u5728</span><a href=\"/shop/.*?\" tar.*?title=\".*?\">")
    filter2 = re.compile("<span class=\"time\">.*?\u5728</span><a href=\"/shop/.*?\" tar.*?title=\"(.*?)\">")
    filter2_shopID = re.compile("<span class=\"time\">.*?\u5728</span><a href=\"/shop/(.*?)\" tar.*?title=\".*?\">")
    times = filter1_time.findall(html) + filter2_time.findall(html)
    places= filter1.findall(html) + filter2.findall(html)
    shopID = filter1_shopID.findall(html) + filter2_shopID.findall(html)
    if not len(times) == len(places) or not len(places) == len(shopID):
        print("Something wrong...")
    return toJSON(times, places, shopID)
