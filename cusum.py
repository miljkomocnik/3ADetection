import matplotlib.pyplot as plt
from detecta import detect_cusum


def calculate_cusum(data, threshold, drift):
    ta, tai, taf, amp = detect_cusum(data['Data'], threshold, drift, ending=True, show=False)

    data["Cumulative Sum Algorithm"] = 0
    start = False
    for i in range(5, len(data["Cumulative Sum Algorithm"])):
        if i in tai:
            start = True
        elif i in taf:
            start = False
        if start:
            data["Cumulative Sum Algorithm"].at[i] = 1

    plt.clf()
    return "Cumulative Sum Algorithm"
