import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import folium



def make_df(df,string, mode='base'):
    if mode=='base':
        lst=[f'{string}{i}' for i in range(1,11)]
    if mode=='time':
        lst=[f'{string}{i}_E' for i in range(1,11)]
    return df[lst]

def make_mean(df,lst,mode='base'):
    '''Creates a mean based on a users total responses to each unique trait.
        Outputs means as new columns in original database
        Input-
            df = dataframe, lst = list of names of traits (3 letters), mode = ['base','time']
        Output-
            df with new mean column'''
    
    for i in lst:    
        dfv=make_df(df,i,mode)            
        if mode =='base':
            df[f'Mean_{i}']=dfv.mean(axis=1)
        if mode =='time':
            df[f'Mean_{i}E']=dfv.mean(axis=1)    
    return df

def radius_function(df,country):
    '''Takes ratio of total responses from the survey and normalizes them to the total amount of responses
        Input:
            df=Main dataframe
            country=string
        Output:
            radius= (float) respective size of that point in the datafram'''
    radius=(df['country'].value_counts()[f'{country}']/df.shape[0])*100+5
    return radius

def country_trait(df,country):
    '''Takes ratio of total responses from the survey and normalizes them to the total amount of responses
       Input:
            df=Main dataframe
            country=string
       Output:
            radius= (float) respective size of that point in the datafram'''
    country_valuelist=[]
    traitlist=['EXT','EST','OPN','AGR','CSN']
    for i in range(len(traitlist):
            df.f'
    
    return country_valuelist

def heatmap_lst(df,trait_lst):
    mean_lst=[]
    for i in trait_lst:
        mean_lst_row=[]
        for j in range(1,11):
            mean_lst_row.append(maindf[f'{i}{j}'].mean())
        mean_lst.append(mean_lst_row)
    return mean_lst
                   
def new_heatmap_lst(df,trait_lst):
    mean_lst=[]
    for i in trait_lst:
        mean_lst_row=[]
        for j in range(1,11):
            x=maindf[f'{i}{j}'].mean()
            if x<2.25:
                x=6-x
            mean_lst_row.append(x)
        mean_lst.append(mean_lst_row)
    return mean_lst

def make_fol_map(lcd,maindf):
    Map = folium.Map(location=[0,0], zoom_start = 2)
    for i in range(df1.shape[0]):
        try:
            country=lcd.country[i]
            counts=maindf['country'].value_counts()[f'{country}']
            if counts<1000:
                continue
            y= lcd['longitude'][i]
            x= lcd['latitude'][i]
            (folium.CircleMarker((x, y),
             popup=f'Country: {lcd.name[i]}\nResponses: {counts}\nEstimated Major Trait:{}',
             radius=radius_function(maindf,country)).add_to(Map)
            )
        except KeyError:
            continue
    return Map

                   
if __name__=='__main__':                   
maindf=pd.read_csv('../Data/IPIP-FFM-data-8Nov2018/data-final.csv',sep='\t')
littlecountrydata=pd.read_csv('../Data/datasets_2312_3908_countries.csv')
traits=['EXT','EST','AGR','CSN','OPN']

