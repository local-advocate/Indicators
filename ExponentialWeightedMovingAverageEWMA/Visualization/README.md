# Visualization, Exponential Weighted Moving Average (EWMA)

## Description
Calculates the Exponential Weighted Moving Average of a stream w/ given alpha.

Use for short term averages only. EWMA highly sensitive to *alpha* values (between 0 and 1).

#### Arguments
1. Period       &emsp;&ensp;:&emsp;         '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'. 
2. Interval     &emsp;:&emsp;               '1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo'. Default: 30m.
3. Start        &emsp;&emsp;&nbsp;:&emsp;   yyyy-mm-dd.
4. End          &emsp;&emsp;&ensp;:&emsp;   yyyy-mm-dd.
5. Ticker       &emsp;&ensp;:&emsp;         TCKR of a company.
6. Alpha        &emsp;&emsp;:&emsp;         Sensitivity of the moving average. Low alpha ∝ More weight to recent prices. Default: 0.8.
7. Column       &emsp;:&emsp;               'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'. Default: Open.
8. Graph        &ensp;&emsp;:&emsp;         Graph the results or not. Default: False. Call show() explicitly to show plot if graphing.

## How to run
```bash
export PYTHONPATH='path/to/current/working/directory'     # Required for module imports
python ewma.py
```
*ExponentialWMA* class is meant to be imported. Therefore, it does not take any command line arguments. Initialize it with proper parameters and call the *run* method to run all the steps. If executes successfully, then the averages will be stored inside the *averageArray* class member.  

```python
   # EXAMPLE
   ewma = ExponentialWMA(period='1d', ticker='AMZN', alpha=0.8, graph=True)
   ewma.run()
   plt.show()
```

A *RunTime Exception* is raise in case of invalid parameters, failed download, or any unexpected error.

## Visualizations
* Alpha: 0.0.  
    <p align='center'>
      <img alt='Alpha 0.0' src='https://github.com/NP1Traders/Indicators/blob/main/ExponentialWeightedMovingAverageEWMA/Visualization/Images/0.0.png' />
    </p>
  
* Alpha: 0.2.  
    <p align='center'>
      <img alt='Alpha 0.2' src='https://github.com/NP1Traders/Indicators/blob/main/ExponentialWeightedMovingAverageEWMA/Visualization/Images/0.2.png' />
    </p> 

* Alpha: 0.5.  
    <p align='center'>
      <img alt='Alpha 0.5' src='https://github.com/NP1Traders/Indicators/blob/main/ExponentialWeightedMovingAverageEWMA/Visualization/Images/0.5.png' />
    </p> 

* Alpha: 0.8.  
    <p align='center'>
      <img alt='Alpha 0.8' src='https://github.com/NP1Traders/Indicators/blob/main/ExponentialWeightedMovingAverageEWMA/Visualization/Images/0.8.png' />
    </p> 

* Alpha: 1.0.  
    <p align='center'>
      <img alt='Alpha 1.0' src='https://github.com/NP1Traders/Indicators/blob/main/ExponentialWeightedMovingAverageEWMA/Visualization/Images/1.0.png' />
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
