import pandas as pd
import numpy as np

from scipy.stats import expon
from scipy.stats import norm

chat_id = 5463739632 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    #z1=expon.ppf(1-alpha/2)
    #z2=expon.ppf(alpha/2)
    #loc = x.mean()
    #scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    #return loc - scale * norm.ppf(1 - alpha / 2), \
    #       loc - scale * norm.ppf(alpha / 2)
    #return x.mean()/np.sqrt(41*z1), \
    #       x.mean()/np.sqrt(41*z2)
    #left_b = x.mean() - np.sqrt(np.var(x)) * norm.ppf(1 - alpha / 2) / np.sqrt(len(x))
    #right_b = x.mean() - np.sqrt(np.var(x)) * norm.ppf(alpha / 2) / np.sqrt(len(x))
    #return (31*left_b)/np.sqrt(41)/39, (31*right_b)/np.sqrt(41)/39
    z1 = expon.ppf(1-alpha/2,scale=2)
    z2 = expon.ppf(alpha/2,scale=2)
    return np.sqrt(np.mean(x*x))/np.sqrt(82) - z2*4/np.sqrt(len(x)),  np.sqrt(np.mean(x*x))/np.sqrt(82) + z2*4/np.sqrt(len(x)) 
