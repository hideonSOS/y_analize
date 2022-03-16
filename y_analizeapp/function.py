import pandas as pd
import numpy as np
targetpath = 'model/viewcount.csv'

df = pd.read_csv(targetpath, index_col=0,encoding='utf-8')
# CL = [i for i in df.columns]

def send_page1(inputbox1,inputbox2):
    try:
        page1_dict={
            'Title1':inputbox1,
            'Title2':inputbox2,
            'View1':[i for i in df[str(inputbox1)]],
            'View2':[i for i in df[str(inputbox2)]],
            'Axis':[i for i in df.index],
            'CL':[i[0:8] for i in df.columns],
        }
    except:
        page1_dict={
            'Title1':'Nonevalue',
            'Title2':'Nonevalue',
            'View1':[0 for i in range(0,358)],
            'View2':[0 for i in range(0,358)],
            'Axis':[i for i in range(0,358)],
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

