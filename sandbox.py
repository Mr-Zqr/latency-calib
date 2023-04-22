import subprocess
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    # find sting "std:" in the output and save the data after it as double
    output = output.decode("utf-8")
    print(output)
    output = output[output.find("mean")+5:output.find("median")-1]
    output_mean = float(output)
    print(output_mean)
    print("-----------------------------------")
    return output_mean

run_command("evo_rpe tum ./processedData/mocapDataRefine_0.txt ./processedData/imuDataRefine_0.txt -va -r rot_part")