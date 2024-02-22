# 传感器驱动

基于 Dora0.3.2环境开发的100D4陀螺仪和GNSS定位。

## 背景

将IMU驱动与GNSS驱动放入一个数据流当中，目前IMU可以直接发到ros2进行显示，但GNSS可能是室内定位的原因，定位数据都是无效定位。

## 安装

通过此文件的 requirements.txt 文件实现环境依赖项的安装：

```
pip install -r requirements.txt
```

## 用法

```
PATH=$PATH:$(pwd)
cd /home/crp/dora_project/dora-rs/dora-hardware/vendors/gnss_imu/
dora up
sudo chmod 777 /dev/ttyUSB0 
sudo chmod 777 /dev/ttyUSB1
dora start dataflowImuGnss.yml --name test
```
目前IMU对应/dev/ttyUSB0，GNSS对应/dev/ttyUSB1；

先插的传感器是/dev/ttyUSB0 ，后插的传感器是/dev/ttyUSB1。

## 日志

```
dora logs test imu #查看imu的数据
dora logs test gnss_sub #查看gnss的数据
```

