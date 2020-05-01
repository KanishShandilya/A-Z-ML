#importing dataset
dataset=read.csv('Ads_CTR_Optimisation.csv')

#Implementing UCB
N=nrow(dataset)
d=ncol(dataset)
number_of_selections=integer(d)
sum_of_rewards=integer(d)
total_rewards=0
ads_selected=integer()
for(n in 1:N){
  max_upper_bound=0
  ad=0
  for(i in 1:d){
    if(number_of_selections[i] > 0){
    avg_reward=sum_of_rewards[i]/number_of_selections[i]
    delta=sqrt(3/2 * log(n)/number_of_selections[i])
    upper_bound=avg_reward+delta
    }
    else{
      upper_bound=1e400
    }
    if(upper_bound > max_upper_bound){
      max_upper_bound=upper_bound
      ad=i
    }
  }
  ads_selected=append(ads_selected,ad)
  number_of_selections[ad]=number_of_selections[ad]+1
  reward=dataset[n,ad]
  sum_of_rewards[ad]=sum_of_rewards[ad]+reward
  total_rewards=total_rewards+reward
}


hist(ads_selected)