import argparse
import cv2
import sys
import os
import fnmatch
import re

ap = argparse.ArgumentParser()
ap.add_argument('-id', '--idir', required = True, help = 'Path to image')
args = vars(ap.parse_args())

## a function you may want to use in debugging
def display_image_pix(image, h, w):
    image_pix = list(image)
    for r in xrange(h):
        for c in xrange(w):
            print list(image_pix[r][c]), ' ',
        print

## luminosity conversion
def luminosity(rgb, rcoeff=0.2126, gcoeff=0.7152, bcoeff=0.0722):
    return rcoeff*rgb[0]+gcoeff*rgb[1]+bcoeff*rgb[2]

def compute_avrg_luminosity(imagepath):
    im = cv2.imread(imagepath)
    (x, y, z) = im.shape
    imSz = x*y
    total = 0
    for i in xrange(x):
        for j in xrange(y):
            total = total+luminosity(im[i][j])
    return total/imSz
    

def gen_avrg_lumin_for_dir(imgdir, filepat):

    #for imgname in fnmatch.filter(imgdir ,filepat):
            #imgpath = os.path.join(root, imgname) 
    for root, dirs, files in os.walk(imgdir):
        for filename in fnmatch.filter(files, filepat):
            imgpath = os.path.join(root,filename)
            avl=compute_avrg_luminosity(str(imgpath))
            yield filename, avl

## run ghe generator and output into STDOUT           
for fp, lum_avrg in gen_avrg_lumin_for_dir(args['idir'], r'*.png'):
    sys.stdout.write(fp + '\t'  + str(lum_avrg) + '\n')
    sys.stdout.flush()



    

