import numpy as np
import matplotlib.pyplot as plt

#一つの周波数のみを光らせた時
def format_mono_LED(specs_all,cutnum,same,freq_LED_deg):
    freq_means = []
    for i in range(same):
        same_spec = specs_all[cutnum*(i):cutnum*(i+1)]#6
        freq_means.append(same_spec[:,freq_LED_deg[i]])

    freq_means = np.array(freq_means).reshape(same,cutnum)
    print(freq_means)
    print(freq_means.shape)
    return freq_means

#全てのLEDを光らせた時
def format_multi_LED(specs_all,LED_freq_deg):
    freq_means4led = []
    for Num in LED_freq_deg:
        freq_means4led.append(specs_all[:,Num])
    freq_means4led = np.array(freq_means4led)
    print(freq_means4led.shape)
    print(freq_means4led)
    return freq_means4led


#プロットの出力
def output_RSS_to_pos(LED_to_recv_dis,freq_means):
    for i in range(len(LED_to_recv_dis)):
        plt.plot(LED_to_recv_dis[i], freq_means[i], marker='.', linestyle='None')
        plt.show()