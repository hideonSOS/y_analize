import pandas as pd
import numpy as np
targetpath = 'model/20210804.csv'

df = pd.read_csv(targetpath, index_col=1)

def send_page1():
    page1_dict={
        'Title':'SAMPLE TITLE',
        'View':[i for i in df.iloc[:, 2]],
        'Axis':[i for i in df.iloc[:, 0]],
    }
    return page1_dict