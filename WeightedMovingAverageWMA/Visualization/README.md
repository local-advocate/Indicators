# Visualization, Weighted Moving Average (WMA)

## Description
Calculates the Weighted Moving Average of a stream w/ given frequency.

Uses *Data Collector* for collecting data.

#### Arguments
1. Period       &emsp;&ensp;:&emsp;         '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'. 
2. Interval     &emsp;:&emsp;               '1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo'. Default: 30m.
3. Start        &emsp;&emsp;&nbsp;:&emsp;   yyyy-mm-dd.
4. End          &emsp;&emsp;&ensp;:&emsp;   yyyy-mm-dd.
5. Ticker       &emsp;&ensp;:&emsp;         TCKR of a company.
6. Freq.        &emsp;&emsp;:&emsp;         Moving average of latest *frequency* data points. Default: 5.
7. Column       &emsp;:&emsp;               'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'. Default: Open.
8. Graph        &ensp;&emsp;:&emsp;         Graph the results or not. Default: False. Call show() explicitly to show plot if graphing.

## How to run
```bash
export PYTHONPATH='path/to/current/working/directory'     # Required for module imports
python wma.py
```
*WeightedMA* class is meant to be imported. Therefore, it does not take any command line arguments. Initialize it with proper parameters and call the *run* method to run all the steps. If executes successfully, then the averages will be stored inside the *averageArray* class member.  

```python
# EXAMPLE (Used for Visualizations below)
wma = WeightedMA(period='1mo', ticker='AMZN', frequency=10, graph=True)
wma.run()
plt.show()
```

A *RunTime Exception* is raise in case of invalid parameters, failed download, or any unexpected error.

## Visualizations
* Frequency: 1.  
    <p align='center'>
      <img alt='MA 1' src='https://github.com/NP1Traders/Indicators/blob/main/WeightedMovingAverageWMA/Visualization/Images/Frequency%201.png' />
    </p>
  
* Frequency: 10.  
    <p align='center'>
      <img alt='MA 10' src='https://github.com/NP1Traders/Indicators/blob/main/WeightedMovingAverageWMA/Visualization/Images/Frequency%2010.png' />
    </p> 

* Frequency: 20.  
    <p align='center'>
      <img alt='MA 20' src='https://github.com/NP1Traders/Indicators/blob/main/WeightedMovingAverageWMA/Visualization/Images/Frequency%2020.png' />
    </p> 

* Frequency: 50.  
    <p align='center'>
      <img alt='MA 50' src='https://github.com/NP1Traders/Indicators/blob/main/WeightedMovingAverageWMA/Visualization/Images/Frequency%2050.png' />
    </p> 

* Frequency: 100.  
    <p align='center'>
      <img alt='MA 100' src='https://github.com/NP1Traders/Indicators/blob/main/WeightedMovingAverageWMA/Visualization/Images/Frequency%20100.png' />
    </p>


## Requirements

>Python 3.7

#### Libraries  
* *yfinance*
* *datetime*
* *dataclasses*
* *matplotlib*
* *numpy*

#### Packages
* *Data_Collector*
