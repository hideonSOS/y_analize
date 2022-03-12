import pandas as pd
import numpy as np
targetpath = 'model/20210804.csv'

df = pd.read_csv(targetpath, index_col=1,encoding='utf-8')

def send_page1(inputbox1,inputbox2):
    page1_dict={
        'Title':inputbox1,
        'View':[i for i in df.iloc[:, 2]],
        'Axis':[i for i in df.iloc[:, 0]],
    }
    return page1_dict


#【ボートレース住之江・イベント配信】JUKUJO DE ナイと！（2022/2/23）
testurl1 = "https://www.youtube.com/embed/v6Qo3DpnmhQ"
#【ボートレース住之江】 １Ｒ－６Ｒ 実況放送～７Ｒ－１２Ｒ マスヒノ大作戦（2022/1/31）
testurl2 = "https://www.youtube.com/embed/_Hod11jijWA"
def send_page3():
    page3_dict={
        'Title':'SAMPLE TITLE',
        'testurl1':testurl1,
        'testurl2':testurl2
    }
    return page3_dict

