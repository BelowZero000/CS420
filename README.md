# Image deblurring and Object detection

[Final Report](https://docs.google.com/document/d/1-79sE9ah7vkfS6oqgzo9WjPBTuuni2KV/edit?usp=sharing&ouid=116476892199540377722&rtpof=true&sd=true)

[Slide](https://www.canva.com/design/DAGar13pzj8/JkLyBy6hiA0hE2kxSGPgkQ/edit?ui=eyJIIjp7IkEiOnRydWV9fQ)

**Dataset preparation**

[GOPRO](https://seungjunnah.github.io/Datasets/gopro)

**Installation**

```pip install -r requirements.txt```

**Train**

```python train.py```

**Test**

Pretrained weights can be [found here](https://drive.google.com/drive/folders/1LzC71JWgb-hX9UuGTHvpCv6cDxis4cIi?usp=drive_link)

```python predict.py -i ./test_img -o ./submit -m ./saved_models/fpn_inception.h5``` 

**App**

```python app.py ```

**Credits**

- [DeblurGANv2](https://github.com/VITA-Group/DeblurGANv2)
- [YOLOv8](https://docs.ultralytics.com/models/yolov8/)
