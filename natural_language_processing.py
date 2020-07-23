#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing dataset
df=pd.read_csv('Restaurant_Reviews.tsv',delimiter='\t',quoting=3)
X=df.iloc[:,0:1].values
#cleaning Text
import nltk
import re
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus=[]
for i in range(X.shape[0]):
    review=re.sub('[^a-zA-Z]',' ',str(X[i]))
    review=review.lower()
    review=review.split()
    ps=PorterStemmer()
    review=[ps.stem(word) for word in review if word not in set(stopwords.words('english'))]
    review=' '.join(review)
    corpus.append(review)