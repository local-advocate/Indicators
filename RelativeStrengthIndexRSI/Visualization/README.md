# Visualization, Relative Strength Index (RSI)

## Description
Calculates the Relative Strength Index of a stream w/ a given period.  


#### Arguments
1. Period           &emsp;&emsp;&emsp;&emsp;&ensp;:&emsp;         '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'. 
2. Interval         &emsp;&emsp;&emsp;&emsp;:&emsp;               '1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo'. Default: 30m.
3. Start            &emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;:&emsp;   yyyy-mm-dd.
4. End              &emsp;&emsp;&emsp;&emsp;&emsp;&ensp;:&emsp;   yyyy-mm-dd.
5. Ticker           &emsp;&emsp;&emsp;&emsp;&ensp;:&emsp;         TCKR of a company.
6. TimePeriod       &nbsp;&emsp;&emsp;:&emsp;                     RSI Time Period. Default: 14.
7. Overbought       &emsp;&emsp;:&emsp;                           Overbought percent line. Default: 70.
8. Oversold         &emsp;&ensp;&emsp;&emsp;:&emsp;               Oversold percent line. Default: 30.
9. Column           &emsp;&emsp;&emsp;&emsp;:&emsp;               'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'. Default: Close.
10. Graph           &nbsp;&emsp;&emsp;&emsp;&ensp;&emsp;:&emsp;   Graph the results or not. Default: False. Call show() explicitly to show plot if graphing.

## How to run
```bash
export PYTHONPATH='path/to/current/working/directory'     # Required for module imports
python rsi.py
```
*RSI* class is meant to be imported. Therefore, it does not take any command line arguments. Initialize it with proper parameters and call the *run* method to run all the steps. If executes successfully, then the values will be stored inside the *rsiArray* class member.  

```python
# EXAMPLE
rsi = RSI(ticker='AMZN', period='1mo', interval='30m', timeperiod=14, graph=True)
rsi.run()
plt.show()
```

A *RunTime Exception* is raise in case of invalid parameters, failed download, or any unexpected error.

## Visualizations
Warning: RSI graph would block the first *timeperiod* values (as they would not be accurate).
* TimePeriod: 10.  
    <p align='center'>
      <img alt='TimePeriod 10' src='https://github.com/NP1Traders/Indicators/blob/main/RelativeStrengthIndexRSI/Visualization/Images/rsi10.png' />
    </p>
  
* TimePeriod: 14.  
    <p align='center'>
      <img alt='TimePeriod 10' src='https://github.com/NP1Traders/Indicators/blob/main/RelativeStrengthIndexRSI/Visualization/Images/rsi14.png' />
    </p> 

## Requirements

>Python 3.7

#### Libraries  
* *yfinance*
* *dataclasses*
* *matplotlib*
* *numpy*

#### Packages
* *Data_Collector*
