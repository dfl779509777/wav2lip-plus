import scipy, cv2, os, sys, argparse
import subprocess
from concurrent.futures import ThreadPoolExecutor

parser = argparse.ArgumentParser(description='1')
parser.add_argument('--input', type=str,
					help='in_path', required=True)
parser.add_argument('--output', type=str,
					help='output', required=True)

args = parser.parse_args()
folder_path=args.input
out_put=args.output

folders = [f for f in os.listdir(folder_path) if f.startswith('new_folder_')]
print(folders)
def run_inference(folder):
    input_path = os.path.join(folder_path, folder, 'output')
    output_path = os.path.join(out_put)
    cmd = f"cp -r {input_path} {output_path}"
    print(cmd)
    subprocess.run(cmd, shell=True)

with ThreadPoolExecutor() as executor:
    executor.map(run_inference, folders)