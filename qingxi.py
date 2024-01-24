import os
import subprocess
from concurrent.futures import ThreadPoolExecutor
import scipy, cv2,  sys, argparse
from tqdm import tqdm
from os import path

import os
parser = argparse.ArgumentParser(description='Inference code to lip-sync videos in the wild using Wav2Lip models')

parser.add_argument('--input', type=str,
					help='mp4', required=True)
parser.add_argument('--item', type=str,
					help='item', required=True)

args = parser.parse_args()
folder_path = args.input
item_path = args.item

folders = [f for f in os.listdir(folder_path) if f.startswith('new_folder_')]
print(folders)
def run_inference(folder):
    input_path = os.path.join(folder_path, folder, 'input')
    output_path = os.path.join(folder_path, folder, 'output')
    cmd = f"python {item_path}/inference.py -i {input_path} -o {output_path} -v RestoreFormer++ -s 2 --save"
    print(cmd)
    subprocess.run(cmd, shell=True)

with ThreadPoolExecutor() as executor:
    executor.map(run_inference, folders)
