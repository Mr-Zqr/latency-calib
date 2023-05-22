import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as R 

global figure_index
figure_index = 1

def quaternion2euler(quaternion):
    r = R.from_quat(quaternion)
    euler = r.as_euler('zyx', degrees=True)
    return euler

def attatch_eul_to_csv(fileName, qx, qy, qz, qw):
    data = pd.read_csv(fileName, sep=",", header=None)
    qx_n = index_csv_key(fileName, qx)
    qy_n = index_csv_key(fileName, qy)
    qz_n = index_csv_key(fileName, qz)
    qw_n = index_csv_key(fileName, qw)
    print(qx_n, qy_n, qz_n, qw_n)
    
    name = [qx, qy, qz, qw]
    quat = data.loc[1:,8:11].astype(float)

    euler = []
    for i in range(quat.shape[0]):
        euler.append(quaternion2euler(quat.loc[i+1,:]))
    # append euler into data
    euler = pd.DataFrame(euler)
    data = pd.concat([data, euler], axis=1)
    data.iloc[0, -3:] = ['euler.yaw', 'euler.pitch', 'euler.roll']
    # save data to csv
    data.to_csv("test.csv", index=True, header=None)

# a function that index the number of the key in a .csv file, input is filename and key, output is the index number
def index_csv_key(fileName, key):
    # read the file
    data = pd.read_csv(fileName, sep=",", header=None)
    # find the index of the key
    index = data.loc[0,:].values.tolist().index(key)
    return index

targetfile = "fast_lio_dd640_odometry_1.csv"

qx = "field.pose.pose.orientation.x"
qy = "field.pose.pose.orientation.y"
qz = "field.pose.pose.orientation.z"
qw = "field.pose.pose.orientation.w"

attatch_eul_to_csv(targetfile, qx, qy, qz, qw)