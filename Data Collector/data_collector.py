from datetime import datetime
from dataclasses import dataclass, field
from datatypes import variant, valid, default
from pandas_datareader import data as pdr
import yfinance as yf

@dataclass(frozen=True,kw_only=True, slots=True)
class DataCollector:

    ''' Collects data within a given period and an interval of a given ticker.
        Arguments:
            start     :   start date, default today - interval
            end      :   end date, default today
            period   :   period till the current date
            interval :   1M, 5M, 30M, 1H, 2H, 4H, 1D, 1W, 1M, 1Y
            ticker   :   ticker of a company
    '''
    start: str = ''
    end: str = ''
    period: str = ''
    ticker: str
    interval: str = default['interval']                                                  # Default variant 3
    _variant: str = field(init=False,repr=True,default=default['variant'])               # Default interval '30M'
    data: str = field(init=False, repr=False)

    def __variant(self) -> str:

        '''
        Decide what parameter to collect the data
        Preference (highest to lowest):
            1. Start, Period (Variant 1)
            2. Period, End (Variant 2)
            3. Period (Variant 3)
            4. Start, End (Variant 4)
            5. Invalid (Variant 5)
        '''

        vrt = ''

        if self.period:
            if self.start:
                vrt = variant['V1']
            elif self.end:
                vrt = variant['V2']
            else:
                vrt = variant['V3']
        elif self.start and self.end:
            vrt = variant['V4']
        else:
            vrt = variant['Invalid']

        return vrt

    def __validate(self) -> None:

        ''' Validate arguments (according to variants)'''

        # Valid interval
        if self.interval not in valid['interval']:
            raise AssertionError('Invalid interval. Valid intervals include: ', valid['interval'])

        vrt = self._variant
        if vrt == variant['Invalid']:
            raise IndexError('Invalid input arguments. Please provide one of the following: period.')
        elif vrt == variant['V4']:
            start = datetime.strptime(self.start, '%Y-%m-%d')
            end = datetime.strptime(self.end, '%Y-%m-%d')
            if end < start:
                raise ValueError('Start date must be before the end date')
        else:
            if self.period not in valid['period']:
                raise AssertionError('Invalid period. Valid periods include: ', valid['period'])
            if vrt == variant['V1']:
                start = datetime.strptime(self.start, '%Y-%m-%d')
            elif vrt == variant['V2']:
                end = datetime.strptime(self.end, '%Y-%m-%d')
        return

    def __gather(self) -> None:
        ''' Download the data '''
        yf.pdr_override()

        if self._variant == variant['V1']:
            pdr.get_data_yahoo(tickers=self.ticker, start=self.start, period=self.period, interval=self.interval)
        elif self._variant == variant['V2']:
            data = pdr.get_data_yahoo(tickers=self.ticker, period=self.period, end=self.end, interval=self.interval)
        elif self._variant == variant['V3']:
            data = pdr.get_data_yahoo(tickers=self.ticker, period=self.period, interval=self.interval)
        else:
            data = pdr.get_data_yahoo(tickers=self.ticker, start=self.start, end=self.end, interval=self.interval)
        if data.empty:
            raise LookupError('Failed to download!')

        data.reset_index(inplace=True)
        # data['Datetime'] = data['Datetime'].dt.date
        data = data.round(decimals=default['round']).to_numpy()
        object.__setattr__(self, 'data', data)                              # set data
        return

    def run(self) -> None:
        ''' Main '''
        try:
            object.__setattr__(self, '_variant', self.__variant())
            self.__validate()
            self.__gather()
        except (AssertionError,ValueError,IndexError, LookupError, AttributeError) as error:
            raise RuntimeError(error) from error
        return

    def usage(self) -> None:
        ''' Usage '''
        info = '''
                Data Collector
        
        Collects the stock data of a given company (w/ a TCKR).
        Stores it in a share memory to be used by other processes.
        Use the run() method to run the whole program.
        
        Arguments:
            1. Period       : '1d','5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max'. 
            2. Interval     : '1m','2m','5m','15m','30m','60m','90m','1h','1d','5d','1wk','1mo','3mo'. Default: 30m.
            3. Start        :  yyyy-mm-dd.
            4. End          :  yyyy-mm-dd.
            5. Ticker*      :  TCKR of a company.
            
        Argument Preference/Variants (from most to least priority)
            V1  : Start and Period provided.
            V2  : Period and End provided.
            V3  : Only Period provided.
            V4  : Start and End provided.
            V5  : All other combinations are invalid.
        
        '''
        print(info)
