#!/bin/bash

#$1为脸部视频地址
#$2为输入的音频地址 
#$3为步骤

mp4=$1
mp3=$2


#项目地址
dir="/root/autodl-tmp/wav2lip-plus"
plus_dir="${dir}/RestoreFormerPlusPlus"
wav2lip_dir="${dir}/Wav2Lip"
data_dir="${dir}/data"

#最终返回的目录
result_dir="${dir}/result"


if [ -n "$3" ]; then
    num=$3
else
    num=-1
fi



#Wav2lip合成
if [ $num == -1 ] || [ $num == 1 ]; then
    echo "step1*********Wav2lip合成**************"
    echo "cd ${wav2lip_dir} && python inference.py --checkpoint_path checkpoints/wav2lip.pth --audio ${mp3} --face ${mp4} --outfile ${data_dir}/input.mp4"
    cd ${wav2lip_dir} && python inference.py --checkpoint_path checkpoints/wav2lip.pth --audio ${mp3} --face ${mp4} --outfile ${data_dir}/input.mp4

fi


if  [ $num == -1 ] || [ $num == 2 ]; then
	echo "step2*********视频切片**************"
    echo  "cd ${dir}  && python qiepian.py --mp4 ${data_dir}/input.mp4 --outfile ${data_dir}/input"
    cd ${dir} && python qiepian.py --mp4 ${data_dir}/input.mp4 --outfile ${data_dir}/input
fi

if  [ $num == -1 ] || [ $num == 3 ]; then
	echo "step3*********图片均分**************"
    echo  "cd ${dir}  && python qiege.py --input ${data_dir}/input --outfile ${data_dir} --num 6"
    cd ${dir}  && python qiege.py --input ${data_dir}/input --outfile ${data_dir} --num 6
fi


if  [ $num == -1 ] || [ $num == 4 ]; then
	echo "step4*********清晰化处理**************"
    echo  "cd ${dir}  && python qingxi.py --input ${data_dir}/handle --item ${plus_dir}"
    cd ${dir}  && python qingxi.py --input ${data_dir}/handle --item ${plus_dir}
fi

if  [ $num == -1 ] || [ $num == 5 ]; then
	echo "step5*********合并图片**************"
    echo  "cd ${dir}  && python hebing.py --input ${data_dir}/handle --output ${data_dir}"
    cd ${dir}  && python hebing.py --input ${data_dir}/handle --output ${data_dir}
fi

if  [ $num == -1 ] || [ $num == 6 ]; then
	echo "step6*********视频合成**************"
    echo  "cd ${dir} && python end.py --mp3 ${mp3} --outfile test.mp4 --outpath ${data_dir}/output --framerate 25"
    cd ${dir} && python end.py --mp3 ${mp3} --outfile test.mp4 --outpath ${data_dir}/output --framerate 25
fi






