# How to use the COCO dataset

```python
# Imports
from icevision.all import *
import icedata

# Load the COCO dataset
path = icedata.coco.load_data()

# Get the class_map, a utility that maps from number IDs to classs names
class_map = icedata.coco.class_map()

# Randomly split our data into train/valid
data_splitter = RandomSplitter([0.8, 0.2])

# COCO parser: provided out-of-the-box
parser = icedata.coco.parser(data_dir=path, class_map=class_map)
train_records, valid_records = parser.parse(data_splitter)

# shows images with corresponding labels and boxes
show_records(train_records[:6], ncols=3, class_map=class_map, show=True)

# load the pretrained model
model = icedata.coco.trained_models.faster_rcnn_resnet50_fpn()
```
