# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 08:03:14 2022

@author: santi
"""
import requests as r
import io
import pandas as pd


url = 'http://drd.ba.ttu.edu/isqs3358/Labs/Lab7/team_missing_data.csv'

res = r.get(url)
df = pd.read_csv(io.StringIO(res.text))
#Round 1
df1=df.dropna()
#Round 2
df2 = df
df2['points_scored'].fillna(0,inplace=True)
df2['points_allowed'].fillna(0,inplace=True)
df2['opposing_team'].fillna('-default-',inplace=True)

#Restart for Round 3
res = r.get(url)
df = pd.read_csv(io.StringIO(res.text))
df3 = df
ColumnScore=df3['points_scored'].mean()
ColumnAllowed = df3['points_allowed'].mean()
df3['points_scored'].fillna(ColumnScore,inplace=True)
df3['points_allowed'].fillna(ColumnAllowed,inplace=True)
df3['opposing_team'].fillna('-default-',inplace=True)

#Restart for Round 4
#Did not drop the extra columns because it is better for error checking.
res = r.get(url)
df = pd.read_csv(io.StringIO(res.text))
df4 = df
AvgScored = df[['points_scored','points_allowed']].groupby(df['team_id']).mean()
AvgScored.rename(columns={'points_scored' : 'AvgScored', 'points_allowed' : 'AvgAllowed'}, inplace=True)
df4 = df.merge(AvgScored, how='inner', left_on='team_id', right_index=True)
df4['points_scored'][df4['points_scored'].isnull()] = df4['AvgScored']
df4['points_allowed'][df4['points_allowed'].isnull()] = df4['AvgAllowed']

df4t =df['opposing_team'].value_counts().to_frame()
texdis = df4t.sample(n=1, weights='opposing_team')
for index, row in df4[df4['opposing_team'].isna()].iterrows():
    df4.at[index, 'opposing_team'] = df4t.sample(n=1, weights='opposing_team').index.tolist()[0]
    







## Round 1
print('Round 1')
print('Means')
print(df1[['points_scored','points_allowed']].mean())
print('Median')
print(df1[['points_scored','points_allowed']].median())
print('Variance')
print(df1[['points_scored','points_allowed']].var())
print('Mean by opposing team')
print('The distribution has changed from the original but has the lowest distribution between points scored and points allowed.')
print('Because there are not that spread out')

print('---------------------------------------------------------------')

##Round 2
print('Round 2')
print('Means')
print(df2[['points_scored','points_allowed']].mean())
print('Median')
print(df2[['points_scored','points_allowed']].median())
print('Variance')
print(df2[['points_scored','points_allowed']].var())
print('Mean by opposing team')
print('The distribution has changed from the original, and has the highest distribution of all Rounds')
print('Due to the fact that that the points scored and allowed are the most spread out.')
print('---------------------------------------------------------------')

##Round 3
print('Round 3')
print('Means')
print(df3[['points_scored','points_allowed']].mean())
print('Median')
print(df3[['points_scored','points_allowed']].median())
print('Variance')
print(df3[['points_scored','points_allowed']].var())
print('Mean by opposing team')
print('The distribution has changed from the original but has the second lowest distribution between points scored and points allowed.')
print('Because there are not that spread out')
print('---------------------------------------------------------------')

##Round 4
print('Round 4')
print('Means')
print(df4[['points_scored','points_allowed']].mean())
print('Median')
print(df4[['points_scored','points_allowed']].median())
print('Variance')
print(df4[['points_scored','points_allowed']].var())
print('Mean by opposing team')
print('The distribution has changed from the original but has the third lowest distribution between points scored and points allowed.')
print('Because there are not that spread out')
