# import numpy as np
# import matplotlib.pyplot as plt
# # data = np.random.randint(low=0, high=13, size=(10,))

# data = [100, 102, 103, 101, 104, 105, 106, 99, 98, 97, 91, 90, 89, 90, 92, 94, 99, 101]
# length = len(data)
# period = min(5, length)

# # used for updating weighted array
# originalArr = np.zeros((period,))
# originalArr[0] = data[0]
# orignial_sum = originalArr[0]

# # weighted array of *period* period
# weightedArr = np.zeros((period,))
# weightedArr[0] = data[0]*period
# weighted_sum = weightedArr[0]

# # weighted average
# weightedAvg = data[0]
# averageArr = np.zeros((length,))
# averageArr[0] = weightedAvg

# # initalization 
# i = 1
# denominator = period
# while i < period:
#   weightedArr = np.subtract(weightedArr, originalArr)                 # decrease older values
  
#   value, weightedValue = data[i], data[i] * period
#   originalArr[i] = value
#   weightedArr[i] = weightedValue                                      # replace oldest value with the newest (most weighted)
  
#   weighted_sum = weighted_sum - orignial_sum + weightedValue          # for average calculations
#   orignial_sum += value
  
#   denominator += (period - i)                                         # only difference between initialization and rest of the process (denominator changes)
#   weightedAvg = weighted_sum / denominator
#   averageArr[i] = weightedAvg
  
#   i += 1

# # rest of the process (quite similar w subtle changes)
# denominator = int((period * (period+1))/2)                             # if period=5, denominator = 1+2+3+4+5 (weighted)
# while (i < length):
#   weightedArr = np.subtract(weightedArr, originalArr)                 
  
#   value, weightedValue = data[i], data[i] * period
  
#   weighted_sum = weighted_sum - orignial_sum + weightedValue        
#   orignial_sum = orignial_sum - originalArr[i%period] + value          # remove the old value from the original sum
  
#   originalArr[i%period] = value                                        # replace the to be removed value w new one
#   weightedArr[i%period] = weightedValue                                
  
#   weightedAvg = weighted_sum / denominator
#   averageArr[i] = weightedAvg
  
#   i += 1

# print('original arr: ', originalArr)
# print('original sum: ', orignial_sum)
# print('weighted arr: ', weightedArr)
# print('weighted sum: ', weighted_sum)
# print('average arr : ', averageArr)
# # print('weightedAvg : ', weightedAvg)

# plt.plot(data)
# plt.plot(averageArr)
# plt.show()

from datetime import datetime
from dataclasses import dataclass, field
from pandas_datareader import data as pdr
from multiprocessing import shared_memory
import numpy as np
import yfinance as yf
from Data_Collector.data_collector import DataCollector
from Data_Collector.datatypes import column, default, valid


@dataclass(frozen=True,kw_only=True, slots=True)
class WeightedMA:

    ''' Calculates weighted average a given frequency/period (20MA, 50MA, and so on).
        Arguments:
            period   :   calculates weighted moving average of last *period* data points
            data     :   array of data points (must use SharedMemory for efficiency)      *one can change it manually to use an array
    '''
    start: str = ''
    end: str = ''
    period: str = ''
    ticker: str
    interval: str = default['interval']                                                  # Default variant 3
    frequency: int = default['frequency']                                                # Last *frequency* points moving average. Default 5.
    column: str = default['column']                                                      # Default column Open
    data: str = field(init=False, repr=False)
    
    def __validate(self) -> None:

        ''' Validate arguments'''

        # Valid interval
        if self.frequency < 1:
            raise AssertionError('Invalid frequecy. Frequency must be >= 1.')
        if self.column not in valid['column']:
            raise AssertionError('Invalid interval. Valid intervals include: ', valid['column'])

        # All other arguments checked by Data Collector
        return
      
    def __gather(self) -> None:
        ''' Download the data '''
        try:
          # Collect data
          d = DataCollector(period=self.period, ticker=self.ticker
                            , start=self.start, end=self.end, interval=self.interval)
          d.run()

          # Run on the column
          data = d.data[:,column[self.column]]
          object.__setattr__(self, 'data', data)                              # set data, not copied
        except LookupError as error:
            raise LookupError(error) from error
        return

    
    def run(self) -> None:
        ''' Main '''
        try:
          # Validate args
          self.__validate()
          
          # Collect data
          self.__gather()
          
          # Run algo 
                    
        except (AssertionError,ValueError,IndexError, LookupError, AttributeError) as error:
            raise RuntimeError(error) from error
        return
      

    # def usage(self) -> None:
    #     ''' Usage '''
    #     info = '''
    #             Data Collector
        
    #     Collects the stock data of a given company (w/ a TCKR).
    #     Stores it in a share memory to be used by other processes.
    #     Use the run() method to run the whole program.
        
    #     Arguments:
    #         1. Period       : '1d','5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max'. 
    #         2. Interval     : '1m','2m','5m','15m','30m','60m','90m','1h','1d','5d','1wk','1mo','3mo'. Default: 30m.
    #         3. Start        :  yyyy-mm-dd.
    #         4. End          :  yyyy-mm-dd.
    #         5. Ticker*      :  TCKR of a company.
            
    #     Argument Preference/Variants (from most to least priority)
    #         V1  : Start and Period provided.
    #         V2  : Period and End provided.
    #         V3  : Only Period provided.
    #         V4  : Start and End provided.
    #         V5  : All other combinations are invalid.
        
    #     '''
    #     print(info)

if __name__ == '__main__':
  
  # Run shared memory & Graph
  wma = WeightedMA(period='1d', ticker='AMZN')
  wma.run()
  
  # print(sharedBlock.buf.shape)