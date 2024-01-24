
### Journal ###
root='results/'
out_root='results/metrics'
CelebAHQ_GT=''
out_root='./results/metrics'

# test_name='RestoreFormer'
test_name='RestoreFormerPlusPlus'
tag='test'

test_image=$test_name'_'$tag'/restored_faces'
out_name=$test_name
need_post=1

# FID
python -u scripts/metrics/cal_fid.py \
$root'/'$test_image \
--fid_stats 'experiments/pretrained_models/inception_FFHQ_512.pth.pth' \
--save_name $out_root'/'$out_name'_fid.txt' \

if [ -d $CelebAHQ_GT ]
then
    # PSRN SSIM LPIPS
    python -u scripts/metrics/cal_psnr_ssim.py \
    $root'/'$test_image \
    --gt_folder $CelebAHQ_GT \
    --save_name $out_root'/'$out_name'_psnr_ssim_lpips.txt' \
    --need_post $need_post \

    # # # PSRN SSIM LPIPS
    python -u scripts/metrics/cal_identity_distance.py  \
    $root'/'$test_image \
    --gt_folder $CelebAHQ_GT \
    --save_name $out_root'/'$out_name'_id.txt' \
    --need_post $need_post
else
    echo 'The path of GT does not exist'
fi