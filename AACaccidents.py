#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
get_ipython().run_line_magic('matplotlib', 'inline')
from scipy import stats
from scipy.stats import norm
import statsmodels.api as sm
import datetime as dt


# 1. Saved .xlsx as csv and Imported CSV

# In[ ]:


AAC_accidents = pd.read_csv('_github-AAC_accidents_tagged_data.csv')


# 2. Ensured Date was in DateTime format

# In[ ]:


AAC_accidents['Publication Year'] = pd.to_datetime(AAC_accidents['Publication Year'], yearfirst=True, format = '%Y')
AAC_accidents['Publication Year'] = pd.DatetimeIndex(AAC_accidents['Publication Year']).year
AAC_accidents['Publication Year'] = AAC_accidents['Publication Year'].fillna(0)
AAC_accidents['Publication Year'] = AAC_accidents['Publication Year'].astype(int)


# 3. Replaced NaN for 0

# In[ ]:


AAC_accidents= AAC_accidents.fillna(0)


# 4. I wanted to create a new column with the location of the accident. This would involve matching the Text and accident columns to a list containing Canadian Provinces and US States

# In[ ]:


Provinces_States = ['Alabama', 'Alaska', 'American Samoa', 'Arizona', 'Arkansas', 'California',
             'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia',
             'Guam', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
             'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
             'Minor Outlying Islands', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
             'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota',
             'Northern Mariana Islands', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Puerto Rico',
             'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'U.S. Virgin Islands',
             'Utah', 'Vermont', 'Virginia', 'Washington',
             'West Virginia', 'Wisconsin', 'Wyoming','Alberta', 'British Columbia', 'Manitoba','New Brunswick', 'Newfoundland and Labrador',
                 'Northwest Territories', 'Nova Scotia','Nunavut', 'Ontario', 'Prince Edward Island' , 'PEI',
                 'Quebec','Saskatchewan', 'Yukon']


# In[ ]:





# In[ ]:


AAC_accidents['Location'] = ''


# In[ ]:


for i in range(AAC_accidents.shape[0] - 1):
    title = AAC_accidents['Accident Title'].iloc[i]
    text = AAC_accidents['Text'].iloc[i]
    location = None
    for place in Provinces_States:
        if place in title:
            location = place
            break
        elif place in text:
            location = place
            break
    if location == None:
        print(title)

        print()

    AAC_accidents['Location'].iloc[i]=location
















# In[ ]:


AAC_accidents['Location'].isna().sum()
