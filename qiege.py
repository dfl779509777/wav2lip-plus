import os
import shutil
import scipy, cv2, os, sys, argparse
from tqdm import tqdm
from os import path

import os
parser = argparse.ArgumentParser(description='Inference code to lip-sync videos in the wild using Wav2Lip models')

parser.add_argument('--input', type=str,
					help='input', required=True)
parser.add_argument('--outfile', type=str,
					help='outfile', required=True)
parser.add_argument('--num', type=int,
					help='outfile', required=True)

args = parser.parse_args()
folder_path = args.input
out_paths = args.outfile
num=args.num

image_list = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.png')]
sub_lists = [image_list[i::num] for i in range(num)]

for i, sub_list in enumerate(sub_lists):
    new_folder_path = os.path.join(out_paths, f'handle/new_folder_{i+1}/input')
    os.makedirs(new_folder_path)
    for image_file in sub_list:
        src_path = os.path.join(folder_path, image_file)
        dst_path = os.path.join(new_folder_path, image_file)
        shutil.copy(src_path, dst_path)
