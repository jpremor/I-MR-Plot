import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({'Measurement': [
    3309.3,
3311.2,
3316.5,
3296.7,
3295.2,
3302.6,
3296.2,
3307.8,
3301.6,
3313.2,
3303,
3312.6,
3300.8,
3300.6,
3298.4,
3309.4,
3305.6,
3294.7,
3315.2,
3290.9,
3309.1,
3302.6,
3296.6,
3311.7,
3312.3,
3303.2,
3307.8,
3292.1,
3299.2,
3303.7,
3301.4,
3316.5,
3301.3,
3289.2,
3303.4,
3312.5,
3304.8,
3287.6,
3307.6,
3292.9,
    ]})


data2 = pd.DataFrame({'Moving Range': []})
data2['Moving Range'] = data['Measurement'].diff().abs()

E2 = 2.66   # 1.772 - considering each datapoint an individual measurement compared to the previous. E2 for n=2 is 2.66, for n=3 is 1.772
R_bar = data2['Moving Range'].mean(skipna=True)

Mean = data['Measurement'].mean()
UCL_I = Mean + E2 * R_bar
LCL_I = Mean - E2 * R_bar


data.insert(0, "upper_limit", UCL_I)
data.insert(0, "lower_limit", LCL_I)
# upper_limit = []
# lower_limit = []
# for i in data:
#     upper_limit.append(UCL_I)
#     lower_limit.append(UCL_I)


fig, axs = plt.subplots(1, figsize=(15,6), sharex=True)
axs.plot(data['Measurement'], linestyle='-', marker='o', color='black')
axs.plot(data['upper_limit'], linestyle='-',  color='red')
axs.plot(data['lower_limit'], linestyle='-',  color='red')
print(UCL_I)
print(LCL_I)
input()