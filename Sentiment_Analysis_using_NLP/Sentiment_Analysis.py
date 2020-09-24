#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t' , quoting=1)
df.head()


# In[3]:


df.info()


# In[4]:


df.isnull().sum()


# In[6]:


df.dtypes


# In[7]:


df.groupby('Liked').size()


# In[8]:


df['Review'][0]


# In[9]:


import re
review = re.sub('[^a-zA-Z]' ,' ' ,df['Review'][0])
print(review) # the use of the sub is to replace something usin something like space


# In[10]:


review = review.lower()
print(review)


# In[13]:


import nltk
nltk.download()


# In[ ]:


# to remove the stopwords 
# what are stopwords?
# its like the prepositions 


# In[16]:


from nltk.corpus import stopwords


# In[17]:


stopwords.words('english')


# In[18]:


# to find the length of the words in the present stopwords
len(stopwords.words('english'))


# In[19]:


review


# In[20]:


review = review.split()
review


# In[21]:


review1 = [ word for word in review if not word in set(stopwords.words('english')) ]
review1   # removed the stopwords from the review 


# In[22]:


x =review
x


# In[24]:


# without the set the use of set is ? ordered words
review2 = [word for word in review if not word in (stopwords.words('english'))]
review2


# In[ ]:


# Stemming  and lemitization best mehtod is lematization
# the use of stemming // it chops the words eg: happily => happy


# In[28]:


from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
review1 = [ps.stem(word) for word in review1] # ps.stem('loving')
review1


# In[35]:


review2 =' ' .join(review1)
review2 # concatinated or else using th ejoin method to join the words instead of commas


# In[38]:


corpus1 = []
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=3)
print(review2)
corpus1.append(review2)
print(corpus1)
X = cv.fit_transform(corpus1)
print(X.toarray())


# In[40]:


df.shape


# In[42]:


import re
import nltk
from nltk.stem.porter import PorterStemmer

corpus = []
for i in range(0 , 1000):
    review = re.sub('[^a-zA-Z]' , " " , df['Review'][i])
    # to lower
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ ps.stem(word) for word in review if not word in set (stopwords.words('english'))]
    review = ' ' .join(review)
    print(review)
    corpus.append(review)


# In[43]:


df.head()


# In[44]:


corpus


# In[46]:


corpus_df = pd.DataFrame(corpus)
corpus_df.head()


# In[47]:


corpus_df['corpus'] = corpus_df
corpus_df.head()


# In[49]:


corpus_df = corpus_df.drop([0] , axis = 1)
corpus_df.head()


# In[50]:


# create the csv file and save it
corpus_df.to_csv('corpus_df.csv')


# In[51]:


type(corpus_df)


# In[52]:


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=1500)


# In[53]:


X = cv.fit_transform(corpus).toarray()
X[0]


# In[55]:


cv.get_feature_names()


# In[56]:


len(cv.get_feature_names())


# In[58]:


y = df.iloc[: , 1].values
y


# In[85]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
   X, y, test_size=0.10, random_state=0)


# In[86]:


# naive bayes classfier 
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train , y_train)


# In[87]:


y_pred = classifier.predict(X_test)


# In[88]:


from sklearn.metrics import confusion_matrix , accuracy_score


# In[89]:


confusion_matrix(y_test , y_pred)


# In[90]:


accuracy_score(y_test , y_pred)


# In[93]:


Review = 'waste of money'
input = [Review]

input_data = cv.transform(input).toarray()

input_pred = classifier.predict(input_data)

if input_pred[0] == 1:
    print("Review is Positive")
else:
    print('Review is Negative')


# In[ ]:





# # SuccessFully Learned NLTK Basics
# # thanks to LetsUpgrade

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




