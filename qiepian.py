import cv2
import scipy, cv2, os, sys, argparse
from tqdm import tqdm
from os import path

import os
parser = argparse.ArgumentParser(description='Inference code to lip-sync videos in the wild using Wav2Lip models')

parser.add_argument('--mp4', type=str,
					help='mp4', required=True)
parser.add_argument('--outfile', type=str,
					help='outfile', required=True)
args = parser.parse_args()
inputVideoPath = args.mp4
unProcessedFramesFolderPath = args.outfile

if not os.path.exists(unProcessedFramesFolderPath):
  os.makedirs(unProcessedFramesFolderPath)

vidcap = cv2.VideoCapture(inputVideoPath)
numberOfFrames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = vidcap.get(cv2.CAP_PROP_FPS)
print("FPS: ", fps, "Frames: ", numberOfFrames)

for frameNumber in tqdm(range(numberOfFrames)):
    _,image = vidcap.read()
    cv2.imwrite(path.join(unProcessedFramesFolderPath, str(frameNumber).zfill(4)+'.jpg'), image)