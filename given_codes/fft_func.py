import numpy as np
import matplotlib.pyplot as plt

def fft_result(contents):#50
    specs_all = np.array([np.abs(np.fft.rfft(rows)) for rows in contents])
    specs_all = specs_all[:,1:]
    return specs_all

def fft_output(specs_all,target):
    x = np.arange(1,21,1)
    for i in range(len(specs_all)):
        specs = specs_all[i,:20]
        plt.plot(x,specs)
        plt.xticks(x)
        plt.ylim([0,8000])
        plt.xlabel("Frequency[Hz]",fontname="MS Gothic")
        plt.ylabel("Amplitude[-]")
        # plt.title(f'{target[i][55:58],target[i][59:62]}freq')#ファイル名を抜き出してから持ってくる
        # plt.savefig(f'{target[i][55:58],target[i][59:62]}freq.png')
        plt.show()

def fft_ana_output(specs_all,target):
    x = np.arange(1,121)
    for i in range(len(specs_all)):
        specs = specs_all[i,:120]
        plt.plot(x,specs)
        plt.xticks(x)
        plt.ylim([0,8000])
        plt.xlabel("Frequency[Hz]",fontname="MS Gothic")
        plt.ylabel("Amplitude[-]")
        # plt.title(f'{target[i][56:59],target[i][60:63]}freq')
        # plt.savefig(f'{target[i][56:59],target[i][60:63]}freq.png')
        plt.show()