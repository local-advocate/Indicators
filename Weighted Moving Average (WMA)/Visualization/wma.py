import numpy as np
import matplotlib.pyplot as plt
# data = np.random.randint(low=0, high=13, size=(10,))

data = [100, 102, 103, 101, 104, 105, 106]
per = 5

originalArr = np.zeros((per,))
originalArr[0] = data[0]
orignial_sum = originalArr[0]

weightedArr = np.zeros((per,))
weightedArr[0] = data[0]*per
weighted_sum = weightedArr[0]

weightedAvg = data[0]
averageArr = np.zeros((len(data),))
averageArr[0] = weightedAvg

i = 1
denom = per
while i < per:
  weightedArr = np.subtract(weightedArr, originalArr)
  
  value, weightedValue = data[i], data[i] * per
  originalArr[i] = value
  weightedArr[i] = weightedValue
  
  weighted_sum = weighted_sum - orignial_sum + weightedValue
  orignial_sum += value
  
  denom += (per - i)
  weightedAvg = weighted_sum / denom
  averageArr[i] = weightedAvg
  
  i += 1
  
print('original arr: ', originalArr)
print('original sum: ', orignial_sum)
print('weighted arr: ', weightedArr)
print('weighted sum: ', weighted_sum)
print('average arr : ', averageArr)
print('weightedAvg : ', weightedAvg)