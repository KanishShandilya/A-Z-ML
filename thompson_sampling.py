#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
#importing dataset
dataset=pd.read_csv('Ads_CTR_Optimisation.csv').values
#Implementing Thompson Sampling ALgo
N,d=dataset.shape[0],dataset.shape[1]
total_rewards=0
ads_selected=[]
number_of_rewards_1=[0]*d
number_of_rewards_0=[0]*d
for n in range(N):
    ad=0
    max_theta=0
    for i in range(d):
        theta=random.betavariate(number_of_rewards_1[i]+1,number_of_rewards_0[i]+1)
        if theta > max_theta:
            max_theta=theta
            ad=i
    ads_selected.append(ad)
    rewards=dataset[n,ad]
    total_rewards+=rewards
    if rewards==1:
        number_of_rewards_1[ad]+=1
    else:
        number_of_rewards_0[ad]+=1
plt.hist(ads_selected)