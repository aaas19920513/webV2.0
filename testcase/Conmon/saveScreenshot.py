#-*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import time
from config import globalparameter as gl
def PngName(name,bool):

    tm = saveTime()
    day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    type = ".png"
    fp = gl.report_path + day + "\\image"+'\\'+bool
    if os.path.exists(fp):
        filename = str(fp)+"\\" + str(tm)+str("_")+str(name)+str(type)
        print filename
        return filename
    else:
        os.makedirs(fp)
        filename = str(fp) + "\\" + str(tm)+str("_")+str(name)+str(type)
        print filename
        return filename



def saveTime():
    # 返回当前系统时间以括号中（2014-08-29-15_21_55）展示
    return time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))

def Screenshot(driver, name,bool):
    image = driver.save_screenshot(PngName(name, bool))
    return image


PngName(u'登录', 'pass')

