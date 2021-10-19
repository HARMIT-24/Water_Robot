# Object Detection in Raspberry Pi
# The post traininng quantised model.
First paste this comand in the terminal of the raspberry pi 
```
pip install tflite_runtime-1.14.0-cp35-cp35m-linux_armv7l.whl
```
To install the Python dependencies, run:
```
pip install -r requirements.txt
```

Next, to run the code on Raspberry Pi, use `classify.py` as follows:

```
python3 main.py --model_path detect.tflite --label_path labelmap.txt
```

For more information, go [here](https://www.tensorflow.org/lite/models/object_detection/overview).

# General Overview
The dataset has been trained using Mobilenet SSD, and is capable of identifying Trash (Taco + UMUNICH dataset: annotated by us), succesfully from differentiatong it between fish, other marine species (Aquarium Dataset) and rocks (UCI Dataset).  
it has been trained using K80 vidia GPU, by Colab for 4000 training epochs and 100 validation set epochs.