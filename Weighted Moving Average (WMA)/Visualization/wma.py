import numpy as np
import matplotlib.pyplot as plt
# data = np.random.randint(low=0, high=13, size=(10,))

data = [100, 102, 103, 101, 104, 105, 106, 99, 98, 97, 91, 90, 89, 90, 92, 94, 99, 101]
length = len(data)
period = min(5, length)

# used for updating weighted array
originalArr = np.zeros((period,))
originalArr[0] = data[0]
orignial_sum = originalArr[0]

# weighted array of *period* period
weightedArr = np.zeros((period,))
weightedArr[0] = data[0]*period
weighted_sum = weightedArr[0]

# weighted average
weightedAvg = data[0]
averageArr = np.zeros((length,))
averageArr[0] = weightedAvg

# initalization 
i = 1
denominator = period
while i < period:
  weightedArr = np.subtract(weightedArr, originalArr)                 # decrease older values
  
  value, weightedValue = data[i], data[i] * period
  originalArr[i] = value
  weightedArr[i] = weightedValue                                      # replace oldest value with the newest (most weighted)
  
  weighted_sum = weighted_sum - orignial_sum + weightedValue          # for average calculations
  orignial_sum += value
  
  denominator += (period - i)                                         # only difference between initialization and rest of the process (denominator changes)
  weightedAvg = weighted_sum / denominator
  averageArr[i] = weightedAvg
  
  i += 1

# rest of the process (quite similar w subtle changes)
denominator = int((period * (period+1))/2)                             # if period=5, denominator = 1+2+3+4+5 (weighted)
while (i < length):
  weightedArr = np.subtract(weightedArr, originalArr)                 
  
  value, weightedValue = data[i], data[i] * period
  
  weighted_sum = weighted_sum - orignial_sum + weightedValue        
  orignial_sum = orignial_sum - originalArr[i%period] + value          # remove the old value from the original sum
  
  originalArr[i%period] = value                                        # replace the to be removed value w new one
  weightedArr[i%period] = weightedValue                                
  
  weightedAvg = weighted_sum / denominator
  averageArr[i] = weightedAvg
  
  i += 1

print('original arr: ', originalArr)
print('original sum: ', orignial_sum)
print('weighted arr: ', weightedArr)
print('weighted sum: ', weighted_sum)
print('average arr : ', averageArr)
print('weightedAvg : ', weightedAvg)

plt.plot(data)
plt.plot(averageArr)
plt.show()