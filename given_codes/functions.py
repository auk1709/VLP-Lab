import numpy as np

def distance_2D(x_LED, y_LED,x_recv,y_recv):
    distance=np.sqrt((x_LED-x_recv)**2+(y_LED-y_recv)**2)
    return distance

def dis_output(LED_T,recv_T):
    LED_to_recv_dis = []
    for LED in LED_T:
        dis = [distance_2D(LED[0],LED[1],recv[0],recv[1]) for recv in recv_T]
        LED_to_recv_dis.append(dis)
    LED_to_recv_dis = np.array(LED_to_recv_dis)
    return LED_to_recv_dis