import glob
import numpy as np
import cv2
import matplotlib.pyplot as plt

# 'S:\\VLP\\resouces\\',jpg

def make_pathlist(path_name,extensions):
    root_path = f'{path_name}\\' 
    target = glob.glob(f'{root_path}*.{extensions}')
    return target

def data_contents_picture(target):
    imgs = np.array([cv2.imread(path) for path in target])#,cv2.IMREAD_GRAYSCALE
    # print(f'imgs shape: {imgs.shape,len(target[0])}')
    imgs_all = imgs
    imgs_each = imgs
    imgs_all = imgs_all[:,:,128:512,1]
    imgs_each = imgs_each[:,:,128:512,1]
    print(f'imgs_all: {imgs_all.shape}, imgs_each: {imgs_each.shape}')
    avg_rows_all = np.mean(imgs_all,axis=2)
    avg_rows_each = np.mean(imgs_each,axis=2)
    print(f'avg_rows_all: {avg_rows_all.shape}, avg_rows_each: {avg_rows_each.shape}')
    return avg_rows_all,avg_rows_each

def data_contents_smart_picture(target):
    imgs = np.array([cv2.imread(path) for path in target])#,cv2.IMREAD_GRAYSCALE
    # print(f'imgs shape: {imgs.shape,len(target[0])}')
    imgs_all = imgs[:,:,:,1]
    imgs_each = imgs[:,300:,:,1]
    print(f'imgs_all: {imgs_all.shape}, imgs_each: {imgs_each.shape}')
    avg_rows_all = np.mean(imgs_all,axis=1)
    avg_rows_each = np.mean(imgs_each,axis=1)
    print(f'avg_rows_all: {avg_rows_all.shape}, avg_rows_each: {avg_rows_each.shape}')
    return avg_rows_all,avg_rows_each

def data_contents_video(target):
    width = 32
    pix_ave = []
    for path in target:
        imgs = cv2.VideoCapture(path)    
        for i in range(50):
            ret, frame = imgs.read()
            if ret == False:
                break
            green_frame = frame[:,:,1]
            sample_frame = green_frame[464:464+width,624:624+width]
            avg_rows = np.mean(sample_frame)
            pix_ave.append(avg_rows)
            imgs.set(cv2.CAP_PROP_POS_FRAMES, i+1)
    return pix_ave

def data_contents_ALS(target):
    return 

def contents_output(contents,target):
    for i in range(len(contents)):
        plt.plot(contents[i])
        # plt.title(f'{target[i][55:58],target[i][59:62]}wave')#ファイル名を抜き出してから持ってくる
        # plt.savefig(f'{target[i][55:58],target[i][59:62]}wave.png')
        plt.show()

def contents_ana_output(contents,target):
    for i in range(len(contents)):
        plt.plot(contents[i])
        # plt.title(f'{target[i][56:59],target[i][60:63]}wave')
        # plt.savefig(f'{target[i][56:59],target[i][60:63]}wave.png')
        plt.show()

