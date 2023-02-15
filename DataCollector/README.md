# Data Collector

## Description
Collects stock price data of a given company or companies within a given timeframe and interval using the *yfinance* library.  

The data is stored in a class member called *data* (for ease of multithreaded testing).  

#### Arguments
1. Period       &emsp;&ensp;:&emsp;         '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'. 
2. Interval     &emsp;:&emsp;               '1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo'. Default: 30m.
3. Start        &emsp;&emsp;&nbsp;:&emsp;   yyyy-mm-dd.
4. End          &emsp;&emsp;&ensp;:&emsp;   yyyy-mm-dd.
5. Ticker       &emsp;&ensp;:&emsp;         TCKR of a company.

#### Variants  
You could provide any of the combinations of *start*, *end*, and *period* arguments for the duration of the data to be downloaded. However, the data will be downloaded with the following preference of order (a.k.a variants):
1. V1         &emsp;&emsp;:&emsp;     *period* and *start* provided.
2. V2         &emsp;&emsp;:&emsp;     *period* and *end* provided.
3. V3         &emsp;&emsp;:&emsp;     Only *period* provided.
4. V4         &emsp;&emsp;:&emsp;     *start* and *end* provided.
5. V5         &emsp;&emsp;:&emsp;     All other combinations are invalid.

## How to run
```
python data_collector.py
```
DataCollector class can be imported. Initialize it with proper parameters and call the *run* method to run all the steps. If executes successfully, then the data will be stored inside the *data* class member.  

A *RunTime Exception* is raise in case of a failed download or any unexpected error.

## Requirements

>Python 3.7

#### Libraries  
* *yfinance*
* *pandas_datareader*
* *datetime*
* *dataclasses*
