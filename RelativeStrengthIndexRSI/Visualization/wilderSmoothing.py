class WilderSmoothing:
  ''' Wilder's Smoothing, Optimized version '''
  def __init__(self, timeperiod):      
      # self.alpha = 1/timeperiod
      self.avg = 0
      self.timeperiod = timeperiod
      self.oneless = timeperiod-1

  def add(self, x):
      # self.avg = (self.alpha * x) + ((1-self.alpha)*self.avg)
      self.avg = (x + (self.oneless*self.avg))/self.timeperiod
