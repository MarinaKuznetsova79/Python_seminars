#Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
#из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без
#get_dummies?

import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10 
random.shuffle(lst)
df = pd.DataFrame({'whoAmI':lst})
print(df)

df1 = pd.DataFrame({'whoAmI_human':df['whoAmI'].apply(lambda x: 1 if x == 'human' else 0)})
whoAmI_robot = pd.DataFrame({'whoAmI_robot':df['whoAmI'].apply(lambda x: 1 if x == 'robot' else 0)})
df1['whoAmI_robot'] = whoAmI_robot

df1
   whoAmI
0   human
1   human
2   human
3   robot
4   robot
5   human
6   robot
7   human
8   robot
9   robot
10  robot
11  robot
12  robot
13  human
14  human
15  human
16  robot
17  robot
18  human
19  human
whoAmI_human	whoAmI_robot
0	1	0
1	1	0
2	1	0
3	0	1
4	0	1
5	1	0
6	0	1
7	1	0
8	0	1
9	0	1
10	0	1
11	0	1
12	0	1
13	1	0
14	1	0
15	1	0
16	0	1
17	0	1
18	1	0
19	1	0
pd.get_dummies(df)
whoAmI_human	whoAmI_robot
0	1	0
1	1	0
2	1	0
3	0	1
4	0	1
5	1	0
6	0	1
7	1	0
8	1	0
9	0	1
10	0	1
11	0	1
12	1	0
13	0	1
14	1	0
15	1	0
16	0	1
17	0	1
18	0	1
19	1	0
 
 
 
 
 
 
