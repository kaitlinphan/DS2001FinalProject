# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 07:47:09 2022

@author: kaitl
"""

#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

data = pd.read_csv("SpotifyFeatures.csv")

#data.head(5)

#Download and import dataset


# In[4]:


data['genre'].unique()
#See unique values for genre


# In[14]:


data = data.loc[(data.genre == "Rock") | (data.genre == "Rap") | (data.genre == "Pop") | (data.genre == "Country") | (data.genre == "Classical")]
print(data.head(20))
#Choose the 5 genres we want to study: Rock, Rap, Pop, Country, Classical


# In[34]:


#data.head(5)


# In[16]:


data.isnull().sum().sum()

#Find if the data has any NA values (it does not)


# In[20]:


np.unique(data.genre, return_counts=True)

#See if there are any imbalances in the dataset. Country has about 600 fewer elements than the other four,
#but that shouldn't throw off our results too much


# In[49]:


arr = np.unique(data.artist_name, return_counts=True)

df = pd.DataFrame(arr)

df = df.transpose()

df = df.rename(columns={0: 'Artist', 1: 'Appearances'})

df = df.sort_values(by=['Appearances'], ascending=False)
#See if any artists hold more weight

df.head(30)




# further data cleaning
#convet all numeric columns to numeric
data[['popularity', 'acousticness', 'danceability', 'duration_ms', 'energy', 'instrumentalness', 'liveness',
        'loudness', 'speechiness', 'tempo', 'valence',
       ]] = data[['popularity', 'acousticness', 'danceability', 'duration_ms', 'energy', 'instrumentalness', 'liveness',
               'loudness', 'speechiness', 'tempo', 'valence',
       ]].apply(pd.to_numeric)


### DATA VISUALIZATION

# Examine the top 100 songs (based on popularity)
top100songs_df = data.sort_values('popularity', ascending = False).head(100)
print(top100songs_df.head(10))

### top 100 songs by genre
genre_top100, genre_counts_top100 = np.unique(top100songs_df.genre, 
                                              return_counts=True)
fig1, ax1 = plt.subplots()
ax1.pie(genre_counts_top100, labels=genre_top100)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show(ax1)

# Examine the top 20 artists (based on ppopularity)
artistbypop = top100songs_df.groupby('artist_name').sum().sort_values('popularity' ,ascending=False)[:20]
artistbypop=artistbypop.reset_index()
#plot the graph
fig2, ax2 = plt.subplots()
ax2.bar(x='artist_name', height='popularity', data=artistbypop)
plt.xticks(rotation='vertical')
plt.show(ax2)


### boxplots

df1 = pd.DataFrame({'top 100':top100songs_df['danceability'], 'all songs':data['danceability']})
df2 = pd.DataFrame({'top 100':top100songs_df['energy'], 'all songs':data['energy']})
df3 = pd.DataFrame({'top 100':top100songs_df['liveness'], 'all songs':data['liveness']})
df4 = pd.DataFrame({'top 100':top100songs_df['valence'], 'all songs':data['valence']})

fig = plt.figure()
ax3 =fig.add_subplot(2,2,1)
df1.boxplot(ax = ax3)
ax3.set_title('danceability')
ax4 =fig.add_subplot(2,2,2)
df2.boxplot(ax = ax4)
ax4.set_title('energy')
ax5 =fig.add_subplot(2,2,3)
df3.boxplot(ax = ax5)
ax5.set_title('liveness')
ax6 =fig.add_subplot(2,2,4)
df4.boxplot(ax = ax6)
ax6.set_title('valence')
plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)
plt.show(fig)