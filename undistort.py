#!/usr/bin/env python
import argparse
import os
from glob import glob

import cv2
import numpy as np
import yaml

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Undistort images based on camera calibration.')
    parser.add_argument('calibration', help='input video file')
    parser.add_argument('input_mask', help='input mask')
    parser.add_argument('out', help='output directory')
    args = parser.parse_args()

    with open(args.calibration) as fr:
        c = yaml.safe_load(fr)

    for fn in glob(args.input_mask):
        print(f'processing {fn}...')
        img = cv2.imread(fn)
        if img is None:
            print(f"failed to load {fn}")
            continue

        K_undistort = np.array(c['camera_matrix'])
        # K_undistort[0:2, 2] = [0., 0.]
        # K_undistort[0, 0] *= 0.3
        # K_undistort[1, 1] *= 0.3
        img_und = cv2.undistort(img, np.array(c['camera_matrix']), np.array(c['dist_coefs']),
                                newCameraMatrix=K_undistort)
        name, ext = os.path.splitext(os.path.basename(fn))
        cv2.imwrite(os.path.join(args.out, name + '_und' + ext), img_und)

        print('ok')
