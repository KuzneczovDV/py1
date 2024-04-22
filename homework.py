import pandas as pd 
import random 
 
lst = ['robot'] * 10 
lst += ['human'] * 10 
random.shuffle(lst) 
data = pd.DataFrame({'whoAmI':lst}) 
data.head()
# 2 способ 
 
list2 = ['robot','human'] 
 
for i in list2: 
  data.loc[data['whoAmI'] == i, i] = 1 
  data.loc[data['whoAmI'] != i, i] = 0 
print(data.head())
