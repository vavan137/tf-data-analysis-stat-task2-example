import pandas as pd
import numpy as np

from scipy.stats import expon
from scipy.stats import chi2
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
    size = len(x)	
	chi2_rv = chi2(df = 2 * size)
	left_b = chi2_rv.ppf(1 - alpha / 2)
	right_b = chi2_rv.ppf(alpha / 2)	
	return np.sqrt(size * np.mean(x*x) / (left_b * 41)), np.sqrt(size * np.mean(x*x) / (right_b * 41))
