# -*- coding: utf-8 -*-
"""
Created on Nov 12 2024

OzFish JSON label file conversion to YOLO txt label files

@author: jamesdp

** keep "batch0X" consistent down file (lines 15, 19, 23, 24)
"""

import json, os

# path to json file
with open(r"K:\test\batch03.json") as f:  
    data = [json.loads(line) for line in f]

# location to output .txt label files
output_dir = r"K:\test"

for entry in data:
    image_name = entry['source-ref']
    annotations = entry['batch03']['annotations']
    image_size = entry['batch03']['image_size'][0]
    
    image_width = image_size['width']
    image_height = image_size['height']
    
    yolo_file_name = os.path.join(output_dir, f"{os.path.splitext(image_name)[0]}.txt")
    
    with open(yolo_file_name, 'w') as yolo_file:
        for annotation in annotations:
            class_id = annotation['class_id']
            left = annotation['left']
            top = annotation['top']
            width = annotation['width']
            height = annotation['height']
            
            # convert to YOLO format
            x_center = (left + width / 2) / image_width
            y_center = (top + height / 2) / image_height
            width_norm = width / image_width
            height_norm = height / image_height
            
            # write new label file
            yolo_file.write(f"{class_id} {x_center:.6f} {y_center:.6f} {width_norm:.6f} {height_norm:.6f}\n")

print("JSON Processing Complete")
