from datetime import datetime

# Input Argument for Data Collector Class
dataCollectorArg: dict = {
    "period": str,
    "interval": str,
    "ticker": str,
    "start": str,
    "end": str,
}

''' Variant values '''
variant: dict = {
    'V1': 1,
    'V2': 2,
    'V3': 3,
    'V4': 4,
    'Invalid': -1,
}

''' Default values '''
default: dict = {'variant': variant['Invalid'], 'interval': '30M'}

''' Valid values '''
valid: dict = {
    'period': ['1d','5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max'],
    'interval': ['1m','2m','5m','15m','30m','60m','90m','1h','1d','5d','1wk','1mo','3mo'],
}

''' Collects data within a given period and an interval of a given ticker. '''
class DataCollector:

    '''
    Arguments:
        from     :   start date, default today - interval
        end      :   end date, default today
        period   :   period till the current date
        interval :   1M, 5M, 30M, 1H, 2H, 4H, 1D, 1W, 1M, 1Y
        ticker   :   ticker of a company
    '''

    def __init__(self, args: dataCollectorArg) -> None:
        self.variant = args['variant'] if 'variant' in args else default['variant']        # Default variant 3
        self.interval = args['interval'] if 'interval' in args else default['interval']     # Default interval '30M'
        self.args = args
        # continue: validate args, py dataframes, share mem, dataclasses etc.

    def __variant(self) -> None:

        '''
        Decide what parameter to collect the data
        Preference (highest to lowest):
            1. Start, Period (Variant 1)
            2. Period, End (Variant 2)
            3. Period (Variant 3)
            4. Start, End (Variant 4)
            5. Invalid (Variant 5)
        '''
        
        if 'period' in self.args:
            if 'start' in self.args:
                self.variant = variant['V1']
            elif 'end' in self.args:
                self.variant = variant['V2']
            else:
                self.variant = variant['V3']
        elif 'start' in self.args and 'end' in self.args:
            self.variant = variant['V4']
        else:
            self.variant = variant['Invalid']


    def __validate(self) -> None:

        ''' Validate arguments (according to variants)'''

        # Valid interval
        if self.args['interval'] not in valid['interval']:
            raise AssertionError('Invalid interval. Valid intervals include: ', valid['interval'])

        vrt = self.variant
        if vrt == variant['Invalid']:
            raise IndexError('Invalid input arguments')
        elif vrt == variant['V4']:
            start = datetime.strptime(self.args['start'], '%Y-%m-%d')
            end = datetime.strptime(self.args['end'], '%Y-%m-%d')
            if end < start:
                raise ValueError('Start date must be before the end date')
        else:
            if self.args['period'] not in valid['period']:
                raise AssertionError('Invalid period. Valid periods include: ', valid['period'])
            if vrt == variant['V1']:
                start = datetime.strptime(self.args['start'], '%Y-%m-%d')
            elif vrt == variant['V2']:
                end = datetime.strptime(self.args['end'], '%Y-%m-%d')


    def run(self) -> None:
        ''' Main '''
        try:
            self.__variant()
            self.__validate()
        except Exception as error:
            print('ERROR: ', error)

if __name__ == '__main__':
    d = DataCollector(args={"period": "max", 'interval':'1m'})
    d.run()
