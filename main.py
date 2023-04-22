import subprocess
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# a function that opens the terminal and runs the input command, then save the output and print 
def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    # find sting "std:" in the output and save the data after it as double
    output = output.decode("utf-8")
    print(output)
    output = output[output.find("mean")+5:output.find("median")-1]
    output_std = float(output)
    print("-----------------------------------")
    return output_std

# a function that reads an .txt file and shift the data by a given amount
def dataModification(fileName, shiftStart, shiftEnd, selectRow):
    # read the file
    data = pd.read_csv(fileName, sep=" ", header=None)
    # create new data
    for i in range(shiftStart, shiftEnd):
        new_data = pd.DataFrame(columns=[0,1,2,3,4,5,6,7])
        # shift the data
        new_data = data.shift(i)
        new_data.loc[:,0] = data.loc[:,0]
        # stlect the middle part of the new_data with length of selectRow
        cut_data = new_data.loc[(new_data.shape[0]//2-selectRow//2):(new_data.shape[0]//2+selectRow//2),:]
        # save the file
        fileName_save = "./processedData/" + fileName[0:-4] + "_" + str(i) + ".txt"
        cut_data.to_csv(fileName_save, sep=" ", header=None, index=None)
    print("Data modified and saved")

# the directory of the reference data and the data to be compared
ref_data_dir = "imuDataRefine.txt"
cmp_data_dir = "mocapDataRefine.txt"

# the range of the shift of the reference data
ref_data_shift_min = -50
ref_data_shift_max = 60
frame_num = 2000

# script execution -------------------------------------------------------------------
dataModification(cmp_data_dir, ref_data_shift_min, ref_data_shift_max+1, frame_num)
dataModification(ref_data_dir, 0, 1, frame_num)

std = []

for i in range(ref_data_shift_min, ref_data_shift_max+1):
    cmp_data_dir = "./processedData/mocapDataRefine_" + str(i) + ".txt"
    ref_data_dir = "./processedData/imuDataRefine_0.txt"
    std.append(run_command("evo_ape tum " + ref_data_dir + " " + cmp_data_dir + " -r angle_deg"))

# plot the average mean
plt.plot(np.arange(ref_data_shift_min, ref_data_shift_max+1), std)
plt.xlabel("shift/frame")
plt.ylabel("difference/degree")
# set x axis to be integer
plt.xticks(np.arange(ref_data_shift_min, ref_data_shift_max+1, 5))
# save plot to file, resolution 300 dpi
plt.savefig("ape-angle_deg_-50-60.png", dpi=300)
plt.show()