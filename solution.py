import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 968976840 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    distances = np.array([45.6, 47.9, 44.2, 48.1, 43.3, 49.2, 42.1, 46.3, 41.6, 49.7])
    mean = np.mean(distances)
    std = np.std(distances, ddof=1)
    se = std / np.sqrt(len(distances))
    confidence_level = 0.95
    t = np.abs(np.round(stats.t.ppf((1 - confidence_level) / 2, len(distances) - 1), decimals=2))
    lower_bound = mean - t * se
    upper_bound = mean + t * se
    x = distances
    loc = mean
    alpha = confidence_level
    alpha = 1 - p
    loc = x.mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return loc - scale * norm.ppf(1 - alpha / 2), \
           loc - scale * norm.ppf(alpha / 2)
