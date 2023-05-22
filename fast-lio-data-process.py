import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as R 

global figure_index
figure_index = 1
# a function that reads an .csv file and output keys in the first line.
def read_csv_keys(fileName):
    # read the file
    data = pd.read_csv(fileName, sep=",", header=None)
    # output the keys without ...
    print(data.loc[0,:].values)

# a function that plots the data in the .csv file, input is the file name and data key, output is the plot
def plot_csv_data(fileName, key):
    # read the file
    global figure_index
    data = pd.read_csv(fileName, sep=",", header=None)
    # plot the data
    index_ = index_csv_key(fileName, key)
    # convert from string to double and plot
    plt.figure(figure_index)
    plt.plot(data.loc[1:,index_].astype(float))
    plt.xlabel("frame")
    plt.ylabel(key+"/m")
    plt.savefig(key+".png",dpi=300)
    figure_index+=1

def quaternion2euler(quaternion):
    r = R.from_quat(quaternion)
    euler = r.as_euler('zyx', degrees=True)
    return euler

# 
def plot_csv_angle(fileName):
    # read the file
    global figure_index
    data = pd.read_csv(fileName, sep=",", header=None)
    # save quaternion data as array
    quat = data.loc[1:,8:11].astype(float)
    # convert quaternion to euler angle
    euler = []
    # print(quaternion2euler(quat.loc[0,:]))
    # loop start from 1 to range(quat.shape[0])
    for i in range(quat.shape[0]):
        euler.append(quaternion2euler(quat.loc[i+1,:]))
    # plot euler angle
    euler = pd.DataFrame(euler)
    plt.figure(figure_index)
    plt.plot(euler.loc[:,0])
    plt.plot(euler.loc[:,1])
    plt.plot(euler.loc[:,2])
    plt.xlabel("frame")
    plt.ylabel("angle/degree")
    plt.legend(["yaw","pitch","roll"])
    plt.savefig("angle.png",dpi=300)
    figure_index+=1

# a function that index the number of the key in a .csv file, input is filename and key, output is the index number
def index_csv_key(fileName, key):
    # read the file
    data = pd.read_csv(fileName, sep=",", header=None)
    # find the index of the key
    index = data.loc[0,:].values.tolist().index(key)
    return index

targetfile = "fast_lio_dd640_odometry.csv"

plot_csv_angle(targetfile)

plt.show()