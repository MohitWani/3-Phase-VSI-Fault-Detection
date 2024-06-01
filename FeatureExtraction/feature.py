import pandas as pd
import numpy as np

def get_Iq(data:pd.DataFrame)->pd.DataFrame:
    return (1.0/(2**0.5))*(data.iloc[:,1]-data.iloc[:,2])

def get_Id(data:pd.DataFrame)->pd.DataFrame:
    ia = ((2./3)**0.5)*data.iloc[:,0]
    ib = (1./(6**0.5))*data.iloc[:,1]
    ic = (1./(6**0.5))*data.iloc[:,2]

    result = ia - ib - ic
    return result

def get_Iq_Id(path:str)->pd.DataFrame:
    path = pd.read_excel(path, header=None, usecols=[0, 1, 2], names=['IA', 'IB', 'IC'])
    
    path['IQ'] = get_Iq(path)
    path['ID'] = get_Id(path)
    
    return path

def get_features(full:pd.DataFrame,x:pd.DataFrame,y:pd.DataFrame)->pd.DataFrame:
    med_x = np.median(x)
    med_y = np.median(y)
    
    dummy = pd.DataFrame([[med_x,med_y]])
    
    med_y1 = full.loc[x<=med_x,['IQ','ID']]
    med_x1 = full.loc[y<=med_y,['IQ','ID']]
    
    a = med_y1.head(1)
    b = med_y1.tail(1)
    c = med_x1.head(1)
    d = med_x1.tail(1)
    
    return pd.DataFrame(np.hstack((dummy,a,b,c,d)),columns=['median_x','median_y','points_x1','points_y1','points_x2','points_y2','points_x3','points_y3','points_x4','points_y4'])

def get_array(path):
    data = path.iloc[:1,:2]
    data = np.array(data)
    return data