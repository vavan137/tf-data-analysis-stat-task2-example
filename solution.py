import pandas as pd
import numpy as np

from scipy.stats import expon


chat_id = 5463739632 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    z1=expon.ppf(1-alpha/2)
    z2=expon.ppf(alpha/2)
    #loc = x.mean()
    #scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    #return loc - scale * norm.ppf(1 - alpha / 2), \
    #       loc - scale * norm.ppf(alpha / 2)
    return x.mean()/np.sqrt(41*z1), \
           x.mean()/np.sqrt(41*z2)
