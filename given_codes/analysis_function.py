import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

def reflect_light_positioning(all_beta,ana_freq_means):
    recv_to_trans =[]
    for i in range(4):
        dis_rec_to_tra = 2*(np.arccosh(0.5*all_beta[i,0]/np.abs(ana_freq_means[i]))/(np.pi*all_beta[i,1]))#LED1と5つの受信機の位置の関係dk
        recv_to_trans.append(dis_rec_to_tra)
    recv_to_trans = np.array(recv_to_trans)
    recv_to_trans = np.nan_to_num(recv_to_trans)
    return recv_to_trans


def direct_light_positioning():
    return 0

def result_output(position_all,recv_ana,LED_T):
    lines = [ [sp,ep] for sp,ep in zip(position_all, recv_ana)]
    colors = ["g"]
    lc = LineCollection(lines, colors=colors)
    fig, ax = plt.subplots()
    ax.plot(position_all[:,0],position_all[:,1],"r.",label="real position",markersize=10)
    ax.plot(recv_ana[:,0],recv_ana[:,1],"b.",label="estimted position",markersize=10)
    ax.plot(LED_T[:,0],LED_T[:,1],"y+",label="LED", markersize=15,)
    plt.xlim(0.75,2.75)
    plt.ylim(0.75,2.25)
    plt.xlabel("X-axis[m]",fontname="MS Gothic")
    plt.ylabel("Y-axis[m]",fontname="MS Gothic")
    ax.legend(loc='best', borderaxespad=0)
    ax.grid(linestyle='dotted')
    ax.add_collection(lc)
    plt.title('Positioning')
    plt.savefig('Positioning')
    plt.show()