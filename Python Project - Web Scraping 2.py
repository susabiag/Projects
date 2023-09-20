
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 14:54:34 2022

@author: santi
"""

import requests as r
import pandas as pd
import io


filepath = "C:\\Users\\santi\\Downloads\\"
url = 'http://drd.ba.ttu.edu/isqs3358/hw/hw2/'
pg = 'powergeneration.csv'
fi = 'fields.csv'
ven = 'vendors.csv'
out1 = 'Revenue_Report.csv'
out2 = 'areaofexpertise_report.csv'
out3 = 'state_report.csv'

# Dataframe power generation
res_pg = r.get(url + pg)
df_pg = pd.read_csv(io.StringIO(res_pg.text), delimiter=',')

# Dataframe fields
res_fi = r.get(url + fi)
df_fi = pd.read_csv(io.StringIO(res_fi.text), delimiter=',')

# Dataframe vendors
res_ven = r.get(url + ven)
df_ven = pd.read_csv(io.StringIO(res_ven.text), delimiter=',')

# Joining datasets
df_fi.rename(columns={'fieldtxt': 'field'}, inplace=True)
df_pg.rename(columns={'vendor': 'CIK'}, inplace=True)
dfful = df_pg.merge(df_fi, how='inner', on='field')
dffull = dfful.merge(df_ven, how='inner', on='CIK')

# Filling Missing Values for RevenueProduced and kilowatt_production


print('The missing data from kilowatt production  and Revenue Produced was filled with the average grouped by the region_cd and model_cd. ')
print('I know they had correlation and thats what I did that.')
dfmalo = dffull[['kilowatt_production','RevenueProduced','region_cd','model_cd']].groupby(['region_cd','model_cd']).mean()
dfmalo.rename(columns={'kilowatt_production' : 'AvgKiloprod'}, inplace=True)
dfmalo.rename(columns={'RevenueProduced': 'AvgRevenue'}, inplace=True)
dffull=dffull.merge(dfmalo, how='inner', on=['region_cd', 'model_cd'])
dffull['kilowatt_production'][dffull['kilowatt_production'].isnull()] = dffull['AvgKiloprod']
dffull['RevenueProduced'][dffull['RevenueProduced'].isnull()] = dffull['AvgRevenue']


#Cut the first two letters of field and create a new column named state
dffull['State'] = dffull['field'].str[0:2]

#First Output
#Revenue per Killowat =  RevenueProduced / kilowatt_production
#Vendor Commission = RevenueProduced*VendorPercent
#Output this file as Revenue_report.csv

dffull['RevenuePerKilowatt'] = dffull['RevenueProduced'] / dffull['kilowatt_production']
dffull['VendorCommission'] = dffull['RevenueProduced'] * dffull['VendorPercent']
#Outputing file
dfRevRep = dffull[['RevenuePerKilowatt','VendorCommission']].to_csv(filepath + out1, sep = ',', index=False)

#Second Output
#Compute revenue per Area of Expertise
#Compute vendor commission per Area of Expertise
#Output file “areaofexpertise_report.csv
dfArea = dffull['RevenueProduced'].groupby(dffull['AreaOfExpertise']).mean().to_frame()
dfArea['VendorCommissionPerAreaOfExpertise'] = dffull['VendorCommission'].groupby(dffull['AreaOfExpertise']).mean()
dfArea.rename(columns={'RevenueProduced':'RevenuePerAreaOfExpertise'}, inplace=True)
dfArea.to_csv(filepath + out2, sep=',', index=False)


#Third Output
#Compute the average Revenue per states
#Compute the aggregated number of fields that have roads by state.
#Output to file called “state_report.csv”
dfState = dffull['RevenueProduced'].groupby(dffull['State']).mean().to_frame()
HasR = dffull[dffull['hasroads']=='Yes']
dfState['FieldsWithRoad'] = HasR['fieldnumber'].groupby(dffull['State']).count().to_frame()
dfState.to_csv(filepath + out3, sep=',', index=False)



