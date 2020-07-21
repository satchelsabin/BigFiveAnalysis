import numpy as np
import pandas as pd
import scipy.stats as stats
import pyspark as ps
spark = (ps.sql.SparkSession.builder 
        .master("local[4]") 
        .appName("sparkSQL exercise") 
        .getOrCreate()
        )
sc = spark.sparkContext

df = spark.read.csv("work/Data/IPIP-FFM-data-8Nov2018/data-final.csv")

dfmain = spark.read.csv('../IPIP-FFM-data-8Nov2018/data-final.csv',
                    header=True,       # use headers or not
                    quote='"',         # char for quotes
                    sep="\t",           # char for separation
                    inferSchema=True)  # do we infer

def database_maker(df,string,mode='traits'):
    #Creates database based off of string+digit, correspondes to 10 questions per
    #Inputs: df=database (specifially 5traitsdb) string=three letter string of database titles, mode=['traits','time','other']
    if mode=='traits':
        lst=[f'{string}{i}' for i in range(1,11)]
        return df[[lst]]
    elif mode=='time':
        lst=[f'{string}{i}_E' for i in range(1,11)]
        return df[[lst]]
    elif mode=='other':
        lst=['dateload','screenw','screenh','introelapse','testelapse','endelapse','IPC','country','lat_appx_lots_of_err','long_appx_lots_of_err']
        return df[[lst]]
traits=['EXT','EST','AGR','CSN','OPN']
#Extraversion, ?Neuroticisim?, Agreeableness,Conseention, Openness]
    
#Create Five Traits Databases
dfEXT=database_maker(dfmain,traits[0])
dfEST=database_maker(dfmain,traits[1])
dfAGR=database_maker(dfmain,traits[2])
dfCSN=database_maker(dfmain,traits[3])
dfOPN=database_maker(dfmain,traits[4])
#Create Five Times Databases
dfEXTT=database_maker(dfmain,traits[0],'time')
dfESTT=database_maker(dfmain,traits[1],'time')
dfAGRT=database_maker(dfmain,traits[2],'time')
dfCSNT=database_maker(dfmain,traits[3],'time')
dfOPNT=database_maker(dfmain,traits[4],'time')
#Create Other Database
dfOther=database_maker(dfmain,traits[4],'other')
  


#Making Pandas Dataframes
pdAGR=dfAGR.toPandas()
pdEXT=dfEXT.toPandas()
pdEST=dfEST.toPandas()
pdCSN=dfCSN.toPandas()
pdOPN=dfOPN.toPandas()

pdAGRT=dfAGRT.toPandas()
pdEXTT=dfEXTT.toPandas()
pdESTT=dfESTT.toPandas()
pdCSNT=dfCSNT.toPandas()
pdOPNT=dfOPNT.toPandas()