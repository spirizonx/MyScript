# encoding: utf-8
import random
import time
from selenium import webdriver

class User(object):
    def __init__(self):
        super(User, self).__init__()
        self.data = {
            'ID' : 0,#用户ID
            'Gender' : 'unknown',#性别
            'Checkin' : -1,#签到
            'Reg_date' : {'Year':1990, 'Month':1, 'Day':1},#注册时间
            'Last_Login' : {'Year':1990, 'Month':1, 'Day':1},#最后登录
            'Follows' : -1,#关注
            'Fans' : -1,#粉丝
            'EXP' : -1,#贡献值
            'Review' : -1,#点评
            'Wishlist' : -1,#收藏
            'Picture' : -1,#图片
            'Bangdan' : -1,#榜单
            'Post' : -1 #帖子
        }

    def getstr(self):
        result = "{\n"\
        + '    \"ID\": \"' + str(self.data['ID']) + "\",\n"\
        + '    \"Gender\": \"' + self.data['Gender'] + "\",\n"\
        + '    \"Checkin\": ' + str(self.data['Checkin']) + ",\n"\
        + '    \"Reg_date\": \n    {\n'\
        + '        \"Year\": ' + str(self.data['Reg_date']['Year']) + ',\n'\
        + '        \"Month\": ' + str(self.data['Reg_date']['Month']) + ',\n'\
        + '        \"Day\": ' + str(self.data['Reg_date']['Day']) + "\n    },\n"\
        + '    \"Last_Login\": \n    {\n'\
        + '        \"Year\": ' + str(self.data['Last_Login']['Year']) + ',\n'\
        + '        \"Month\": ' + str(self.data['Last_Login']['Month']) + ',\n'\
        + '        \"Day\": ' + str(self.data['Last_Login']['Day']) + "\n    },\n"\
        + '    \"Follows\": ' + str(self.data['Follows']) + ",\n"\
        + '    \"Fans\": ' + str(self.data['Fans']) + ",\n"\
        + '    \"EXP\": ' + str(self.data['EXP']) + ",\n"\
        + '    \"Review\": ' + str(self.data['Review']) + ",\n"\
        + '    \"Wishlist\": ' + str(self.data['Wishlist']) + ",\n"\
        + '    \"Picture\": ' + str(self.data['Picture']) + ",\n"\
        + '    \"Bangdan\": ' + str(self.data['Bangdan']) + ",\n"\
        + '    \"Post\": ' + str(self.data['Post']) + "\n}"
        return result

def get_page(ID, driver):
    url = "http://www.dianping.com/member/" + str(ID)
    driver.get(url)
    content = driver.page_source
    content = content.split("\n")
    user = User()
    user.data['ID'] = ID
    for line in content:
        if line.find("class=\"woman\"></i>") != -1:
            user.data['Gender'] = 'woman'
        if line.find("class=\"man\"></i>") != -1:
            user.data['Gender'] = 'man'
        if line.find(u">签到(") != -1:
            user.data['Checkin'] = get_number(line, u">签到(", ")")
        if line.find(u"注册时间：</span>") != -1:
            user.data['Reg_date'] = get_date(line, u"注册时间：</span>", "<")
        if line.find(u"最后登录：</span>") != -1:
            user.data['Last_Login'] = get_date(line, u"最后登录：</span>", "<")
        if line.find(u"关注</span><strong>") != -1:
            user.data['Follows'] = get_number(line, u"关注</span><strong>", "<")
        if line.find(u"粉丝</span><strong>") != -1:
            user.data['Fans'] = get_number(line, u"粉丝</span><strong>", "<")
        #added in Version 2:
        if line.find(u"贡献值：</span><span id=\"J_col_exp\">") != -1:
            user.data['EXP'] = get_number(line, u"贡献值：</span><span id=\"J_col_exp\">", "<")
        if line.find(u">点评(") != -1:
            user.data['Review'] = get_number(line, u">点评(", ")")
        if line.find(u">收藏(") != -1:
            user.data['Wishlist'] = get_number(line, u">收藏(", ")")
        if line.find(u">图片(") != -1:
            user.data['Picture'] = get_number(line, u">图片(", ")")
        if line.find(u">榜单(") != -1:
            user.data['Bangdan'] = get_number(line, u">榜单(", ")")
            #It's difficult to translate "榜单"...
        if line.find(u">帖子(") != -1:
            user.data['Post'] = get_number(line, u">帖子(", ")")
    return user

def get_number(line, pre, pos):
    i = line.find(pre)
    j = line.find(pos, i+len(pre))
    return int(line[i+len(pre):j])

def get_date(line, pre, pos):
    i = line.find(pre)
    i = i + len(pre)
    return {'Year':int(line[i:i+4]), 'Month':int(line[i+5:i+7]), 'Day':int(line[i+8:i+10])}


