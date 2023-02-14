import numpy as np
import matplotlib.pyplot as plt
data = np.random.uniform(low=0.5, high=13.3, size=(500,))

print(data)

head = 0
len = 500
per = 20
sum = 0
i = 1
avg = 0

wmaArray = []
avgArray = []

# Initial values
while i <= per:
  sum += data[i-1]
  avg = sum / i
  avgArray.append(avg)
  wmaArray.append(data[i-1])
  i += 1

i -= 1

while i < len:
  sum -= wmaArray[head]
  sum += data[i]
  avg = sum / per
  avgArray.append(avg)
  wmaArray[head] = data[i]
  head = (head+1)%per
  i += 1
  
print(avgArray)

plt.plot(data)
plt.plot(avgArray)
plt.show()