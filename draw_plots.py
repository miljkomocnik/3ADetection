import matplotlib.pyplot as plt
import time


def draw_alarm_plots(data, name, file_name):

    data[['Data']].plot(figsize=(9, 3))

    x_position = []
    for i in range(0, len(data[name])):
        if data[name].at[i] != 0:
            x_position.append(i)
    for xc in x_position:
        plt.axvline(x=xc, color='red', linestyle='--')

    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())

    plt.xlabel('Time\n')
    plt.ylabel('Network traffic')
    plt.title(name)
    plt.legend(["Network traffic", "Alarm"], loc=0)
    plt.tight_layout()

    str(time.time())
    plt.savefig('results/' + file_name + name + '.png')
