#!/bin/bash
import argparse
import cv2
import numpy
import math
import sys
import os
import fnmatch

def line_deg_angle(x1, y1, x2, y2):
    return math.degrees(math.atan((y2-y1)/(x2-x1)))

## >>> line_deg_angle(1, 1, 5, 5)
##45.0
##>>> line_deg_angle(0, 5, 5, 0)
##-45.0

def unit_test_01(x1, y1, x2, y2):
    print line_deg_angle(x1, y1, x2, y2)

def draw_lines_in_image(image, lines, color, line_thickness):
    try:
        for ln in lines:
            x1, y1, x2, y2 = ln
            cv2.line(image, (x1, y1), (x2, y2), color, line_thickness)
    except Exception as e:
        print str(e)

def draw_ht_lines_in_image(image, lines, color, line_thickness):
    try:
        for ln in lines:
            x1, y1, x2, y2 = ln[0]
            cv2.line(image, (x1, y1), (x2, y2), color, line_thickness)
    except Exception as e:
        print str(e)

def display_lines_and_angles(lines):
    try:
        for ln in lines:
            x1, y1, x2, y2 = ln
            print (x1, y1, x2, y2), line_deg_angle(x1, y1, x2, y2)
    except Exception as e:
        print str(e)

def display_ht_lines_and_angles(lines):
    try:
        for ln in lines:
            x1, y1, x2, y2 = ln[0]
            print (x1, y1, x2, y2), line_deg_angle(x1, y1, x2, y2)
    except Exception as e:
        print str(e)

def is_angle_in_range(a, ang_lower, ang_upper):
    if a>=ang_lower and a<=ang_upper:
        return True
    else:
        return False

def is_left_lane_line(x1, y1, x2, y2, ang_lower, ang_upper):
    a = line_deg_angle(x1, y1, x2, y2);  
    return is_angle_in_range(a, ang_lower, ang_upper);

def is_right_lane_line(x1, y1, x2, y2, ang_lower, ang_upper):
    a = line_deg_angle(x1, y1, x2, y2)
    return is_angle_in_range(a, ang_lower, ang_upper);

def display_ht_lanes_in_image(image_path, rho_accuracy, theta_accuracy, num_votes, min_len, max_gap):
    image = cv2.imread(image_path) ## read the image
    gray  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) ## grayscale
    edges = cv2.Canny(gray, 50, 150, apertureSize=3) ## detect edges
    lines = cv2.HoughLinesP(edges, rho_accuracy, theta_accuracy, num_votes, min_len, max_gap) ## detect hough lines
    print 'Detected lines and angles:'
    display_ht_lines_and_angles(lines)
    draw_ht_lines_in_image(image, lines, (255, 0, 0), 2)
    cv2.imshow('Gray',  gray)
    cv2.imshow('Edges', edges)
    cv2.imshow('Lines in Image', image)
    cv2.waitKey(0)

def unit_test_02(image_path,  num_votes, min_len, max_gap):
    display_ht_lanes_in_image(image_path, 1, numpy.pi/180, num_votes, min_len, max_gap)

def filter_left_lane_lines(lines, ang_lower=-60, ang_upper=-30):
    filtered_l_lanes = []
    for line in lines:
        if is_left_lane_line(line(1), line(2), line(3), line(4), ang_lower, ang_upper):
          filtered_l_lanes.append(line)
    return filtered_l_lanes

def filter_right_lane_lines(lines, ang_lower=30, ang_upper=60):
    filtered_r_lanes=[]
    for line in lines:
        if is_right_lane_line(line(1), line(2), line(3), line(4), ang_lower, ang_upper):
            filtered_r_lanes.append(line)
    return filtered_r_lanes

## most common value for rho_accuracy is 1
## most common value for theta_accuracy is numpy.pi/180.
## typo with display_line_angles is fixed.
def plot_ht_lanes_in_image(image_path, rho_accuracy, theta_accuracy, num_votes, min_len, max_gap):
    image = cv2.imread(image_path) ## read the image
    gray  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) ## grayscale
    edges = cv2.Canny(gray, 50, 150, apertureSize=3) ## detect edges
    lines = cv2.HoughLinesP(edges, rho_accuracy, theta_accuracy, num_votes, min_len, max_gap) ## detect hough lines
    ## if you want to convert lines from 3D numpy array into 2D Py list, you
    ## conversion should take place here. Then you can call display_lines_and_angles.
    ## Take a look at numpy_opencv_test below to see how that conversion is done.
    display_ht_lines_and_angles(lines)
    cv2.imshow('Gray',  gray)
    cv2.imshow('Edges', edges)
    ## my implementation of filter_left_lane_lines and filter_right_lane_lines returns 2D Py lists, hence
    ## I call draw_lines_in_image, not draw_ht_lines_in_image.
    ll_lines = filter_left_lane_lines(lines)
    rl_lines = filter_right_lane_lines(lines)
    draw_lines_in_image(image, ll_lines, (255, 0, 0), 2)
    draw_lines_in_image(image, rl_lines, (0, 0, 255), 2)
    print 'detected', len(ll_lines), 'left lanes'
    print 'detected', len(rl_lines), 'right lanes'
    cv2.imshow('Lanes in Image', image)
    cv2.waitKey(0)

def detect_ht_lanes_in_image(image_path, rho_accuracy, theta_accuracy, num_votes, min_len, max_gap):
    image = cv2.imread(image_path) ## read the image
    gray  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) ## grayscale
    edges = cv2.Canny(gray, 50, 150, apertureSize=3) ## detect edges
    lines = cv2.HoughLinesP(edges, rho_accuracy, theta_accuracy, num_votes, min_len, max_gap) ## detect hough lines
    #cv2.imshow('Gray',  gray)
    #cv2.imshow('Edges', edges)
    ll_lines = filter_left_lane_lines(lines)
    rl_lines = filter_right_lane_lines(lines)
    draw_lines_in_image(image, ll_lines, (255, 0, 0), 2)
    draw_lines_in_image(image, rl_lines, (0, 0, 255), 2)
    cv2.imwrite(image_path[:-4] + '_lanes' + image_path[-4:], image)
    #print len(ll_lines), len(rl_lines)
    return (len(ll_lines), len(rl_lines))

def unit_test_03(image_path, rho_accuracy, theta_accuracy, num_votes, min_len, max_gap):
    ll, rl = detect_ht_lanes_in_image(image_path, rho_accuracy, theta_accuracy, num_votes, min_len, max_gap)
    print 'number of left lanes:', ll
    print 'number of right lanes:', rl
    
def find_ll_rl_lanes_in_images_in_dir(imgdir, filepat, rho_acc, th_acc, num_votes, min_len, max_gap):
    for im in imgdir:
        if re.match(filepat, im):

def unit_test_04(imgdir, filepat, rho_acc, th_acc, num_votes, min_len, max_gap):
    for fp, ll_rl in find_ll_rl_lanes_in_images_in_dir(imgdir, filepat, 1, numpy.pi/180,
                                         num_votes, min_len, max_gap):
       print fp, ll_rl[0], ll_rl[1]

## these functions are only for debugging.
def numpy_opencv_ht_test(image_path):
    image = cv2.imread(image_path) ## read the image
    gray  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) ## grayscale
    edges = cv2.Canny(gray, 50, 150, apertureSize=3) ## detect edges
    lines = cv2.HoughLinesP(edges, 1, numpy.pi/180, 100, 10, 10) ## detect hough lines
    #print lines.shape
    #display_ht_lines_and_angles(lines)
    print lines

def numpy_opencv_test(image_path):
    image = cv2.imread(image_path) ## read the image
    gray  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) ## grayscale
    edges = cv2.Canny(gray, 50, 150, apertureSize=3) ## detect edges
    lines = cv2.HoughLinesP(edges, 1, numpy.pi/180, 100, 10, 10) ## detect hough lines
    # convert 3D numpy array into a 2D python list
    x, y, z = lines.shape
    lines.shape = (x, z) # drop the y-dimension, because it is always 1
    #print lines
    display_lines_and_angles(lines)
    #print lines
    
## This is the new __main__
if __name__ == '__main__':
    #unit_test_01(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    #plot_ht_lanes_in_image(sys.argv[1], 1, numpy.pi/180, int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    #unit_test_02(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    #unit_test_03(sys.argv[1], 1, numpy.pi/180, int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    #unit_test_04(sys.argv[1], sys.argv[2], 1, numpy.pi/180, int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))
    pass





