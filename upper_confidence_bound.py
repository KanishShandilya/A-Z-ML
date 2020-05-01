#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
#importing dataset
dataset=pd.read_csv('Ads_CTR_Optimisation.csv').values
#implementing UCB
N=dataset.shape[0]
d=dataset.shape[1]
number_of_selections=[0] * d
sum_of_rewards=[0] * d
ads_selected=[]
total_reward=0
for n in range(N):
    ad,max_upper_bound=0,0
    for i in range(d):
        if number_of_selections[i] > 0:
            avg_reward=sum_of_rewards[i]/number_of_selections[i]
            delta=math.sqrt((3/2) * (math.log(n+1)/number_of_selections[i]))
            upper_bound=avg_reward+delta
        else:
            upper_bound=1e400
        if upper_bound > max_upper_bound:
            max_upper_bound=upper_bound
            ad=i
    ads_selected.append(ad+1)
    number_of_selections[ad]+=1
    reward=dataset[n,ad]
    sum_of_rewards[ad]+=reward
    total_reward+=reward
    
    
    
#To visualize
plt.hist(ads_selected)