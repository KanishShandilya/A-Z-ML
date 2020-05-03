#importing dataset
dataset=read.csv('Ads_CTR_Optimisation.csv')

#implementing TSA
d=10
N=10000
ads_selected=integer()
total_rewards=0
number_of_rewards_1=integer(d)
number_of_rewards_0=integer(d)
for(n in 1:N){
  max_random=0
  ad=0
  for(i in 1:d){
    random_beta=rbeta(n=1,shape1=number_of_rewards_1[i]+1,shape2 = number_of_rewards_0[i]+1)
    if(random_beta>max_random){
      max_random=random_beta
      ad=i
    }
  }
  ads_selected=append(ads_selected,ad)
  reward=dataset[n,ad]
  total_rewards=total_rewards+reward
  if(reward == 1){
    number_of_rewards_1[ad]=number_of_rewards_1[ad]+1
  }
  else{
    number_of_rewards_0[ad]=number_of_rewards_0[ad]+1
  }
}

hist(ads_selected)