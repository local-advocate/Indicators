''' Variant values '''
variant: dict = {
    'V1': 'V1',
    'V2': 'V2',
    'V3': 'V3',
    'V4': 'V4',
    'Invalid': 'Invalid',
}

''' Default values '''
default: dict = {
    'variant': variant['Invalid'],
    'interval': '30m',
    'round': 3,
    'column': 'Open',
    'frequency': 5,
    'alpha': 0.8,
    'timeperiod': 14
}

''' Valid values '''
valid: dict = {
    'period': ['1d','5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max'],
    'interval': ['1m','2m','5m','15m','30m','60m','90m','1h','1d','5d','1wk','1mo','3mo'],
    'column': ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
}

''' Dataframe columns '''
column: dict = {
    'Datetime'  : 0,
    'Open'      : 1,
    'High'      : 2,
    'Low'       : 3,
    'Close'     : 4,
    'Adj Close' : 5,
    'Volume'    : 6,
}
