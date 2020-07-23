#importing dataset
dataset=read.delim('Restaurant_Reviews.tsv',quote='',stringsAsFactors = FALSE)

#cleaning text
#install.packages('tm')
#install.packages('SnowballC')

library(tm)
library(SnowballC)

corpus=VCorpus(VectorSource(dataset$Review))
corpus=tm_map(corpus,content_transformer(tolower))
corpus=tm_map(corpus,removeNumbers)
corpus=tm_map(corpus,removePunctuation)
corpus=tm_map(corpus,removeWords,stopwords())
corpus=tm_map(corpus,stemDocument)
corpus=tm_map(corpus,stripWhitespace)
#Creating Bag of Words
dtm=DocumentTermMatrix(corpus)
dtm=removeSparseTerms(dtm,0.999)
#Building classification model
dataset_o=as.data.frame(as.matrix(dtm))
dataset_o=dataset$Liked
dataset$Liked=factor(dataset$Liked,levels=c(0,1))
library(caTools)
split=sample.split(dataset$Liked,SplitRatio = 0.8)
training_set=subset(dataset,split==TRUE)
test_set=subset(dataset,split==FALSE)

library(randomForest)
classifier=randomForest(x=training_set[-692],y=training_set$Liked,ntree = 10)