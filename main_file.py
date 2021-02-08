import pandas as pd
from ewma import calculate_ewma
from cusum import calculate_cusum
from draw_plots import draw_alarm_plots
from knn import calculate_knn

FILE_NAME = 'FINAL_UDP.csv'

THRESHOLD_CUMSUM = 136  # Used by CUMSUM 100 for http 136 for udp
THRESHOLD_EWMA = 70  # Used by EWMA 100 for http 70 for udp
DRIFT = 30  # Used by CUMSUM 20 for http 30 for udp
WINDOW_SIZE_EWMA = 25  # Used for EWMA 20 for http 25 for udp

# load data from file
data = pd.read_csv('data_files/' + FILE_NAME)

draw_alarm_plots(data, 'Attack', FILE_NAME)

# calculate alarms
names = [calculate_knn(data),
         calculate_ewma(data, threshold=THRESHOLD_EWMA, window_size=WINDOW_SIZE_EWMA),
         calculate_cusum(data, threshold=THRESHOLD_CUMSUM, drift=DRIFT)]

# make graph
for name in names:
    draw_alarm_plots(data, name, FILE_NAME)

data['3A Alarm'] = 0
for i in range(0, len(data['3A Alarm'])):
    if((data[names[0]].at[i] == 1 and data[names[1]].at[i] == 1) or
            (data[names[0]].at[i] == 1 and data[names[2]].at[i] == 1) or
            (data[names[1]].at[i] == 1 and data[names[2]].at[i] == 1)):
        data['3A Alarm'].at[i] = 1

draw_alarm_plots(data, '3A Alarm', FILE_NAME)


data.to_csv('results/'+FILE_NAME)
