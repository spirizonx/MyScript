# encoding: utf-8
import time
import codecs
import os
import random
import profile_crawler
import follows_crawler
import fans_crawler
import checkins_crawler
from selenium import webdriver

def getInRange(first, last, step):
    driver = webdriver.PhantomJS()
    for i in range(first, last+1, step):
        time.sleep(random.randint(2, 3))
        profile_str = profile_crawler.get_page(i, driver).getstr()
        if profile_str.find("\"Year\": 1990") != -1:
            profile_str = profile_crawler.get_page(i, driver).getstr()
            if profile_str.find("\"Year\": 1990") != -1:
                continue
        out = open("../Data/%s_profile.txt"%str(i), 'w')
        out.write(profile_str + "\n")
        out.close()
        time.sleep(random.randint(2, 3))
        out = open("../Data/%s_follows.txt"%str(i), 'w')
        out.write(follows_crawler.get_follows(i, driver).getstr() + "\n")
        out.close()
        time.sleep(random.randint(2, 3))
        out = open("../Data/%s_fans.txt"%str(i), 'w')
        out.write(fans_crawler.get_fans(i, driver).getstr() + "\n")
        out.close()
        time.sleep(random.randint(2, 3))
        out = codecs.open("../Data/%s_checkins.txt"%str(i), 'w', 'utf-8')
        out.write(checkins_crawler.get_checkins(i, driver) + os.linesep)
        out.close()
    driver.close()