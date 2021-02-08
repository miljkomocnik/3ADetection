import pandas as pd


def calculate_ewma(data, threshold, window_size):
    x = pd.Series.ewm(data['Data'], span=window_size).mean()

    data['Exponentially Weighted Moving Average'] = 0
    for i in range(0, len(data['Data'])):
        if data['Data'].at[i] > x[i] + threshold or data['Data'].at[i] < x[i] - threshold:
            data['Exponentially Weighted Moving Average'].at[i] = 1
    return "Exponentially Weighted Moving Average"
