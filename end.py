import os
import scipy, cv2, os, sys, argparse
import subprocess

parser = argparse.ArgumentParser(description='1')
parser.add_argument('--mp3', type=str,
					help='mp3', required=True)
parser.add_argument('--outfile', type=str,
					help='outfile', required=True)
parser.add_argument('--outpath', type=str,
					help='outpath', required=True)

parser.add_argument('--framerate', type=int,
					help='framerate', default=25)

args = parser.parse_args()
inputAudioPath=args.mp3
framerate=args.framerate
outFile=args.outfile
outputPath = args.outpath
restoredFramesPath = outputPath + '/restored_imgs/'
processedVideoOutputPath = outputPath

dir_list = os.listdir(restoredFramesPath)
dir_list.sort()

import cv2
import numpy as np

batch = 0
batchSize = 300
from tqdm import tqdm

for i in tqdm(range(0, len(dir_list), batchSize)):
    img_array = []
    start, end = i, i + batchSize
    print("processing ", start, end)
    for filename in tqdm(dir_list[start:end]):
        filename = restoredFramesPath + filename;
        img = cv2.imread(filename)
        if img is None:
            continue
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)

    out = cv2.VideoWriter(processedVideoOutputPath + '/batch_' + str(batch).zfill(4) + '.avi',
                          cv2.VideoWriter_fourcc(*'DIVX'), framerate, size)
    batch = batch + 1

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
concatTextFilePath = outputPath + "/concat.txt"
concatTextFile = open(concatTextFilePath, "w")
for ips in range(batch):
    concatTextFile.write("file batch_" + str(ips).zfill(4) + ".avi\n")
concatTextFile.close()

concatedVideoOutputPath = outputPath + "/concated_output.avi"
command1 = f"ffmpeg -y -f concat -i {concatTextFilePath} -c copy {concatedVideoOutputPath}"
subprocess.run(command1,
               stdout=subprocess.PIPE,
               stderr=subprocess.PIPE, close_fds=True, shell=True)

# ffmpeg -y -f concat -i {concatTextFilePath} -c copy {concatedVideoOutputPath}

finalProcessedOuputVideo = processedVideoOutputPath + '/'+outFile
command2 = f"ffmpeg -y -i {concatedVideoOutputPath} -i {inputAudioPath} -map 0 -map 1:a -c:v h264 -b:v 5000k -shortest {finalProcessedOuputVideo}"
subprocess.run(command2,
               stdout=subprocess.PIPE,
               stderr=subprocess.PIPE, close_fds=True, shell=True)
# ffmpeg -y -i {concatedVideoOutputPath} -i {inputAudioPath} -map 0 -map 1:a -c:v copy -shortest {finalProcessedOuputVideo}


