import numpy as np
import pandas as pd

a=2.833
b=1.767
c=2.83
d=2.33

rng=np.random.default_rng(123)

highintent=pd.DataFrame({'user_no':np.arange(1,500001)})
highintent['treat']=rng.binomial(1,0.2,size=len(highintent))
highintent.loc[highintent['treat']==0,'kpi']=rng.binomial(1,a/100,size=len(highintent)-highintent['treat'].sum())
highintent.loc[highintent['treat']==1,'kpi']=rng.binomial(1,c/100,size=highintent['treat'].sum())
highintent['intent']='high'
lowintent=pd.DataFrame({'user_no':np.arange(500001,1000001)})
lowintent['treat']=rng.binomial(1,0.8,size=len(lowintent))
lowintent.loc[lowintent['treat']==0,'kpi']=rng.binomial(1,b/100,size=len(lowintent)-lowintent['treat'].sum())
lowintent.loc[lowintent['treat']==1,'kpi']=rng.binomial(1,d/100,size=lowintent['treat'].sum())
lowintent['intent']='low'
comb=pd.concat([highintent,lowintent],ignore_index=True)
comb.to_csv('combined0802.csv',index=False)

highintent05=pd.DataFrame({'user_no':np.arange(1,500001)})
highintent05['treat']=rng.binomial(1,0.5,size=len(highintent05))
highintent05.loc[highintent05['treat']==0,'kpi']=rng.binomial(1,a/100,size=len(highintent05)-highintent05['treat'].sum())
highintent05.loc[highintent05['treat']==1,'kpi']=rng.binomial(1,c/100,size=highintent05['treat'].sum())
highintent05['intent']='high'
lowintent05=pd.DataFrame({'user_no':np.arange(500001,1000001)})
lowintent05['treat']=rng.binomial(1,0.5,size=len(lowintent05))
lowintent05.loc[lowintent05['treat']==0,'kpi']=rng.binomial(1,b/100,size=len(lowintent05)-lowintent05['treat'].sum())
lowintent05.loc[lowintent05['treat']==1,'kpi']=rng.binomial(1,d/100,size=lowintent05['treat'].sum())
lowintent05['intent']='low'
comb05=pd.concat([highintent05,lowintent05],ignore_index=True)
comb05.to_csv('combined0505.csv',index=False)

a=1.75
b=1.75
c=2.5
d=2.5

highintent_same=pd.DataFrame({'user_no':np.arange(1,500001)})
highintent_same['treat']=rng.binomial(1,0.2,size=len(highintent_same))
highintent_same.loc[highintent_same['treat']==0,'kpi']=rng.binomial(1,a/100,size=len(highintent_same)-highintent_same['treat'].sum())
highintent_same.loc[highintent_same['treat']==1,'kpi']=rng.binomial(1,c/100,size=highintent_same['treat'].sum())
highintent_same['intent']='high'
lowintent_same=pd.DataFrame({'user_no':np.arange(500001,1000001)})
lowintent_same['treat']=rng.binomial(1,0.8,size=len(lowintent_same))
lowintent_same.loc[lowintent_same['treat']==0,'kpi']=rng.binomial(1,b/100,size=len(lowintent_same)-lowintent_same['treat'].sum())
lowintent_same.loc[lowintent_same['treat']==1,'kpi']=rng.binomial(1,d/100,size=lowintent_same['treat'].sum())
lowintent_same['intent']='low'
comb_same=pd.concat([highintent_same,lowintent_same],ignore_index=True)
comb_same.to_csv('combined_same0802.csv',index=False)

highintent_same05=pd.DataFrame({'user_no':np.arange(1,500001)})
highintent_same05['treat']=rng.binomial(1,0.5,size=len(highintent_same05))
highintent_same05.loc[highintent_same05['treat']==0,'kpi']=rng.binomial(1,a/100,size=len(highintent_same05)-highintent_same05['treat'].sum())
highintent_same05.loc[highintent_same05['treat']==1,'kpi']=rng.binomial(1,c/100,size=highintent_same05['treat'].sum())
highintent_same05['intent']='high'
lowintent_same05=pd.DataFrame({'user_no':np.arange(500001,1000001)})
lowintent_same05['treat']=rng.binomial(1,0.5,size=len(lowintent_same05))
lowintent_same05.loc[lowintent_same05['treat']==0,'kpi']=rng.binomial(1,b/100,size=len(lowintent_same05)-lowintent_same05['treat'].sum())
lowintent_same05.loc[lowintent_same05['treat']==1,'kpi']=rng.binomial(1,d/100,size=lowintent_same05['treat'].sum())
lowintent_same05['intent']='low'
comb_same05=pd.concat([highintent_same05,lowintent_same05],ignore_index=True)
comb_same05.to_csv('combined_same0505.csv',index=False)