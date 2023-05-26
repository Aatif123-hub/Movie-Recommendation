#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[4]:


data=pd.read_csv('Kollywood Movie Dataset (2011 - 2017).csv')
data


# In[6]:


from sklearn.feature_extraction.text import TfidfVectorizer
tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(data['Genre'])


# In[7]:


from sklearn.metrics.pairwise import linear_kernel
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)


# In[8]:


titles = data['Title']
indices = pd.Series(data.index, index=data['Title'])

# Function that get movie recommendations based on the cosine similarity score of movie genres
def genre_recommendations(Title):
    idx = indices[Title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:21]
    movie_indices = [i[0] for i in sim_scores]
    return titles.iloc[movie_indices]


# In[10]:


genre_recommendations('Chennai 2 Singapore').head(20)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




