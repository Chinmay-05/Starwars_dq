#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

star_wars = pd.read_csv("star_wars.csv", encoding = 'ISO-8859-1')

star_wars = star_wars[pd.notnull(star_wars['RespondentID'])]


# In[2]:


yes_no = {"Yes": True, "No": False}

col = ["Have you seen any of the 6 films in the Star Wars franchise?",
       "Do you consider yourself to be a fan of the Star Wars film franchise?"]

for c in col:
    star_wars[c] = star_wars[c].map(yes_no)


# In[3]:


import numpy as np

name_map = {"Star Wars: Episode I  The Phantom Menace": True, np.nan: False,
            "Star Wars: Episode II  Attack of the Clones": True,
            "Star Wars: Episode III  Revenge of the Sith": True,
            "Star Wars: Episode IV  A New Hope": True,
            "Star Wars: Episode V The Empire Strikes Back": True,
            "Star Wars: Episode VI Return of the Jedi": True}

for col in star_wars.columns[3:9]:
    star_wars[col] = star_wars[col].map(name_map)


# In[4]:


star_wars = star_wars.rename(columns = {"Which of the following Star Wars films have you seen? Please select all that apply.": "seen_1",
        "Unnamed: 4": "seen_2",
        "Unnamed: 5": "seen_3",
        "Unnamed: 6": "seen_4",
        "Unnamed: 7": "seen_5",
        "Unnamed: 8": "seen_6"})


# In[5]:


star_wars[star_wars.columns[9:15]] = star_wars[star_wars.columns[9:15]].astype("float")

star_wars = star_wars.rename(columns = 
        {"Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.": "ranking_1",
        "Unnamed: 10": "ranking_2", "Unnamed: 11": "ranking_3", "Unnamed: 12": "ranking_4",
        "Unnamed: 13": "ranking_5", "Unnamed: 14": "ranking_6"})
                             


# In[6]:


rank_mean = star_wars[star_wars.columns[9:15]].mean()

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt

plt.bar(range(6), rank_mean)


# In[7]:


seen_sum = star_wars[star_wars.columns[3:9]].sum()

plt.bar(range(6), seen_sum)


# In[8]:


males = star_wars[star_wars["Gender"] == "Male"]
females = star_wars[star_wars["Gender"] == "Female"]


# In[9]:


male_rank_mean = males[males.columns[9:15]].mean()
plt.bar(range(6), male_rank_mean)
plt.show()

female_rank_mean = females[females.columns[9:15]].mean()
plt.bar(range(6), female_rank_mean)
plt.show()


# In[10]:


male_seen_sum = males[males.columns[3:9]].sum()
plt.bar(range(6), male_seen_sum)
plt.show()

female_seen_sum = females[females.columns[3:9]].sum()
plt.bar(range(6), female_seen_sum)
plt.show()


# In[11]:


high_school = star_wars[star_wars['Education'] == 'High school degree']
bachelor = star_wars[star_wars['Education'] == 'Bachelor degree']
cg_assc = star_wars[star_wars['Education'] == 'Some college or Associate degree']
graduate = star_wars[star_wars['Education'] == 'Graduate degree']
less_high_school = star_wars[star_wars['Education'] == 'Less than high school degree']


# In[15]:


#Analyzing ranks of movies based on eduction::

degree_col = [high_school, bachelor, cg_assc, graduate, less_high_school]
for col in degree_col:
    plt.bar(range(6), col[col.columns[9:15]].mean())
    plt.show()


# In[16]:


#Analyzing seen moveis on the basis of eductaion:

for col in degree_col:
    plt.bar(range(6), col[col.columns[3:9]].sum())
    plt.show()


# In[107]:


#Cleaning columns 15 to 29 to get information about characters

#Renaming columns
char_map = {'Please state whether you view the following characters favorably, unfavorably, or are unfamiliar with him/her.': 'Character_1',
            "Unnamed: 16": "Character_2", "Unnamed: 17": "Character_3", "Unnamed: 18": "Character_4", 
            "Unnamed: 19": "Character_5", "Unnamed: 20": "Character_6", "Unnamed: 21": "Character_7", 
            "Unnamed: 22": "Character_8", "Unnamed: 23": "Character_9", "Unnamed: 24": "Character_10",
            "Unnamed: 25": "Character_11", "Unnamed: 26": "Character_12", "Unnamed: 27": "Character_13", "Unnamed: 28": "Character_14"}

star_wars = star_wars.rename(columns = char_map)
star_wars['Character_1'].value_counts()


# In[108]:


# Most liked character has the highest sum of Very favorably and Somewhat Favorably
most_liked = {}

for c in star_wars.columns[15:29]:
    a = (char_count[c] == 'Very favorably') | (char_count[c] == 'Somewhat favorably')
    most_liked[c] = a.sum()

print("Most liked character is",list(most_liked.keys())[list(most_liked.values()).index(max(most_liked.values()))],'with', max(most_liked.values()), "votes")

#Least liked character has the highest sum of Somewhat unfavorably and Very unfavorably 
least_liked = {}

for c in star_wars.columns[15:29]:
    a = (char_count[c] == 'Very unfavorably') | (char_count[c] == 'Somewhat unfavorably')
    least_liked[c] = a.sum()

print("Least liked character is",list(least_liked.keys())[list(least_liked.values()).index(max(least_liked.values()))],'with', max(least_liked.values()), "votes")


# In[ ]:





# In[ ]:




