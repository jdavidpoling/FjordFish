## Welcome to Fjord Fish. 
### The computer vision north Atlantic marine faunal dataset paired with the Coast Watch "North Atlantic Species Classification" project: https://github.com/jdavidpoling/North-Atlantic-Species-Classification.

![corkwing wrasse](https://github.com/jdavidpoling/FjordFish/blob/main/Images/1407.jpg)

This is a dataset of imagery from baited and unbaited remote underwater video from the Norwegian and Swedish North Atlantic coastlines and acts as a dataset for computer vision model training as well as:
  - model testing and validation
  - model pretraining

The dataset contain approximately 6000 annotations across 3000 images from wild fauna, as well as images of coastal cod gadus _morhua_ of varied sizes and ages from a holding pond resembling wild rocky habitat.

### Download
https://huggingface.co/datasets/jdpoling/FjordFish/tree/main

### Detection and Classification

The dataset contains 28 classes:
  - 23 species level classes i.e. "cod" (gadus _morhua_)
  - 5 uknown or group level classes i.e. "labrids_unknown" (unknown wrasses)

All annotations are bounding boxes contained in text files currently in the You Only Look Once (YOLO) format for YOLOv8+
