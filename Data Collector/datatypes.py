''' Variant values '''
variant: dict = {
    'V1': 'V1',
    'V2': 'V2',
    'V3': 'V3',
    'V4': 'V4',
    'Invalid': 'Invalid',
}

''' Default values '''
default: dict = {'variant': variant['Invalid'], 'interval': '30m'}

''' Valid values '''
valid: dict = {
    'period': ['1d','5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max'],
    'interval': ['1m','2m','5m','15m','30m','60m','90m','1h','1d','5d','1wk','1mo','3mo'],
}
