# latency-calib
使用evo工具估计传感器之间的误差，并绘制不同时间差下的误差平均值图像

## Dependency
- subprocess
- pandas
- numpy
- matplotlib

## Method
用于估计动捕系统误差，同时采集动捕和IMU的角度数据。

该脚本将动捕数据上下移动若干帧，生成对应的轨迹文件，使用evo工具逐个对比姿态信息，并绘制平均误差曲线。

## Usage
- `ref_data_dir`：参考轨迹的文件路径

- `cmp_data_dir`：对比轨迹的文件路径

- `ref_data_shift_min`：对比轨迹的数据移动最小值

- `ref_data_shift_max`：对比轨迹的数据移动最大值

- `frame_num`：用于对比的帧的数量

## Note
脚本在运行时会将每一次执行evo的输出打印到终端上，在Ubuntu中可以使用
``` bash
$ python3 main.py > output.txt
```
命令将输出转存到"output.txt"文件中，方便储存和查看。
