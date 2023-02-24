from dataclasses import dataclass, field
from numpy import zeros as npZeros, subtract as npSubtract
from matplotlib.pyplot import style as pltStyle, plot as pltPlot, title as pltTitle, xlabel as pltXlabel, ylabel as pltYlabel, legend as pltLegend, show as pltShow
from discountAverage import DiscountedAveragerator
from DataCollector.data_collector import DataCollector
from DataCollector.datatypes import column, default, valid

@dataclass(frozen=True,kw_only=True, slots=True)
class ExponetialWMA:

    ''' Calculates exponential weighted average a given frequency/period (20MA, 50MA, and so on).
        Arguments:
            period   :   calculates weighted moving average of last *period* data points
            data     :   array of data points (must use SharedMemory for efficiency)      *one can change it manually to use an array
    '''
    start: str = ''
    end: str = ''
    period: str = ''
    ticker: str
    interval: str = default['interval']                                                  # Default variant 3
    column: str = default['column']                                                      # Default column Open
    data: str = field(init=False, repr=False)
    alpha: int = default['alpha']                                                        # Default value 0.8
    averageArray: str = field(init=False, repr=False)
    graph: bool = False                                                                  # Graph the results. Default: False.
    
    def __validate(self) -> None:

        ''' Validate arguments'''

        # Valid interval
        if not 0 <= self.alpha <= 1:
            raise AssertionError('Invalid alpha. ALpha must be between 0 and 1.')
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

    def __algo(self) -> None:
      ''' EWMA Algorithm '''
      length = len(self.data)
      
      averageArr = npZeros((length,))
      averageArr[0] = self.data[0]

      averagerator = DiscountedAveragerator(alpha=self.alpha)
      
      i = 1
      while (i < length):
        curr = self.data[i]
        averagerator.add(curr)
        averageArr[i] = averagerator.avg
        i += 1
      
      object.__setattr__(self, 'averageArray', averageArr)                # set avgArray, not copied
      return

    def __graph(self)  -> None:
      ''' Graph (does not show, just plots, call show explicitly) '''
      # Green if closes higher than opens
      pltStyle.use('dark_background')
      color = 'g' if self.data[-1] > self.data[0] else 'r'
      pltPlot(self.data, color=color, label='%s'%self.ticker)
      pltPlot(self.averageArray, color='c', ls='dashed', label='EMA (%s)'%self.alpha)
      
      pltTitle('Exponential Weighted Moving Average')
      pltXlabel('Datetime')
      pltYlabel('Price ($)')
      pltLegend(loc='upper right')
      
      return
    
    def run(self) -> None:
        ''' Main '''
        try:
          # Validate args
          self.__validate()
          
          # Collect data
          self.__gather()
          
          # Run algo 
          self.__algo() 
          
          # Graph
          if self.graph:
            self.__graph()

        except (AssertionError,ValueError,IndexError, LookupError, AttributeError) as error:
            raise RuntimeError(error) from error
        return

    def usage(self) -> None:
        ''' Usage '''
        info = '''
                Exponential Weighted Moving Average (EWMA)
        
        Calculates the Exponential Weighted Moving Average of a stream w/ given alpha.
        Use the run() method to run the whole program.
        
        Use for short term averages only.
        
        Arguments:
            1. Period       : '1d','5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max'. 
            2. Interval     : '1m','2m','5m','15m','30m','60m','90m','1h','1d','5d','1wk','1mo','3mo'. Default: 30m.
            3. Start        :  yyyy-mm-dd.
            4. End          :  yyyy-mm-dd.
            5. Ticker*      :  TCKR of a company.
            6. Alpha        :  [0, 1]. Lower the alpha, less weight to previous values. Ex: 20day alpha: 0.4, 200day alpha: 0.9.
            7. Column       :  'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'. Default: Open.
            8. Graph        :  Graph the results or not. Default: False. Call show() explicitly to show plot if graphing.
        
        '''
        print(info)

if __name__ == '__main__':
  ewma = ExponetialWMA(ticker='AMZN', period='1mo', interval='15m', alpha=0.5, graph=True)
  ewma.run()
  pltShow()