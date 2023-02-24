import numpy as np

class DiscountedAveragerator:
  ''' A smoother and effiecient implementation of sliding window average. '''
  def __init__(self, alpha):      # lower the alpha, the less weight of the previous values
      self.alpha = alpha
      self.w = 0.
      self.sum_x = 0.
      self.sum_x_sq = 0.

  def add(self, x):
      self.w = self.alpha * self.w + 1.
      self.sum_x = self.alpha * self.sum_x + x
      self.sum_x_sq = self.alpha * self.sum_x_sq + x * x

  @property
  def avg(self):
      return self.sum_x / self.w

  @property
  def std(self):
      mu = self.avg
      # The np.maximum is purely for safety.
      return np.sqrt(np.maximum(0., self.sum_x_sq / self.w - mu * mu))