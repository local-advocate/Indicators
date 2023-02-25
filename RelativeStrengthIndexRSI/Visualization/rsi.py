from dataclasses import dataclass, field
from numpy import zeros as npZeros, subtract as npSubtract
import matplotlib.pyplot as plt
from matplotlib import gridspec
from DataCollector.data_collector import DataCollector
from DataCollector.datatypes import column, default, valid
from wilderSmoothing import WilderSmoothing

@dataclass(frozen=True,kw_only=True, slots=True)
class RSI:

    ''' Calculates RSI of given timeperiod (10, 14, and so on).
        Arguments:
            timeperiod   :   calculates rsi of last *timeperiod* data points
            overbought   :   overbought line
            oversold     :   oversold line
    '''
    start: str = ''
    end: str = ''
    period: str = ''
    ticker: str
    interval: str = default['interval']                                                  # Default variant 3
    timeperiod: int = default['timeperiod']                                              # Last *timeperiod* points moving average. Default 14.
    column: str = 'Close'                                                                # Default column Close
    data: str = field(init=False, repr=False)
    rsiArray: str = field(init=False, repr=False)
    overbought: int = default['overbought']                                              # overbought line. default 70.
    oversold: int = default['oversold']                                                  # oversold line. default 30.
    graph: bool = False                                                                  # Graph the results. Default: False.
    
    def __validate(self) -> None:

        ''' Validate arguments'''

        # Valid interval
        if self.timeperiod < 1:
            raise AssertionError('Invalid timeperiod. Timeperiod must be >= 1.')
        if self.column not in valid['column']:
            raise AssertionError('Invalid interval. Valid intervals include: ', valid['column'])
        if not 1 <= self.overbought <= 100:
          raise AssertionError('Invalid overbought. Overbought must be 1 <= x <= 100.')
        if not 1 <= self.oversold <= 100:
          raise AssertionError('Invalid overbought. Oversold must be 1 <= x <= 100.')

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
      ''' RSI Algorithm '''
      length = len(self.data)
      timeperiod = min(self.timeperiod, length)

      rsiArr = npZeros((length,))
      
      lastValue = self.data[0]
      change = 0
      curr = self.data[0]
      up, down = 0, 0             # values to add in up average or down average
      rs = 0
      rsi = 0
      epsilon = 0.00000000000000000000001
      
      # averagerators
      upAvg = WilderSmoothing(timeperiod=timeperiod)
      downAvg = WilderSmoothing(timeperiod=timeperiod)
      
      i = 1
      while i < length:
        curr = self.data[i]
        change = curr - lastValue
        lastValue = curr
        
        # price decrease
        if change < 0:
          up = 0
          down = abs(change)
        else:
          up = change
          down = 0
        
        # update averages
        upAvg.add(up)
        downAvg.add(down)
        
        # calculate Relative Strength (RS)
        rs = upAvg.avg / (downAvg.avg+epsilon) if downAvg.avg == 0 else upAvg.avg / downAvg.avg
        
        # calulcate RSI
        rsi = 100 - (100/(1+rs))
        rsiArr[i] = rsi
        
        i += 1


      object.__setattr__(self, 'rsiArray', rsiArr)                # set avgArray, not copied
      return

    def __graph(self)  -> None:
      ''' Graph (does not show, just plots, call show explicitly) '''
      plt.style.use('dark_background')

      fig = plt.figure()
      gs = gridspec.GridSpec(nrows=2, ncols=1, height_ratios=[2, 1])
      
      # Main Graph
      mainGraph = plt.subplot(gs[0])
      color = 'g' if self.data[-1] > self.data[0] else 'r'
      mainGraph.plot(self.data, color=color, label='%s'%self.ticker)
      mainGraph.title.set_text('Relative Strength Index')
      mainGraph.set_ylabel('Price ($)')
      mainGraph.set_xticks([])
      mainGraph.legend(loc='upper right')
      
      # RSI Graph
      zorder = 1
      rsiGraph = plt.subplot(gs[1])
      rsiGraph.plot(self.rsiArray, color='y', label='RSI %s'%self.timeperiod, zorder=zorder)
      rsiGraph.axvspan(0, self.timeperiod, color='w', zorder=zorder+1)
      rsiGraph.set_xlabel('RSI')
      rsiGraph.set_yticks([0, self.oversold, self.overbought, 100])
      rsiGraph.axhline(self.overbought, linestyle='dashed')
      rsiGraph.axhline(self.oversold, linestyle='dashed')
      rsiGraph.legend(loc='upper right')
      
      plt.subplots_adjust(wspace=0, hspace=0)
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
                Relative Strength Index (RSI)
        
        Calculates the Relative String Index of a stream w/ given timeperiod.
        Use the run() method to run the whole program.
        
        Arguments:
            1. Period       : '1d','5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max'. 
            2. Interval     : '1m','2m','5m','15m','30m','60m','90m','1h','1d','5d','1wk','1mo','3mo'. Default: 30m.
            3. Start        :  yyyy-mm-dd.
            4. End          :  yyyy-mm-dd.
            5. Ticker*      :  TCKR of a company.
            6. Timeperiod   :  Last *timeperiod* points moving average. Default 14..
            7. Column       :  'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'. Default: Close.
            8. Graph        :  Graph the results or not. Default: False. Call show() explicitly to show plot if graphing.
        
        '''
        print(info)
