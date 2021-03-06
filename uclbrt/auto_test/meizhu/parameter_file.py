#coding=utf-8
from selenium import webdriver
from webdata import get_webinfo
from userdata import  get_userinfo
import time
account_name = '13480251015'
account_pwd = "111111a"
list_Ele = []
def getHandler():
    return  webdriver.Firefox()
def openUrl(b,url):
    b.get(url)
def findEle(b,dict):
    #找到元素
    print(dict['name_id'])
    name_Ele = b.find_element_by_id(dict['name_id'])
    pwd_Ele = b.find_element_by_id(dict['pwd_id'])
    login_Ele = b.find_element_by_id(dict['login_id'])
    list_Ele.append(name_Ele)
    list_Ele.append(pwd_Ele)
    list_Ele.append(login_Ele)
    return list_Ele
def sendInfo(list,arg):
    b = 0
    #查到到的元素句柄
    # name_Ele = b.find_element_by_id("requestUsername")
    # pwd_Ele = b.find_element_by_id("requestPassword")
    # login_Ele = b.find_element_by_id("requestSubmit")
    list_key = ['uname','pwd']
    b = 0
    for i in list_key:
        list[b].send_keys("")
        list[b].send_keys(arg[i])
        b+=1
    list[2].click()
#检查结果
def checkResult(b,err,arg,log):
    time.sleep(3)
    result = -1
    try:
        e = b.find_element_by_id(err).text
        msg = '%s %s:error:%s'%(arg['uname'],arg['pwd'],e)
        log.log_write(msg.encode('gbk'))
    except:
        msg = '%s %s:pass'%(arg['uname'],arg['pwd'])
        log.log_write(msg.encode('gbk'))
        result = True
    return result
def loginout(b,dict):
    ele = b.find_element_by_link_text(dict['loginout']).click()
def login_test(dict,user_list):
     #获得句柄
    b = getHandler()
    #打开浏览器
    openUrl(b,dict['url'])
    # log = Loginfo()
    #查找元素，得到一个元组
    list = findEle(b,dict)
    #插入登录信息
    for arg in user_list:
        sendInfo(list,arg)
        result = checkResult(b, dict['errorid'],arg,log)
        if result:
            time.sleep(2)
        #退出登录，重新进入
            loginout(b,dict)
            time.sleep(2)
            list = findEle(b, dict)
            #检查结果
    # log.log_close()
if __name__ == "__main__":
    dict = get_webinfo("./webinfo.txt")
    print(dict)
    #user_list = [{'uname':account_name,'pwd':account_pwd}]
    user_list = get_userinfo('./userinfo.txt')
    login_test(dict,user_list)