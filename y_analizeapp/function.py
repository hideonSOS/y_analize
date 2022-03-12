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

def send_page3():
    page3_dict={
        'Title':'SAMPLE TITLE',
        'View':[i for i in df.iloc[:, 2]],
        'Axis':[i for i in df.iloc[:, 0]],
    }
    return page3_dict