# Wav2lip Plus

## ER-NeRF : [Paper](https://arxiv.org/abs/2307.09323) | [github](https://github.com/Fictionarry/ER-NeRF.git)

## 语言: [[English](README.md)] | [简体中文]

## 概述

- 这只是一个缝合怪项目，一个基于wav2lip的数字人视频生成的全流程方案,类似Wav2Lip-GFPGAN。

## 安装

- Ubuntu18.04; CUDA11.1;Python 3.8.10

    ```

- python环境:

    # install pytorch
    pip install torch==1.8.1+cu111 torchvision==0.9.1+cu111 --extra-index-url https://download.pytorch.org/whl/cu111

    # install others
    pip install -r requirements.txt


## 使用说明

- 输入的视频数据并保证每一帧都有人脸,25帧率, 视频中只有一人, 且需要保证时间连续性(一镜到底).

    ```shell
    ./hecheng.sh mp4地址 MP3地址
    ```
结果在根目录下data/output/test.mp4
## 感谢列表

- 人脸合成源于: [Wav2lip](https://github.com/Rudrabha/Wav2Lip.git)

- 人脸清晰化: [RestoreFormerPlusPlus](https://github.com/wzhouxiff/RestoreFormerPlusPlus.git)


