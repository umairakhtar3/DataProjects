#!/usr/bin/env python
# coding: utf-8

# # Analysis of Mobile operators download speed and economic indicators in Europe.
# **Purpose**: Main focus of the study is to search the relevant data, collect mobile network speed and economic indicators data. 
# Once data is collected, read the data in jupyter notebook and then select and choose the relevant columns and store them into a file. Once all relevant columns are stored in the table. Next step would be to draw some visualisation to better understand the which countries are performing better using matplot and seaborn.Once this process is done. We move on to conclusion.

# In[96]:


#All the import statements:
import pandas as pd

#Read the Economic_indicator using pandas.

df = pd.read_excel(r'Economic_indicator.xlsx')
df


# #### Renamed Columns Accordingly

# In[ ]:


df.columns = ['Sr.No', 'Country', 'Area_in_sqkm', 'Population_in_sqkm',
       'Urban_Area_in_sqkm', 'Agricultural_areas_sqkm', 'Forest_Areas_sqkm',
       'Population', 'GDP_in_bn_2019', 'GDP_Per_Capita_2019',
       'Mobile_Subcription_2019', 'Mobile_Subcription_per_100_people_2019']


# In[221]:


df.head()


# In[223]:


#Opened Opensignal_data.xlsx using pandas.
df1 = pd.read_excel('Opensignal_data.xlsx')
df1


# In[99]:


#Renmaed the column names
df1.columns


# In[236]:


df1.columns = ['Europe_Opensignal', 'Year', 'Network_type',
       'Download_Speed_Experience_Mbps', 'Upload_Speed_Experience_Mbps',
       'Latency_Experience_ms', '4G_Availability_%',
       'Video_Experience_out_of_100']


# In[107]:


#Checked first 10 rows
df1.head(10)


# In[71]:


df.head()


# In[72]:


df.info()


# In[73]:


df.describe() #Summary of Economic Indicators


# In[74]:


#Took transpose to check the structure of dataframe.
df.describe().transpose()


# In[80]:


df['Country'].head()


# In[86]:


['Country', 'Urban_Area_in_sqkm']


# In[87]:


df[['Country', 'Urban_Area_in_sqkm']].head()


# In[90]:


df.Urban_Area_in_sqkm.head()


# In[95]:


df[['Country', 'Urban_Area_in_sqkm']]


# In[180]:


''''Imported matplot and 
seaborn for visualisatoin of the Economic Indicators.'''
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings


warnings.filterwarnings('ignore')


# In[184]:


#Visualised density vs population.
vis1 = sns.distplot(df['Population'], bins = 5)


# In[156]:


#Visualised Mobile subscriptions per 100 people vs GDP per capita. 
vis2 = sns.boxplot(data=df, x='GDP_Per_Capita_2019', y='Mobile_Subcription_per_100_people_2019') 


# In[183]:


#Visualised Mobile GDP per capita. 
vis4 = sns.distplot(df['GDP_Per_Capita_2019'], bins=10)


# In[178]:


#Plotted Mobile subscriptions per 100 people vs GDP per capita with hue as country.
vis5 = sns.lmplot(data=df, x='GDP_Per_Capita_2019', y='Mobile_Subcription_per_100_people_2019',                   fit_reg=False,hue='Country')


# In[199]:


#Plotted Area_in_sqkm and Mobile_Subcription_per_100_people_2019 using seaborn.
sns.set_theme(style="ticks", palette="pastel")

sns.boxplot(x="Area_in_sqkm", y="Mobile_Subcription_per_100_people_2019",
        palette=["m", "g"],
            data=df)
sns.despine(offset=10, trim=True)


# ### Visualisation for Mobile Network Data

# In[207]:


#Filtered out countries with download speed experience greater than 30.
downloadspeed = df1.loc[ df1['Download_Speed_Experience_Mbps'] >30 ]
downloadspeed


# In[217]:


#Plotted countries and download speed experience.
vis21 = sns.boxplot(data=downloadspeed, x='Europe_Opensignal', y='Download_Speed_Experience_Mbps') 
vis21.set(xlim=(0,5))


# In[219]:


#Filtered out the dataframes on the basis of upload speed experience greater than 10.
uploadspeed = df1.loc[ df1['Upload_Speed_Experience_Mbps'] >=10 ]
uploadspeed
vis22 = sns.boxplot(data=uploadspeed, x='Europe_Opensignal', y='Upload_Speed_Experience_Mbps') 
vis22.set(xlim=(0,5))


# In[238]:


#Filtered out the dataframes on the basis of upload speed experience greater than 10.
videoexperience = df1.loc[ df1['Video_Experience_out_of_100'] >=65 ]
videoexperience
vis22 = sns.boxplot(data=videoexperience, x='Europe_Opensignal', y='Video_Experience_out_of_100') 
vis22.set(xlim=(0,5))


# In[237]:


uploadspeed = df1.loc[ df1['Upload_Speed_Experience_Mbps'] >=10 ]
uploadspeed


# ### Conclusion

# In[ ]:


#In economic indicators, GDP does not seem to have direct impact based on visualisation and data available. More work needs 
#to be done to learn more about the relationship between GDP and mobile subscription. Similarly, there are more varibale needs
#be taken into consideration to develop a relationship between area in square kilometer and mobile subscription. 

#In mobile network data visualisation.Norway,Netherlands and Switzerland came out as winner in download speed experience. It is
#important to know that Netherlands has such dense area and population meaning mobile operators do not have to install many
#base stations to cover the population. Hence, low cost and much better network quality. 

