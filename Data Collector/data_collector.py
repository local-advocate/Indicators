''' Collects data within a given period and an interval of a given ticker. '''
class DataCollector:
    '''
    Arguments:
        from     :   start date, default today - interval
        end      :   end date, default today
        interval :   1M, 5M, 30M, 1H, 2H, 4H, 1D, 1W, 1M, 1Y
        ticker   :   ticker of a company
    '''
    def __init__(self) -> None:
        print('Data Collector')
        # continue: validate args, py dataframes, share mem, etc.